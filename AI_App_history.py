from openai import AzureOpenAI
import os
import dotenv

#calling dotenv
dotenv.load_dotenv()

#initializing AI
client = AzureOpenAI(
  azure_endpoint = os.environ["Azure_endpoint"],
  api_key=os.environ["Azure_api"],
  api_version = "2023-10-01-preview"
)

deployment = os.environ['Azure_openai_deployment']


#variable define
event = input("Enter the event for which you want information = ")
question = input("How do you want your output (example : essay, points) =")
word_limit = input(" Enter the word limit =")


#prompting
prompt=f"""Give me a breif description about the {event} in a form of {question} and mention all the events in about {word_limit} words."""
message = [{"role" : "user","content" : prompt}]

#completing
completion = client.chat.completions.create(model=deployment, message=message, temperature=0)

#output printing
print(completion.choices[0].message.content)

