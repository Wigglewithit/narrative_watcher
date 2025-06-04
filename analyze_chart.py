import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
import os

processed_folder = "data/processed/"
category_counts = Counter()

for filename in os.listdir(processed_folder):
    if filename.endswith(".csv"):
        df = pd.read_csv(os.path.join(processed_folder, filename))
        for cat_list in df['Categories']:
            for cat in map(str.strip, cat_list.split(",")):
                category_counts[cat] += 1

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
