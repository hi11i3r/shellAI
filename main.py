import os
import argparse
from dotenv import load_dotenv
load_dotenv()
from openai import OpenAI
#from ollama_python import chat


def main():
    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()
    # Now we can access `args.user_prompt`



    llmModel = "llama3.2"
    client = OpenAI(
        base_url="http://192.168.1.55:11434/v1/",
        api_key="ollama",  # required but ignored
    )
    print(f"OpenAI moodule found. {llmModel} connected.\n")
    messages: list[dict[str, str]]=[
        {
            "role": "user",
            "content": args.user_prompt,
        }
    ]
    #print(f"{llmModel}:>", end=" ")
    chat_completion = client.chat.completions.create(
        model=llmModel,
        messages=messages,
    )
    
    if args.verbose ==  True:
        print(f"User prompt: {args.user_prompt}")
        print(f"Prompt tokens: {chat_completion.usage.prompt_tokens}")
        print(f"Response tokens: {chat_completion.usage.completion_tokens}")

    print(chat_completion.choices[0].message.content)
    
if __name__ == "__main__":
    main()
