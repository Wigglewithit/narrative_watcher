def save_headlines(headline_data, source):
    import pandas as pd
    import os

    path = f"data/processed/{source}.csv"
    new_data = pd.DataFrame(headline_data)

    if os.path.exists(path):
        existing = pd.read_csv(path)
        combined = pd.concat([existing, new_data]).drop_duplicates(subset=["headline"])
    else:
        combined = new_data

    combined.to_csv(path, index=False)
