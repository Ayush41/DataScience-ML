# pages/youtube_summarizer.py
import streamlit as st
import re
import pytube
from youtube_transcript_api import YouTubeTranscriptApi
# from utils.groq_client import get_groq_completion

def extract_video_id(youtube_url):
    """Extract the video ID from a YouTube URL."""
    youtube_id_match = re.search(r'(?:v=|\/)([0-9A-Za-z_-]{11}).*', youtube_url)
    if youtube_id_match:
        return youtube_id_match.group(1)
    return None

def get_video_info(video_id):
    """Get video information using pytube."""
    try:
        youtube = pytube.YouTube(f'https://www.youtube.com/watch?v={video_id}')
        return {
            'title': youtube.title,
            'author': youtube.author,
            'length': youtube.length,
            'thumbnail_url': youtube.thumbnail_url,
            'description': youtube.description
        }
    except Exception as e:
        st.error(f"Error fetching video info: {str(e)}")
        return None

def get_transcript(video_id):
    """Get the transcript for a YouTube video."""
    try:
        transcript_list = YouTubeTranscriptApi.get_transcript(video_id)
        transcript_text = " ".join([item['text'] for item in transcript_list])
        return transcript_text, transcript_list
    except Exception as e:
        st.error(f"Error fetching transcript: {str(e)}")
        return None, None

def summarize_transcript(transcript, video_title=None):
    """Summarize the transcript using Groq API."""
    prompt = f"""
    Please summarize the following YouTube video transcript{' titled "' + video_title + '"' if video_title else ''}.
    
    Focus on extracting:
    1. Main points and key takeaways
    2. Important concepts explained
    3. Organize the summary by topics or timeline
    4. Highlight any actionable insights
    
    Transcript:
    {transcript[:15000]}  # Limiting to avoid token limits
    """
    
    summary = get_groq_completion(prompt)
    return summary

def generate_flashcards(transcript, video_title=None):
    """Generate flashcards from the transcript using Groq API."""
    prompt = f"""
    Based on the following YouTube video transcript{' titled "' + video_title + '"' if video_title else ''}, 
    create 10 flashcards in the following format:
    
    Question: [Question about an important concept from the video]
    Answer: [Concise answer]
    
    Make sure the flashcards cover the most important concepts from the video.
    
    Transcript:
    {transcript[:15000]}  # Limiting to avoid token limits
    """
    
    flashcards = get_groq_completion(prompt)
    return flashcards

def create_timestamps(transcript_list, video_title=None):
    """Create intelligent timestamps for the video using Groq API."""
    # Prepare simplified transcript with timestamps for the AI
    simplified_transcript = []
    for item in transcript_list:
        timestamp_mins = int(item['start'] // 60)
        timestamp_secs = int(item['start'] % 60)
        timestamp = f"{timestamp_mins}:{timestamp_secs:02d}"
        simplified_transcript.append(f"[{timestamp}] {item['text']}")
    
    # Join but limit length to avoid token limits
    simplified_text = "\n".join(simplified_transcript)
    
    prompt = f"""
    Based on the following YouTube video transcript with timestamps{' titled "' + video_title + '"' if video_title else ''}, 
    identify 5-8 key moments or topics discussed in the video.
    
    For each key moment:
    1. Provide the timestamp where this topic begins
    2. Write a brief title for this section
    3. Add a 1-2 sentence description of what's discussed
    
    Format your response as:
    
    ## [timestamp] Topic Title
    Brief description of what's covered in this section.
    
    Transcript with timestamps:
    {simplified_text[:15000]}
    """
    
    timestamps = get_groq_completion(prompt)
    return timestamps

def show():
    st.title("YouTube Video Summarizer & Flashcard Generator")
    st.write("Extract key insights, generate flashcards, and get intelligent timestamps from any YouTube video.")
    
    # URL input
    youtube_url = st.text_input("Enter YouTube Video URL:")
    
    if youtube_url:
        video_id = extract_video_id(youtube_url)
        
        if not video_id:
            st.error("Invalid YouTube URL. Please enter a valid YouTube video URL.")
        else:
            # Get video information
            video_info = get_video_info(video_id)
            
            if video_info:
                # Display video information
                col1, col2 = st.columns([1, 2])
                
                with col1:
                    st.image(video_info['thumbnail_url'], use_column_width=True)
                
                with col2:
                    st.subheader(video_info['title'])
                    st.write(f"By: {video_info['author']}")
                    st.write(f"Length: {video_info['length'] // 60} minutes {video_info['length'] % 60} seconds")
                
                # Get transcript
                transcript_text, transcript_list = get_transcript(video_id)
                
                if transcript_text:
                    # Options for processing
                    st.subheader("What would you like to do with this video?")
                    
                    tab1, tab2, tab3, tab4 = st.tabs(["Summarize", "Flashcards", "Key Timestamps", "Full Transcript"])
                    
                    with tab1:
                        if st.button("Generate Summary"):
                            with st.spinner("Generating summary..."):
                                summary = summarize_transcript(transcript_text, video_info['title'])
                                st.markdown(summary)
                                
                                # Allow downloading the summary
                                st.download_button(
                                    label="Download Summary",
                                    data=summary,
                                    file_name=f"{video_info['title']}_summary.txt",
                                    mime="text/plain"
                                )
                    
                    with tab2:
                        if st.button("Generate Flashcards"):
                            with st.spinner("Creating flashcards..."):
                                flashcards = generate_flashcards(transcript_text, video_info['title'])
                                st.markdown(flashcards)
                                
                                # Allow downloading the flashcards
                                st.download_button(
                                    label="Download Flashcards",
                                    data=flashcards,
                                    file_name=f"{video_info['title']}_flashcards.txt",
                                    mime="text/plain"
                                )
                    
                    with tab3:
                        if st.button("Create Key Timestamps"):
                            with st.spinner("Identifying key moments..."):
                                timestamps = create_timestamps(transcript_list, video_info['title'])
                                st.markdown(timestamps)
                                
                                # Allow downloading the timestamps
                                st.download_button(
                                    label="Download Timestamps",
                                    data=timestamps,
                                    file_name=f"{video_info['title']}_timestamps.txt",
                                    mime="text/plain"
                                )
                    
                    with tab4:
                        st.markdown("### Full Transcript")
                        st.text_area("", transcript_text, height=300)
                else:
                    st.error("Couldn't fetch transcript for this video. The video might not have captions available.")
            else:
                st.error("Couldn't fetch video information. Please check the URL and try again.")
    
    # Usage tips
    with st.expander("Usage Tips"):
        st.markdown("""
        - **Summarize**: Get a concise summary of the main points covered in the video.
        - **Flashcards**: Generate question-answer pairs to test your understanding.
        - **Key Timestamps**: Get an outline of the video with timestamps for easy navigation.
        - **Full Transcript**: View or download the complete transcript of the video.
        
        This tool works best with educational content, lectures, and tutorials.
        """)


# import streamlit as st
# import requests

# # Function to query your n8n workflow or backend
# def get_jobs(location, salary, role):
#     # Example request to your n8n API (replace with your actual API endpoint)
#     response = requests.post(
#         'http://your-n8n-instance-endpoint', 
#         json={
#             'location': location,
#             'salary': salary,
#             'role': role
#         }
#     )
#     return response.json()

# # Streamlit UI
# st.title("Job Search Automation")

# # User inputs
# location = st.text_input("Enter your preferred job location")
# salary = st.number_input("Enter your minimum salary", min_value=0)
# role = st.selectbox("Select a role", ["Data Analyst", "Full Stack Developer", "Other"])

# if st.button('Search Jobs'):
#     if location and salary and role:
#         jobs = get_jobs(location, salary, role)
#         st.write("Jobs Found:")
#         st.write(jobs)
#     else:
#         st.warning("Please fill out all fields")
