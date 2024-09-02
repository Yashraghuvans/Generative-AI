import openai
import dotenv
import os
import request
from PIL import Image

dotenv.load_dotenv()

openai.api_base=os.environ['Azure End Point']
openai.api_key=os.environ['Azure Api_key']
openai.api_version = '2023-06-01-preview'
openai.api_type = 'azure'

generate=openai.Image.create(
  prompt='generate an image of lion with white hairs',
  size='1024x1024',
  n=2,
  temperature=0
)
image_dir = os.path.join(os.curdir, 'images')
if not os.path.isdir(image_dir):
  os.mkdir(image_dir)

image_url = generation_response["data"][0]["url"]  
generated_image = requests.get(image_url).content  
with open(image_path, "wb") as image_file:
  image_file.write(generated_image)

   
image = Image.open(image_path)
image.show()


except openai.InvalidRequestError as err:
    print(err)
