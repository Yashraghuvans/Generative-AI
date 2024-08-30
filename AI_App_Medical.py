from openai from AzureOpenAI
import dotenv
import os

dotenv.load_dotenv();

#insilizing
client=AzureOpenAI{
  azure_endpoint = os.environ["AzureOpenAI_Endpoint"],
  api_key = os.environ['OpenAI_Key'],
  api_version = "2023-10-01-preview"
}

#deployment

deployment=os.environ['AzureOpenAI']


#variables 

problem = input("What is your medical problem = ")
symptoms = input("Your symptoms")
days = input("From how many days are you sick = ")


#prompt

prompt = f" I was having {problem} medical condition and i was sick for {days} days with having these {symptoms} symptoms. 
        Suggest me some primary treatments and medicans for my medical condition "
messages = [{"role": "user", "content": prompt}]

# prints response
print("Primary treatment and medicans :")
print(completion.choices[0].message.content)

new_prompt = f"Create a list of medicans which can be used in {problem} conditions"
messages = [{"role": "user", "content": new_prompt}]
completion = client.chat.completions.create(model=deployment, messages=messages, max_tokens=600, temperature=0)


print("\n=====Medicans list ======= \n")
print(completion.choices[0].message.content)


