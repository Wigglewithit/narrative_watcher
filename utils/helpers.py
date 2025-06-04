CATEGORIES = {
    "politics": [
        "biden", "trump", "white house", "senate", "congress", "government",
        "lawmakers", "administration", "legislation", "campaign", "election"
    ],
    "military": [
        "army", "veteran", "air force", "navy", "war", "recruiting",
        "missile", "nato", "defense", "troops", "soldier"
    ],
    "business": [
        "deal", "acquired", "merger", "stock", "price", "firm", "ceo", "tech",
        "startup", "inflation", "economy", "billion", "investment"
    ],
    "social": [
        "trans", "race", "gender", "lgbt", "abortion", "rights", "religion",
        "equality", "diverse", "minority", "protest", "student", "classroom"
    ],
    "crime": [
        "attack", "terror", "shooting", "murder", "arrest", "police", "theft",
        "assault", "charged", "suspect", "crime", "killed", "gun"
    ],
    "lifestyle": [
        "diet", "food", "fashion", "celebrity", "father", "mother", "holiday",
        "shopping", "gift", "entertainment", "home", "pets", "fitness"
    ]
}


def categorize_headline(headline):
    tags = []
    for category, keywords in CATEGORIES.items():
        if any(word in headline.lower() for word in keywords):
            tags.append(category)
    return tags or ["uncategorized"]
