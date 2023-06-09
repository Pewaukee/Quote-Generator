# define the functions and classes for the api

import openai
import tiktoken
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

class API: # class for functionality of the api 
    def __init__(self, model:str) -> None:
        self.model = model
        # create the message list with system 
        self.messages = [
            {"role": "system", "content": "You are a helpful assistant that specifically works with creating quotes based of the user's prompt."},
            {"role": "system", "content": "Specifically, you should use your creativity to make new and unique quotes."},
            {"role": "system", "content": "Also, make sure you mimic the style of quotations of the given inspiriation."},
            {"role": "system", "content": "For example, if the inspiration is Arnold Schwarzenegger, you should make quotes that sound like Arnold Schwarzenegger said them."},
            {"role": "system", "content": "Add the end of your response, provide the author inspiriation from the user's prompt."},
            {"role": "user", "content": "Give me a quote about love and marriage in the style of Arnold Schwarzenegger."},
            {"role": "assistant", "content": "It's simple, love is like bodybuilding, the last 3-4 reps of love grow the muscle of love. - Arnold Schwarzenegger"},
        ]
    def add_message(self, role:str, content:str) -> None:
        # add a message to the message list
        self.messages.append({"role": role, "content": content})
    def generate_response(self, prompt:str, max_tokens:int=300, temperature:float=1.5) -> str: # temp 1.5 to be more creative
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
            

    