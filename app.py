from flask import Flask, render_template
from analysis.analyze_chart import get_category_counts_from_csv

app = Flask(__name__)

@app.route("/")
def index():
    trends = get_category_counts_from_csv()
    return render_template("index.html", trends=trends)


if __name__ == "__main__":
    app.run(debug=True)
