import openai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Fetch OpenAI API key
openai.api_key = os.getenv('OPENAI_API_KEY')

def get_llm_response(prompt):
    """Calls the OpenAI API to generate a response based on the given prompt."""
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # You can also use gpt-4 if available
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
        ]   
        )
        return response['choices'][0]['message']['content'].strip()
    except openai.error.RateLimitError as e:
        print("Rate limit exceeded. Please check your API usage and billing details.")
        return "Error: Rate limit exceeded."
    except openai.error.InvalidRequestError as e:
        print(f"Invalid request: {e}")
        return "Error: Invalid request."
    except openai.error.OpenAIError as e:
        print(f"An error occurred: {e}")
        return "Error: OpenAI API error."

def generate_custom_job_description(job_title, job_description, user_profile):
    """Generates a customized job description based on the user's profile."""
    prompt = f"""
    The job title is '{job_title}', and the job description is '{job_description}'.
    The user profile includes the following skills: {user_profile}.
    Based on this, can you rewrite the job description to highlight why this user is a good fit for the role?
    """
    return get_llm_response(prompt)



