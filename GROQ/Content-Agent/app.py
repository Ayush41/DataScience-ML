import streamlit as st
from agents import crew

st.title("Content Creation Crew")
topic = st.text_input("Enter a topic:")
if st.button("Generate Content"):
    with st.spinner("Agents at work..."):
        result = crew.kickoff(inputs={"topic": topic})
    st.write(result)