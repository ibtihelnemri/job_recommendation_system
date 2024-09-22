from modules.scraper import scrape_job_data_adzuna
from modules.preprocess import preprocess_jobs, preprocess_user_profile
from modules.matching import calculate_similarity
from modules.llm_integration import generate_custom_job_description

def main():
    # Fetch job data from Adzuna API
    jobs_df = scrape_job_data_adzuna()

    if jobs_df is not None:
        # Preprocess the job descriptions
        jobs_df = preprocess_jobs(jobs_df)

        # Get user profile from input
        user_profile = input("Enter your profile (skills, experience, etc.): ")
        cleaned_profile = preprocess_user_profile(user_profile)

        # Calculate similarity between user profile and job descriptions
        matched_jobs = calculate_similarity(jobs_df, cleaned_profile)
        print("Top job matches based on your profile:\n", matched_jobs[['Title', 'Company', 'Location']].head())

        # Generate a customized job description using OpenAI GPT
        job_title = matched_jobs.iloc[0]['Title']
        job_description = matched_jobs.iloc[0]['Description']
        custom_description = generate_custom_job_description(job_title, job_description, cleaned_profile)
        print("\nCustomized Job Description:\n", custom_description)
    else:
        print("Unable to fetch job data. Please check your API credentials.")

if __name__ == '__main__':
    main()
