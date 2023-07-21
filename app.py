import openai
import os
import re
from flask import Flask, render_template, request

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
from griptape.utils import Chat

app = Flask(__name__)


@app.route("/")
def index():
   return render_template("index.html")

@app.route("/finance", methods=["GET", "POST"])
def finance():
    if request.method == "POST":
       agent = Agent(
       rulesets = [
          Ruleset(
       name="Fractional CFO", 
       rules=[
          Rule("Behave like an efficient fractional CFO"), 
          Rule("Act like you work for MaxedS, a startup designed to help other businesses be more efficient"),
          Rule("Discuss only topics related to what a CFO discusses: business forecasting, depositing money, processing invoices, brainstorming financial strategy")
       ]
          )
       ]
    )
       message = request.form.get("message", "")
       agent.run(message)
       full_agent_response = str(utils.Conversation(agent.memory))
    
       with_space = full_agent_response.replace(message, message+"<br>")
       with_agent = with_space.replace("A: ", "<b>Agent:</b> ")
       with_question = with_agent.replace("Q: ", "<b>You:</b> ")

       
          
       return render_template("finance.html", chat=with_question) 
    else:
       return render_template("finance.html", chat="")

@app.route("/job_posting_input")
def job_posting_input():
   return render_template("job_posting_input.html")

@app.route("/job_posting", methods=["POST"])
def job_posting_generator():
    role = request.form.get("role", "")
    agent = Agent(
    rulesets=[
        Ruleset(
            name="Recruitment Manager",
            rules=[
                Rule("Behave like a recruiter"),
                Rule("Write a fully-featured job posting, intended to be posted on LinkedIn, based on the role that is specified"),
                #Rule("Come up with job descriptions based on what is provided")
            ]
        )
    ]
)


    #Chat(agent).start()
    agent.run("Write a fully featured LinkedIn job posting for a " + role)



    string_conversation =  str(utils.Conversation(agent.memory)) # gotta convert griptape conversation object to string

    #job_description = string_conversation[74:]
    job_description = string_conversation

    start_index = job_description.find("A:")
    description_index = 0

    if start_index != -1: 
        description_index = start_index + 3
        sliced_string = job_description[description_index:]

    else: 
        sliced_string = "Unavailable"

    list_of_headings = ["Company:", "Location:", "Job Type:", "About Us:", "Job Description:", "Responsibilities:", "Requirements:", "Benefits:", "How to Apply:" "Note:"]

    for heading in list_of_headings:
        modified_heading = '<br><br>' + heading
        sliced_string = sliced_string.replace(heading, modified_heading)

    #return job_description
    return render_template('job_posting.html', job_posting=sliced_string)

   
    
   
   

if __name__ == "__main__":
   port = int(os.environ.get("PORT", 3000))
   app.run(host="0.0.0.0", port=port)
