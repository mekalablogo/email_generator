from fastapi import FastAPI,HTTPException,APIRouter
from models import InputData
from services import IntentAndEmailPredictor

from prompt_functions import (EmailPromptGenerator,IntentPromptGenerator,example_email)


# Create a FastAPI instance
email_generator= APIRouter()

# Initialize the IntentAndEmailPredictor class
intent_email = IntentAndEmailPredictor()

# Define a POST endpoint for generating email content
@email_generator.post("/generate-email/")
async def generate_synthetic_mail(data: InputData):
    """
    Validates the input data, processes it for intent and email generation, 
    and returns the predicted intent and generated email.
    """
    
    # Extract the user's first part of the email (before the '@' and '.') for their name
    user_name = data.email.split('@')[0].split('.')[0]
    
    # Initialize a dictionary to store the headings and paragraphs of the last visited pages
    last_visited_pages = {}
    print(data.last_3_pages_visited)
    # Loop through each of the last visited pages and extract headings and paragraphs
    for url in data.last_3_pages_visited:
        last_visited_pages[f"{str(url)}"] = await intent_email.extract_headings_and_paragraphs(str(url))
        print(last_visited_pages[f"{str(url)}"])
    
    print('success')
    # Initialize the IntentPromptGenerator class with the data to create an intent prompt
    intent_prompt_generator = IntentPromptGenerator(
                                        last_visited_websites = data.last_3_pages_visited,
                                        user_message = data.message)
    
    # Generate the intent prompt template based on the provided data
    intent_prompt = await intent_prompt_generator.generate_intent_prompt_template()

    # Generate the intent messages using the generated intent prompt
    intent_user_messages = await intent_prompt_generator.intent_messages(intent_prompt)

    # Use the intent_email object to predict the intent using the generated messages
    intent_result = await intent_email.intent_prediction(intent_user_messages)
    print(intent_result)
    intent_class = intent_result["intent"],
    intent_class_reason = intent_result["explanation"]
    
    # Initialize the EmailPromptGenerator class with data to create an email prompt
    email_prompt_generator = EmailPromptGenerator(
                                    last_visited_pages = last_visited_pages,
                                    user_name = user_name,
                                    user_message = data.message,
                                    intent_class = intent_class,
                                    intent_class_reason = intent_class_reason,
                                    example_email = example_email
                                )
    
    
    # Generate the email prompt using the email prompt generator
    email_prompt = await email_prompt_generator.generate_email_prompt_template()
    
    # Generate the email messages using the generated email prompt
    email_user_message = await email_prompt_generator.email_messages(email_prompt)

    # Use the intent_email object to predict the email content using the generated email messages
    synthetic_email = await intent_email.email_prediction(email_user_message)
    
    # Return the predicted intent and generated email as a response
    return {
        "intent": intent_result,
        "email": synthetic_email
    }

