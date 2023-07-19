import openai
import os
from langchain.llms import OpenAI

env_file = os.path.join(os.path.dirname(__file__), ".env")
if os.path.isfile(env_file):
    for line in open(env_file):
      line = line.strip()
      if not line or line.startswith("#"):
        continue
      key, value = line.split("=", 1)
      os.environ[key] = value

my_openai_key = os.environ["OPENAI_API_KEY"]

llm = OpenAI(openai_api_key=my_openai_key)

llm = OpenAI(temperature=0.9)

if __name__ == "__main__":
  print(llm.predict("What would be a good company name for a company that makes colorful socks?"))

