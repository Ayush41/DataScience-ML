import streamlit as st
import os 
import google.generativeai as genai
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

import textwrap
import pathlib
from PIL import Image

client = Groq()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# loading gemini model and get response
model = genai.GenerativeModel("gemini-1.5-flash")

def get_gemini_response(input, image):
    if input != "":
        response = model.generate_content(input=input, image=image)
    else:
        response = model.generate_content(image=image)
    return response.text

st.header("Gemini Application")
input = st.text_input("Input Prompt: ", key="input")
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
image = None

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)
    # Convert image to a format that can be passed to the model
    image = image.convert("RGB")

submit = st.button("Tell me about the image")

# if submit clicked
if submit:
    if image is not None:
        response = get_gemini_response(input, image)
        st.subheader("The Response is:")
        st.write(response)
    else:
        st.write("Please upload an image before submitting.")


# import streamlit as st
# import os 
# import google.generativeai as genai
# from dotenv import load_dotenv
# from groq import Groq
# load_dotenv()

# # import textwrap
# # import pathlib
# # from PIL import Image

# genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


# # loading gemini model and get response

# model=genai.GenerativeModel("gemini-1.5-flash")

# def get_gemini_response(input,image):
#     if input !="":
#         response = model.generate_content(input,image)
#     else:
#         response=model.generate_content(image)
#     return response.text


# st.header("Gemini Application")
# input=st.text_input("Input Prompt: ",key="input")
# uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
# image=""   
# if uploaded_file is not None:
#     image = Image.open(uploaded_file)
#     st.image(image, caption="Uploaded Image.", use_column_width=True)


# submit=st.button("Tell me about the image")

# # if submit clicked
# if submit:
#     response = get_gemini_response(input,image)
#     st.subheader("The Response is :")
#     st.write(response)
