# Quote Generation
The Quote Generation project is a Python-based application that leverages the power of OpenAI to generate different types of quotes. This project allows users to input different topics or themes and receive dynamically generated quotes related to their input.

## Features
* Quote Generation: Enter a topic or theme, and the application will generate a unique and meaningful quote related to that input.
* Customization: Adjust the length and style of the generated quotes to suit your preferences.
* User-Friendly Interface: Enjoy a simple and intuitive command-line interface for interacting with the quote generation functionality.
* OpenAI Integration: Utilize the OpenAI API to generate quotes based on advanced language models and natural language processing.

## Prerequisites
Before using the Quote Generation project, ensure that the following dependencies are installed:

* Install Python's latest version from: https://www.python.org/downloads/release/python-3114/
* Run `pip install -r requirements.txt` to install the dependencies required.

## Getting Started
To get started with the Quote Generation project, follow these steps:

1. Clone the Repository: Clone this repository to your local machine using the following command:

`git clone https://github.com/pewaukee/quote-generation.git`

Configuration: Set up your OpenAI API credentials. Create an account at https://www.openai.com and obtain an API key. Set the API key as an environment variable which will be used in `/src/api.py`.

Run the Application: Execute the Python script `/src/main.py` to launch the quote generation application. Ensure that the necessary dependencies are installed and accessible.

Input and Generate Quotes: Follow the instructions provided by the application to input your desired topic or theme. The application will generate a quote based on your input and display it on the command line.

## Configuration
The Quote Generation project requires configuration settings to connect to the OpenAI API. Update the configuration file config.py with your OpenAI API key or set the API key as an environment variable named OPENAI_API_KEY.

```
OPENAI_API_KEY = 'your-api-key' # or os.getenv('OPEN_API_KEY')
```

## Customization
The quote generation process can be customized based on your preferences. Your output quotes will be based on initial fed system data but also customized by the messages you send in. Further customization can be achieved by directly modifying `/data/messages.txt`.

### Acknowledgements
The Quote Generation project utilizes the OpenAI platform to generate quotes. Powerful language models are the backbone of this application! Feel free to check out this API and others at: https://openai.com/blog/chatgpt-plugins