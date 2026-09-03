import os
from dotenv import load_dotenv
load_dotenv()
from openai import OpenAI
#from ollama_python import chat


def main():
    llmModel = "Lumina"
    client = OpenAI(
        base_url="http://192.168.1.55:11434/v1/",
        api_key="ollama",  # required but ignored
    )
    print(f"OpenAI moodule found. {llmModel} connected.")
    print(f"{llmModel}:>", end=" ")
    chat_completion = client.chat.completions.create(
        model=llmModel,
        messages=[
            {
                "role": "user",
                "content": input(),
            }
        ],
  
    )
    
    print(f"Prompt tokens: {chat_completion.usage.prompt_tokens}")
    print(f"Response tokens: {chat_completion.usage.completion_tokens}")

    print(chat_completion.choices[0].message.content)
    
if __name__ == "__main__":
    main()
