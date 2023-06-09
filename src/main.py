import time
from api import *

MODEL = 'gpt-3.5-turbo'

def main():
    # define simple functionality of the API
    api = API(MODEL)
    # define the prompt
    prompt = "Give me a quote about cooking in the style of Arnold Schwarzenegger."
    # generate and return the response
    response = api.generate_response(prompt)
    print(response)


if __name__ == '__main__':
    main()