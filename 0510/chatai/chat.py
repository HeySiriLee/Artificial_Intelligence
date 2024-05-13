# Register a library
import openai
import os

OPENAI_KEY = os.environ.get("OPENAI_API_KEY")

# Preferences
# openai key 등록
openai.api_key = OPENAI_KEY

# Select the AI model
MODEL = "gpt-3.5-turbo"

#########################
# ChatCGPT Function
#########################

# User message
# msg = "What's a generative artificial intelligence?"

def ChatMessage(msg):
    response = openai.ChatCompletion.create(
        model = MODEL,
        messages = [
            {"role": "system", "content": "Plz answer in detail"},
            {"role": "user", "content": msg},
            {"role": "assistant", "content": ""},
        ],
        temperature = 0,
    )

    # print(res)
    return response["choices"][0]["message"]["content"]