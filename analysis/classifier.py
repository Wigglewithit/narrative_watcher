from transformers import pipeline

# Define your candidate labels
LABELS = [
    # Core mainstream topics
    "Government & Policy",       # Replaces generic "Politics"
    "Civil Rights & Liberties",  # Targets freedom-focused political stories
    "Geopolitical Affairs",      # Covers foreign power moves, alliances, conflicts
    "Economy", "Health", "Technology", "Environment",
    "War", "Crime", "Education", "Science", "Culture",
    "Business", "Entertainment", "Sports", "Opinion",

    # Power & Control themes
    "Surveillance",
    "Corporate Corruption",
    "Private Equity",
    "Financial Manipulation",
    "Wealth Inequality",
    "Media Bias",
    "Deep State",
    "Global Elites",
    "Military Industrial Complex",
    "Political Coverup",
    "Social Engineering",
    "BlackRock",
    "JP Morgan",
    "Warfare Profiteering",
    "Pharmaceutical Influence",
    "Censorship",
    "Disinformation"
]

# Load the model once globally (it will cache after first use)
classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

def classify_headline(text: str):
    result = classifier(text, LABELS)
    top_label = result["labels"][0]
    score = result["scores"][0]
    return top_label, score
