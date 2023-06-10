import time
from api import *
import atexit

MODEL = 'gpt-3.5-turbo'

class MyApp:
    def __init__(self):
        # create instance of API
        self.api = API(MODEL)

    def run(self):
        # Define the prompt
        prompt = "Give me a quote about cooking in the style of Arnold Schwarzenegger."

        # Generate and return the response
        response = self.api.generate_response(prompt)
        print(response)

    def exit_handler(self):
        if self.api:
            # Perform any cleanup or finalization tasks related to the API
            # self.api.cleanup()
            pass

        print("Exiting the program...")

if __name__ == '__main__':
    # Create an instance of the application
    app = MyApp()

    # Register the exit handler
    atexit.register(app.exit_handler)

    # Run the application
    app.run()
