##!pip install tiktoken

import tiktoken

text=f""" Hello welcome to this repo of generative ai """

## ste the model you want 
encoding=tiktoken.encoding_for_model("gpt-3.5-turbo")

##create a prompt to be tokinized 
prompt=f""" ```{text}``` """

##send the token
tokens=encoding.encode(prompt)
print(tokens)


##decode the integer to see what the text is about
[encoding.decode_single_token_bytes(tokesn)for token in tokens]
