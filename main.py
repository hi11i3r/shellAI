import os
import argparse
import json
from dotenv import load_dotenv
load_dotenv()
from openai import OpenAI
#from ollama_python import chat
from call_function import available_functions

def main():
    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()
    # Now we can access `args.user_prompt`
    system_prompt = """
    You are a helpful AI coding agent.
    When a user asks a question or makes a request, make a function call plan. You can perform the following operations:
    
    - List files and directories
    - Read file contents
    - Execute Python files with optional arguments
    - Write or overwrite files
    
    All paths you provide should be relative to the working directory. You do not need to specify the working directory 
    in your function calls as it is automatically injected for security reasons.
    """
        


    llmModel = "Gormsby"
    client = OpenAI(
        base_url="http://192.168.1.55:11434/v1/",
        api_key="ollama",  # required but ignored
    )
    #print(f"OpenAI module found. {llmModel} connected.\n")
    messages = [
        {
           "role": "user",
            "content": system_prompt
        },
        {
            "role": "user",
            "content": args.user_prompt
        }
    ]
    #print(f"{llmModel}:>", end=" ")
    chat_completion = client.chat.completions.create(
        model=llmModel,
        messages=messages,
        stream=False,
        tools=available_functions,# type: ignore
    )
    
    if args.verbose ==  True:
        print(f"User prompt: {args.user_prompt}")
        print(f"Prompt tokens: {chat_completion.usage.prompt_tokens}") # type: ignore
        print(f"Response tokens: {chat_completion.usage.completion_tokens}") # type: ignore

    massage = chat_completion.choices[0].message
    print(massage.content)

    #if not massage.content:
    #    raise Exception("No reply.")
    #if massage.content:
    #    lastln = massage.content.splitlines()
        #print(lastln)
    #    ll = str(lastln[len(lastln) - 1])
    #print(ll) # type: ignore

    if massage.tool_calls:
        for tool_call in massage.tool_calls:
            function_args = json.loads(tool_call.function.arguments or "{}")
            print(f"Calling function: {tool_call.function.name}({function_args})")
   
   #     for tool_call in massage.tool_calls:
   #         function_args = json.loads(massage.content or "{}") #type: ignore
   #         print(f"Calling function: ({function_args})")
   # if ll:
   # else:
   #     print("No function call")
    
if __name__ == "__main__":
    main()
