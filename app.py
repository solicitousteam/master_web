from flask import Flask, render_template, request, jsonify
# import scraper  # Import your scraping script
from test_t import scrap

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/search_product", methods=["GET"])
def search_product():
    product_name = request.args.get("productName")
    # Call your scraping function in scraper.py and get the results
    # results = scraper.scrape_snapdeal(product_name)  # Replace with your scraping function
    results = scrap(product_name)  # Replace with your scraping function

    # Return the results as JSON
    return jsonify(results)

if __name__ == "__main__":
    app.run(debug=True)
# 
