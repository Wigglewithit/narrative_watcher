import csv
from datetime import datetime
from utils.helpers import categorize_headline

def save_headlines(headlines, source):
    filename = f"data/processed/{source}_{datetime.now().date()}.csv"

    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Headline", "Categories"])

        for line in headlines:
            cats = ", ".join(categorize_headline(line))
            writer.writerow([line, cats])
