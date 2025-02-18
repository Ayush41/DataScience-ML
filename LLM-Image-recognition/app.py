import streamlit as st
import os 
import google.generativeai as genai
from dotenv import load_dotenv
load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


# loading gemini model and get response

# model = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.3)

model=genai.GenerativeModel("gemini-1.5-flash")
def get_gemini_response(question):
    response = model.generate_content(question)
    return response.text

#app init
st.set_page_config(page_title="Ai-img-redear")
st.header("Gemini-Image-Recognizer")
input= st.text_input("Input: ",key="input")
sumbit = st.button("Ask me anything :)")

if sumbit:
    response = get_gemini_response(input)
    st.write(response)
