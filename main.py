#!/Users/stephen.porath@siemens.com/Library/CloudStorage/OneDrive-SiemensAG/Dev/Python/boot.dev/ai-agent/bootdev-ai-agent/venv/bin/python3

import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
import sys

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

def main():
    client = genai.Client(api_key=api_key)
    if len(sys.argv) > 1:
        user_prompt = sys.argv[1]
        messages = [
            types.Content(role="user", parts=[types.Part(text=user_prompt)])
        ]
        response = client.models.generate_content(
            model="gemini-2.0-flash-001", 
            contents=messages,
        )
        print(response.text)
        for arg in sys.argv:
            if arg == "--verbose":
                print(f"User prompt: {user_prompt}")
                print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
                print(f"Response tokens:  {response.usage_metadata.candidates_token_count}")
    else:
        print("An argument was not passed.")
        sys.exit(1)

main()
