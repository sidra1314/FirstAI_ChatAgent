import os
from dotenv import load_dotenv
from agents import (
    Agent,
    Runner,
    set_default_openai_client,
    AsyncOpenAI,
    OpenAIChatCompletionsModel,
    set_tracing_disabled,

)
load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")
external_client = AsyncOpenAI(
    api_key = gemini_api_key,
    base_url = "https://generativelanguage.googleapis.com/v1beta/openai/",
)

set_default_openai_client(external_client)
set_tracing_disabled(True)
model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client,
)

def run_global():
    agent = Agent(
        name = "Assistant",
        instructions = "you are a helpful assistant",
        model = model,
    )

    result = Runner.run_sync(agent,"what is the capital of pakistan")
    print("\n")
    print(result.final_output)
    
if __name__ == "__main__":
    run_global()
    

