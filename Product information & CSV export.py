import requests
from bs4 import BeautifulSoup
import csv


def scrape_products():
    url = "https://books.toscrape.com/"

    response = requests.get(url)

    if response.status_code != 200:
        print("Failed to access the website.")
        print("Status Code:", response.status_code)
        return

    soup = BeautifulSoup(response.text, "html.parser")
    products = soup.find_all("article", class_="product_pod")

    with open("products.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        # Header row
        writer.writerow(["Product Name", "Price", "Rating"])

        print("\n" + "=" * 80)
        print("PRODUCT LIST")
        print("=" * 80)

        for i, product in enumerate(products, start=1):
            name = product.h3.a["title"]
            price = product.find("p", class_="price_color").text
            rating = product.find("p", class_="star-rating")["class"][1]

            # Save to CSV
            writer.writerow([name, price, rating])

            # Display on terminal
            print(f"Product {i}")
            print(f"Name   : {name}")
            print(f"Price  : {price}")
            print(f"Rating : {rating}")
            print("-" * 80)

    print(f"\n{len(products)} products saved to products.csv successfully.")


if __name__ == "__main__":
    scrape_products()