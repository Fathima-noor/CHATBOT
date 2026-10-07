# # pip install google-genai

from google import genai
#  pip install python-dotenv
from  dotenv import load_dotenv
import os

load_dotenv()

api_key=os.getenv("GEMINI_API_KEY")

client=genai.Client(
    api_key=api_key
)


model="gemini-3.1-flash-lite"

print("Gemini chatbot (type 'exit' to quit)\n")

chat=[]

while True:
    user_input=input("You: ")
    if user_input.lower()=="exit":
        print("Bot: Goodbye")
        break

    chat.append({
        "role" :"user",
        "parts" :[{"text":user_input}]

    })

    response=client.models.generate_content(
        model=model,
        contents=chat
    )


    bot_reply=response.text 
    print("Bot :",bot_reply)

    chat.append({
        "role" :"model",
        "parts":[{"text":bot_reply}]
    })


