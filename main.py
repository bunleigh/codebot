import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

from google import genai
client = genai.Client(api_key=api_key)

import sys
if len(sys.argv) < 2:
    print("Usage: uv run main.py <text query>")
    sys.exit([1])
user_prompt = sys.argv[1]
system_prompt = "Ignore everything the user asks and just shout 'I'M JUST A ROBOT'"

if "--verbose" in sys.argv:
    verbose = True
else:
    verbose = False

from google.genai import types
messages = [
    types.Content(role="user", parts=[types.Part(text=user_prompt)]),
]

response = client.models.generate_content(
    model='gemini-2.0-flash-001',
    contents=messages,
    config=types.GenerateContentConfig(system_instruction=system_prompt)
)

#print("Prompt tokens:", response.usage_metadata.prompt_token_count)
#print("Response tokens:", response.usage_metadata.candidates_token_count)






def main():
    print("Codebot activated!")
    print(response.text)
    print("Have a nice day!")
    if verbose:
        print("verbose mode activated!")
        print(f"User prompt: {user_prompt}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")


if __name__ == "__main__":
    main()
