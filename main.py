#import os
import argparse
import json
from typing import cast
from dotenv import load_dotenv
load_dotenv()
from openai import OpenAI
from openai.types.chat import ChatCompletionToolUnionParam
#from ollama_python import chat
from call_function import available_functions, call_function

def main():
    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()
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
    
    Model = "Gormsby"
    client = OpenAI(
        base_url="http://192.168.1.55:11434/v1/",
        api_key="ollama",  # required but ignored
    )
    print(f"{Model} connected.\n")
    
    messages = [
        {
           "role": "system",
            "content": system_prompt
        },
        {
            "role": "user",
            "content": args.user_prompt
        }
    ]
    
    for msgI in range(30):
    
        chat_completion = client.chat.completions.create(
            model=Model,
            messages=messages,
            stream=False,
            tools=cast(list[ChatCompletionToolUnionParam], available_functions),
            ) 
    
        if args.verbose ==  True:
           print(f"User prompt: {args.user_prompt}")
        if chat_completion.usage is not None:
            print(f"Prompt tokens: {chat_completion.usage.prompt_tokens}")
            print(f"Response tokens: {chat_completion.usage.completion_tokens}")
        
        massage = chat_completion.choices[0].message
        messages.append(massage)

        if massage.tool_calls:
            for tool_call in massage.tool_calls:
                if tool_call.type != "function":
                    continue
                function_args = json.loads(tool_call.function.arguments or "{}")
                if args.verbose:
                    print(f"Requesting function: {tool_call.function.name}({function_args})")
                else:
                    print(f"Requesting {tool_call.function.name}...")
                res_msg = call_function(tool_call, args.verbose)
                if res_msg == None or res_msg['content'] == "":
                    raise Exception("No response from tool call")
                if args.verbose:
                    print(f"-> {res_msg['content']}")
                messages.append(res_msg)
        else:
            print(msgI, massage.content)
            break
    
if __name__ == "__main__":
    main()
