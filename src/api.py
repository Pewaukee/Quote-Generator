# define the functions and classes for the api

import openai
import tiktoken
import os
import json

openai.api_key = os.getenv("OPENAI_API_KEY")

class API: # class for functionality of the api 
    def __init__(self, model:str) -> None:
        self.model = model
        # create the message list with system messages from data/messages.json
        with open('data/messages.json', 'r') as file:
            json_data = file.read()
        self.messages = json.loads(json_data)

    def add_message(self, role:str, content:str) -> None:
        # add a message to the message list
        self.messages.append({"role": role, "content": content})

    def generate_response(self, prompt:str, max_tokens:int=300, temperature:float=1.0) -> str: # temp 1.5 to be more creative
        # generate a OpenAI response from the prompt and update the corresponding variables
        response = openai.ChatCompletion.create(
            model=self.model,
            messages=self.messages,
            temperature=temperature,
            max_tokens=max_tokens, # max tokens the API can use in its response
        )
        # add the prompt to the messages list
        response_text = response['choices'][0]['message']['content']
        
        # add the respective strings to their respective lists
        self.add_message("user", prompt)
        self.add_message("assistant", response_text)
        
        return response_text
    
    def count_tokens(self) -> int:
        encoding = tiktoken.encoding_for_model(self.model)
        # only based on the gpt-3.5-turbo
        tokens_per_message = 4
        tokens_per_name = -1
        
        num_tokens = 0
        for message in self.messages:
            num_tokens += tokens_per_message
            for key, value in message.items():
                num_tokens += len(encoding.encode(value))
            if key == "name":
                num_tokens += tokens_per_name
        num_tokens += 3  # every reply is primed with <|start|>assistant<|message|>
        return num_tokens

    def cleanup(self) -> None:
        # save the messages to data/output.json
        with open('data/output.json', 'w') as file:
            json.dump(self.messages, file, indent=4)