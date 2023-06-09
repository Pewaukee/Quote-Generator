# define the functions and classes for the api

import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

class API: # class for functionality of the api 
    def __init__(self, model:str) -> None:
        self.model = model
        # create the message list with system 
        self.messages = []
    def add_message(self, role:str, content:str) -> None:
        # add a message to the message list
        self.messages.append({"role": role, "content": content})
    def generate_response(self, prompt:str, max_tokens:int=300, temperature:float=1) -> str: 
        self.add_message("user", prompt)
        # generate a OpenAI response from the prompt and update the corresponding variables
        response = openai.ChatCompletion.create(
            model=self.model,
            messages=self.messages,
            temperature=temperature,
            max_tokens=max_tokens,
        )
        # add the prompt to the messages list
        response_text = response['choices'][0]['message']['content']
        self.add_message("assistant", response_text)
        return response_text
    
            

    