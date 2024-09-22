import spacy

# Load the English language model from spaCy
nlp = spacy.load('en_core_web_sm')

def clean_text(text):
    """Cleans and lemmatizes a given text."""
    doc = nlp(text)
    tokens = [token.lemma_.lower() for token in doc if not token.is_stop and not token.is_punct]
    return ' '.join(tokens)

def preprocess_jobs(jobs_df):
    """Applies text cleaning to job descriptions in a DataFrame."""
    jobs_df['Cleaned_Description'] = jobs_df['Description'].apply(clean_text)
    return jobs_df

def preprocess_user_profile(user_profile):
    """Cleans and lemmatizes the user profile."""
    return clean_text(user_profile)