import os
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter

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



category_df = pd.DataFrame(category_counts.items(), columns=["Category", "Count"])
category_df = category_df.sort_values(by="Count", ascending=False)

plt.figure(figsize=(10, 6))
plt.bar(category_df["Category"], category_df["Count"])
plt.title("Total Headlines per Category (All Outlets)")
plt.xlabel("Category")
plt.ylabel("Number of Headlines")
plt.xticks(rotation=45)
plt.tight_layout()
plt.grid(axis='y')
plt.show()
