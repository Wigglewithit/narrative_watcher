from scraper.cnn import scrape_cnn

def main():
    cnn_headlines = scrape_cnn()
    print("CNN Headlines:")
    for line in cnn_headlines:
        print(f"- {line}")

if __name__ == "__main__":
    main()
