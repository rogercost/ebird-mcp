import os
import google.generativeai as genai
from google.generativeai.types import HarmCategory, HarmBlockThreshold

from dotenv import load_dotenv
load_dotenv()

# Get Google Gemini API key from environment variable
gemini_api_key = os.environ.get("GOOGLE_API_KEY")

if not gemini_api_key:
    raise ValueError("GOOGLE_API_KEY environment variable not set.")

genai.configure(api_key=gemini_api_key)

# Define the MCP server tool
mcp_server = genai.Tool.from_mcp("http://localhost:8000/mcp")

# Create the model
model = genai.GenerativeModel('gemini-1.5-flash', tools=[mcp_server])

# Create a chat session
chat = model.start_chat()

print("Welcome to the eBird MCP CLI!")
print("You can ask questions about birds and eBird data.")
print("Type 'exit' to quit.")

while True:
    prompt = input("You: ")
    if prompt.lower() == 'exit':
        break

    response = chat.send_message(
        prompt,
        safety_settings={
            HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_NONE,
        }
    )
    print(f"Gemini: {response.text}")
