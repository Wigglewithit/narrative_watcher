# Narrative Watcher

Narrative Watcher is a Python-based media scraping and classification tool designed to analyze the thematic distribution of headlines across various news outlets. It scrapes recent headlines, classifies them using a local AI model, and saves the data for further analysis and visualization.

---

## Features

- Scrapes headlines from 40+ diverse news sources
- Performs zero-shot text classification using Hugging Face's `facebook/bart-large-mnli`
- Runs classification fully offline, with no external API or token required
- Saves AI-labeled headlines to CSV with category and confidence score
- Deduplicates headline data across runs
- Generates bar chart visualizations showing headline frequency by category
- Designed with long-term trend analysis in mind

---

## Stack

- Python 3.11+
- `feedparser`
- `transformers`
- `torch`
- `pandas`
- `matplotlib`
- `tqdm`

---

## How to Run

Activate the virtual environment:

```bash
source .venv/Scripts/activate  # Windows Git Bash or similar
