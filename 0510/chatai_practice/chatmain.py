# Follow the OpenAI Chat Function
from chat import ChatMessage
from chatdb import ChatGPTadd

while True:
    msg = input("Question: ")
    result = ChatMessage(msg)

    # Save the Database
    ChatGPTadd(msg, result)

    print("Answer: ", result)