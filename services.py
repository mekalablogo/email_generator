# import transformers
from huggingface_hub import login
import torch
import requests 
from bs4 import BeautifulSoup
import nltk
import json
import re
from nltk.corpus import stopwords
import asyncio
import aiohttp  # For async HTTP requests

class IntentAndEmailPredictor:
    def __init__(self, model_id="meta-llama/Meta-Llama-3.1-8B-Instruct"):
        """
        Initializes placeholders for model ID, pipeline, and stop words. Use `async_init` to perform initialization.
        """
        
        # Log in with your HuggingFace token
        login("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")

        # Download stopwords
        nltk.download('stopwords')
        self.STOP_WORDS = set(stopwords.words('english'))

        self.pipeline = None
        # Load the model pipeline synchronously
        # self.pipeline = transformers.pipeline(
        #     "text-generation",
        #     model = model_id,
        #     model_kwargs={"torch_dtype": torch.bfloat16},
        #     device_map="auto",
        # )
        
         
    def clean_text(self, text):
        """
        Cleans the given text by removing unwanted characters, words, and stop words,
        and applies lemmatization.
        """
        # Remove non-alphanumeric characters
        text = re.sub(r'[^a-zA-Z0-9.\s]', '', text)
        
        # Split into words, remove stop words, and convert to lowercase
        cleaned_words = [
            word.lower()  # convert to lowercase
            for word in text.split()
            if word.lower() not in self.STOP_WORDS  # Remove stop words
        ]
        print(self.STOP_WORDS)

        return ' '.join(cleaned_words[0:500])  # Limit to the first 500 words
    
    async def extract_headings_and_paragraphs(self, url):
        """
        Extracts headings and paragraphs from a given URL, cleans and processes the text.
        Uses aiohttp for async HTTP requests.
        """
        try:
            # Initialize a list to store extracted information
            content_info = []
            print(url)
            # Send an async HTTP GET request to the URL
            async with aiohttp.ClientSession() as session:
                async with session.get(url) as response:
                    response.raise_for_status()  # Raise an exception for HTTP errors

                    # Parse the page content
                    soup = BeautifulSoup(await response.text(), 'html.parser')

                    # Extract all headings (h1, h2, h3, h4, h5, h6) and paragraphs
                    for tag in soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p']):
                        content_info.append(tag.get_text(strip=True).lower())  # Cleaned text content
            return self.clean_text('.'.join(content_info))  # Return cleaned text

        except aiohttp.ClientError as e:
            print(e)
            return f"Error: {e}"

    async def intent_prediction(self, messages):
        """
        Generates a prediction for the user's intent based on the provided messages.
        """
        if self.pipeline is None:
            return {"reason": "Failed to load the model"}

        # Generate the text based on the provided message
        outputs = await asyncio.to_thread(self.pipeline, messages, max_new_tokens=300)
        
        # Extract the generated content from the output
        content = outputs[0]["generated_text"][-1]["content"]

        # Remove control characters that are not allowed in JSON
        cleaned_content = re.sub(r'[\x00-\x1F\x7F]', '', content)
        return json.loads(cleaned_content)

    async def email_prediction(self, messages):
        """
        Generates a professional email based on the provided message input.
        """
        if self.pipeline is None:
            return {"reason": "Failed to load the model"}

        # Generate the text based on the provided message
        outputs = await asyncio.to_thread(self.pipeline, messages, max_new_tokens=1500)
        
        # Extract the generated content from the output
        content = outputs[0]["generated_text"][-1]["content"]

        # Remove control characters that are not allowed in JSON
        cleaned_content = re.sub(r'[\x00-\x1F\x7F]', '', content)
        return json.loads(cleaned_content)