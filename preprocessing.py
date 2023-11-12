import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer


# remove any url pattern from the text
def remove_url(text):
    url_pattern = r'https?://\S+|www\.\S+'
    cleaned_text = re.sub(url_pattern, '', text)
    return cleaned_text

def preprocess_text(text):
    lemmatizer = WordNetLemmatizer()
    stop_words = set(stopwords.words('english'))

    cleaned_text = remove_url(text)
    # Tokenization
    tokens = word_tokenize(cleaned_text)
    # Remove punctuation and convert to lowercase
    words = [word.lower() for word in tokens if word.isalnum()]
    # Remove stopwords
    words = [word for word in words if word not in stop_words]
    # Lemmatization using WordNetLemmatizer
    words = [lemmatizer.lemmatize(word) for word in words]
    
    return ' '.join(words)