import os
import requests
import pandas as pd
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

def scrape_job_data_adzuna(search_term='Data Scientist', location='Paris'):
    # Load API keys from the .env file
    app_id = os.getenv('ADZUNA_APP_ID')
    app_key = os.getenv('ADZUNA_APP_KEY')

    # Adzuna API URL
    url = f"https://api.adzuna.com/v1/api/jobs/fr/search/1"
    
    # Request parameters
    params = {
        'app_id': app_id,
        'app_key': app_key,
        'results_per_page': 20,
        'what': search_term,
        'where': location
    }
    
    # Send the HTTP request to the Adzuna API
    response = requests.get(url, params=params)
    
    # Check if the request was successful
    if response.status_code != 200:
        print(f"Erreur: {response.status_code}")
        return None
    
    # Extract the results in JSON format
    data = response.json()
    
    # Extract relevant job information
    jobs = []
    for job in data['results']:
        job_info = {
            'Title': job['title'],
            'Company': job['company']['display_name'],
            'Location': job['location']['display_name'],
            'Description': job['description']
        }
        jobs.append(job_info)
    
    # Create a DataFrame from the data
    jobs_df = pd.DataFrame(jobs)
    return jobs_df

# Example usage
if __name__ == '__main__':
    jobs_df = scrape_job_data_adzuna()
    print(jobs_df.head())