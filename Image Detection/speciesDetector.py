import streamlit as st
# from PIL import Image
# from gemini_api import analyze_image

# Streamlit app UI
st.title("🧠 AI Image Recognition - RAG Powered by Gemini")

st.write("Upload an image to recognize objects and species with detailed analysis using the Gemini AI model.")

# File uploader
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

