import re
def clean_text(text):
    # 1. Convert text to lowercase
    text = text.lower()
    
    # 2. Remove HTML tags (if text comes from web scraping)
    text = re.sub(r'<.*?>', '', text)
    
    # 3. Remove punctuation and special characters (keep only letters and spaces)
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    
    # 4. Remove extra whitespace
    text = re.sub(r'\s+', ' ', text).strip()
    
    return text