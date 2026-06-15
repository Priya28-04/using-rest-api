from dotenv import load_dotenv
import os
from groq import Groq

# Load environment variables
load_dotenv()

# Read API Key
api_key = os.getenv("GROQ_API_KEY")

# Create Groq client
client = Groq(api_key=api_key)

print("Simple Groq Chatbot")
print("Type 'exit' to quit\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Goodbye!")
        break

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": user_input
            }
        ]
    )

    print(
        "\nBot:",
        response.choices[0].message.content,
        "\n"
    )
