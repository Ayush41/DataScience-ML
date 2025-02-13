import os
from dotenv import load_dotenv
from groq import Groq


# Load environment variables from the .env file
load_dotenv()

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

# load_dotenv(find_dotenv())
# genai.configure(api_key=os.getenv("GROQ_API_KEY"))
# api_key=os.environ.get("GROQ_API_KEY"),

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Explain the importance of fast language models",
        }
    ],
    model="llama-3.3-70b-versatile",
)

print(chat_completion.choices[0].message.content)