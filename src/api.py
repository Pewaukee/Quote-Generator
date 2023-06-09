# define the functions and classes for the api

import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

class API: # class for functionality of the api 
    def __init__(self, model:str) -> None:
        self.model = model
        