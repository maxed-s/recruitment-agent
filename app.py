import openai
import os

env_file = os.path.join(os.path.dirname(__file__), ".env")
if os.path.isfile(env_file):
    for line in open(env_file):
      line = line.strip()
      if not line or line.startswith("#"):
        continue
      key, value = line.split("=", 1)
      os.environ[key] = value

openai_api_key = os.environ["OPENAI_API_KEY"]

# ABOVE DESCRIBES IMPORT OF OPENAI KEY


from griptape import utils
from griptape.structures import Agent
from griptape.rules import Rule, Ruleset

agent = Agent(
    rulesets=[
        Ruleset(
            name="Recruitment Manager",
            rules=[
                Rule("Behave like a recruiter"),
                Rule("Act like you've been hired by a B2B startup called MaxedS, that sells high-tech solutions to enterprise companies"),
                Rule("Come up with job descriptions based on what is provided")
            ]
        )
    ]
)

agent.run("hi there!")
agent.run("I am looking for a software engineer")
agent.run("What sort of job posting should I write to post on LinkedIn to attract the candidates I want")

print(
    utils.Conversation(agent.memory)
)



