# LangScraper

## Project Description

LangScraper is a Streamlit application designed to scrape web content and summarize it using the power of language models from LangChain. It automates the process of fetching articles from specified URLs, extracting their main content, and then using language models to identify and summarize the key themes.

## Environment Setup

To run LangScraper, you'll need to have Python installed on your machine. This guide assumes you have Python 3.8 or higher.

### Creating a Virtual Environment

It's recommended to use a virtual environment for Python projects. This keeps your project dependencies isolated from your global Python installation. Here's how you can set it up:

```bash
# Navigate to your project directory
cd path/to/LangScraper
```
```bash
# Create a virtual environment
python -m venv venv
```
```bash
# Activate the virtual environment
# On Windows
venv\Scripts\activate
```
```bash
# On macOS and Linux
source venv/bin/activate
```

### Installing Dependencies
With your virtual environment activated, install the project dependencies by running:

```bash
pip install -r requirements.txt
```

### Setting Up the OpenAI API Key
LangScraper requires an API key from OpenAI to function. To set this up, follow these steps:

1. If you haven't already, generate an API key by visiting OpenAI's API platform.
2. Create a file named .env in the root directory of your project.
3. nside the .env file, add the following line, replacing YOUR_API_KEY_HERE with your actual API key:

```plaintext
OPENAI_API_KEY=YOUR_API_KEY_HERE
```

This file will be automatically loaded by the application, and the API key will be used to authenticate requests to OpenAI.

### Running the Application
Once all dependencies are installed and the API key is set, you can run the LangScraper application using Streamlit:

```bash
streamlit run app.py
```

### Usage
After starting the application, navigate to the provided local URL in your web browser. You'll see an interface where you can enter URLs for scraping and summarization. Simply paste the URLs into the text area, separated by new lines, and press the "Iniciar Scraping e Sumarizar" button to begin the process.

### Contributing
Contributions to LangScraper are welcome! If you have suggestions for improvements or encounter any issues, please feel free to open an issue or submit a pull request.

## More Information

For further information and to get started with LangChain in Python, please visit the [LangChain Python documentation](https://python.langchain.com/docs/get_started/introduction).
