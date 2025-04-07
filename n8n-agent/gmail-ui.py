import streamlit as st
import requests

# n8n API URL (replace with the actual URL of your n8n instance)
n8n_url = "http://localhost:5678/webhook-test/send-email"

# Streamlit UI
st.title("Contact Form")

# User input fields
email = st.text_input("Your Email", "")
message = st.text_area("Your Message", "")

# Send button
if st.button("Send Message"):
    if email and message:
        # Prepare the data to send to n8n
        data = {
            "email": email,
            "message": message
        }

        # Send the POST request to n8n
        try:
            response = requests.post(n8n_url, json=data)
            if response.status_code == 200:
                st.success("Your message has been sent successfully!")
            else:
                st.error("Failed to send message. Please try again.")
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.warning("Please fill in both the email and message fields.")
