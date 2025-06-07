# analysis/analyze_chart.py

import os
import json
import pandas as pd
from collections import Counter
from pathlib import Path

def get_category_counts_from_json():
    path = Path("data/classified_headlines.json")
    if not path.exists():
        return {}
    with open(path, "r", encoding="utf-8") as f:
        headlines = json.load(f)
    categories = [item.get("category") for item in headlines if "category" in item]
    return dict(Counter(categories))


def get_category_counts_from_csv():
    processed_folder = "data/processed/"
    category_counts = Counter()

    for filename in os.listdir(processed_folder):
        if filename.endswith(".csv"):
            df = pd.read_csv(os.path.join(processed_folder, filename))
            if 'label' not in df.columns:
                print(f"⏭️ Skipping {filename} (no 'label' column)")
                continue
            for label in df['label']:
                category_counts[label.strip()] += 1

    return dict(category_counts)

if __name__ == "__main__":
    counts = get_category_counts_from_csv()
    category_df = pd.DataFrame(counts.items(), columns=["Category", "Count"])
    category_df = category_df.sort_values(by="Count", ascending=False)

    import matplotlib.pyplot as plt
    plt.figure(figsize=(10, 6))
    plt.bar(category_df["Category"], category_df["Count"])
    plt.title("Total Headlines per Category (All Outlets)")
    plt.xlabel("Category")
    plt.ylabel("Number of Headlines")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.grid(axis='y')
    plt.show()
