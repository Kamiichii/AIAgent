import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
from functions.system_prompt import *

def main():

    load_dotenv()

    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    user_input = " ".join(sys.argv[1:])
    verbose = "--verbose" in sys.argv

    if user_input.strip() == "":
        print('You need to input a string after calling the program like python main.py "my input"')
        sys.exit(1)

    messages = [
    types.Content(role="user", parts=[types.Part(text=user_input)]),
    ]

    response = client.models.generate_content(model ="gemini-2.0-flash-001", 
                                              contents =messages,
                                              config=types.GenerateContentConfig(tools =[available_functions], system_instruction=SYSTEM_PROMPT))
 
    if response.function_calls: 
       for function_call_part in response.function_calls:     
        print(f"Calling function: {function_call_part.name}({function_call_part.args})")

    print(f"User prompt:{str(response.text)}")
    
    if verbose:       
        print(f"Prompt tokens: {str(response.usage_metadata.prompt_token_count)}")
        print(f"Response tokens: {str(response.usage_metadata.candidates_token_count)}")


if __name__ == "__main__":
    main()
