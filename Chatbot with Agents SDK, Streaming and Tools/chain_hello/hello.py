import chainlit as cl
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel, RunConfig
from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv())

gemini_api_key= "AIzaSyAx9MTfyN-k-WLnH0Zl-E9rW2sxSN8tM9c"

external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client
)

config= RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True
)

agent1: Agent = Agent(name="Assistant", instructions="You are helpful assistant" , model=model)
result = Runner.run_sync(agent1, "Who is the Founder of Pakistan??", run_config=config)

print('/nCALLING AGENT\n')
print(result.final_output)

@cl.on_chat_start
async def handle_chat_start():
    cl.user_session.set('history' , [])
    await cl.Message("Who is the Founder of Pakistan?").send()


@cl.on_message
async def handle_message(message: cl.Message):
    history = cl.user_session.get("history")
    history.append({"role" : "user" , "content" : message.content})
    result = await Runner.run(
        agent1, 
        input=history,
        run_config=config
    )
    await cl.Message(content=result.final_output).send()