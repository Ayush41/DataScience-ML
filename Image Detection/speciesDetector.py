import streamlit as st
# from PIL import Image
# from gemini_api import analyze_image

# Streamlit app UI
st.title("🧠 AI Image Recognition - RAG Powered by Gemini")

st.write("Upload an image to recognize objects and species with detailed analysis using the Gemini AI model.")

# File uploader
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

if uploaded_file:
    # Display the uploaded image
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # User input query
    user_query = st.text_input("Ask something about the image (e.g., What species is this?)", "What species is this?")

    if st.button("Analyze Image"):
        st.info("Analyzing the image, please wait...")
        # Call the Gemini AI function
        result = analyze_image(image, user_query)
        # Display results
        st.subheader("Analysis Result:")
        st.write(result)
