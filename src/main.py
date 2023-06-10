import time
from api import *
import atexit
from pyfiglet import Figlet
from typing import List

MODEL = 'gpt-3.5-turbo'

class MyApp:
    def __init__(self) -> None:
        # create instance of API
        self.api:API = API(MODEL)
        self.messages: List[str] = [] # gather the user messages and responses in a list
        self.user_menu = '''
        0. Quit
        1. Generate a quote
        2. Read the responses
        3. Download the responses?
        '''

    def generate_quote(self, subject:str, inspiration:str) -> str:
        # Generate and return the response
        prompt = f'Generate a quote about {subject} inspired by {inspiration}.\n'
        response = self.api.generate_response(prompt)
        
        self.messages.append(prompt)
        self.messages.append(response)
        
        return response

    def run(self) -> None:
        # Define the main loop of the application
        while True:
            print(self.user_menu)
            choice = input("Enter your choice: ")
            # check invalid input
            if not choice.isdigit() or int(choice) > 3:
                print("Invalid input. Please try again...")
                continue
            if choice == "0":
                break
            elif choice == "1":
                # Get user input
                subject = input("Enter a subject: ")
                inspiration = input("Enter an inspiration: ")

                print("Generating a quote...")
                # Generate the response
                print(self.generate_quote(subject, inspiration))
            elif choice == "2":
                print("Displaying the responses...")
                for message in self.messages:
                    print(message)
            elif choice == "3":
                print("Downloading the responses...")

    def exit_handler(self) -> None:
        # Perform any cleanup or finalization tasks related to the API
        print("Saving the responses...")
        self.api.cleanup()
        print("Exiting the program...")

def main():
    # display a pretty banner
    figlet = Figlet(font='slant')
    figlet.font_size = 20
    banner = figlet.renderText('Quote Generator')
    print(banner)
    print("Welcome to the Quote Generator! Type in a subject and inspiration and we'll generate a quote for you.")
    print("Look at /README.md for more information.")

    # Create an instance of the application
    app = MyApp()

    # Register the exit handler
    atexit.register(app.exit_handler)

    # Run the application
    app.run()

if __name__ == '__main__':
    main()
