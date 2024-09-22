from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def calculate_similarity(jobs_df, user_profile):
    """Calculates similarity between the user profile and job descriptions."""
    
    # Combine all cleaned job descriptions with the cleaned user profile
    all_texts = jobs_df['Cleaned_Description'].tolist() + [user_profile]

    # Create a TF-IDF matrix
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(all_texts)

    # Compute similarity between the user profile and job descriptions
    similarity_scores = cosine_similarity(tfidf_matrix[-1], tfidf_matrix[:-1])

    # Add the similarity scores to the DataFrame
    jobs_df['Similarity_Score'] = similarity_scores[0]
    
    # Sort the jobs by similarity score (from highest to lowest)
    jobs_df = jobs_df.sort_values(by='Similarity_Score', ascending=False)
    
    return jobs_df