from collections import Counter
import re

# Common words to skip
STOP_WORDS = {
    "the", "a", "and", "in", "to", "of", "on", "for", "at", "with", "from",
    "by", "an", "as", "is", "are", "was", "were", "be", "has", "have", "it",
    "this", "that", "but", "not", "or", "you", "they", "their", "its"
}

def extract_keywords(headlines, top_n=10):
    words = []

    for headline in headlines:
        # Remove punctuation and make lowercase
        cleaned = re.sub(r'[^\w\s]', '', headline.lower())
        words.extend(cleaned.split())

    # Remove stop words
    filtered_words = [word for word in words if word not in STOP_WORDS]

    # Count and return the top N keywords
    counter = Counter(filtered_words)
    return counter.most_common(top_n)
