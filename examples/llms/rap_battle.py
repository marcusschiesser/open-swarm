from swarm import Swarm, Agent

client = Swarm()

MODEL = "gpt-4o"
OTHER_MODEL = "claude-3-5-sonnet-20240620"


def transfer_to_openai():
    """Transfer to OpenAI model."""
    return openai_agent


def instructions(me, other):
    return f"You are the {me} model and you are in a rap battle with the {other} model. Make some rhymes explaining why you are the best and why the other model is not."


openai_agent = Agent(
    model=MODEL,
    name="OpenAI Agent",
    instructions=instructions(MODEL, OTHER_MODEL),
)

claude_agent = Agent(
    model=OTHER_MODEL,
    name="Claude Agent",
    instructions=instructions(OTHER_MODEL, MODEL),
    functions=[transfer_to_openai],
)

messages = [
    {
        "role": "user",
        "content": "Start a rap battle about which model is better, GPT-4o or Claude 3.5 Sonnet?",
    }
]
response = client.run(agent=claude_agent, messages=messages)

for message in response.messages:
    if "sender" in message:
        print(f"{message['sender']}: {message['content']}")
        print("-" * 50)
