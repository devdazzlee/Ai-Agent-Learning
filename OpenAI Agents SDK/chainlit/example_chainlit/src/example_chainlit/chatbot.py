import chainlit as cl
from litellm import completion
import os

os.environ['GEMINI_API_KEY'] = "AIzaSyD4gRQkOAfWHix87V7Lo7fbms8OPdEJplE"

@cl.on_message
async def main(messge: cl.Message):
    print("Messge" ,  cl.Message)
    response = completion(
        model="gemini/gemini-1.5-flash", 
        messages=[{"role": "user", "content": messge.content}]
    )
    print(response['choices'][0]['message']['content'])
    await cl.Message(
        content=f"Response : {response['choices'][0]['message']['content']}"
    ).send()