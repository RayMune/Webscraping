from bs4 import BeautifulSoup
import requests
import re

url = "https://www.jumia.co.ke/smartphones/samsung/"

result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")

# find all the product containers on the page
product_containers = doc.find_all("article", class_="prd _fb col c-prd")

# loop through the product containers and extract the price for each product
for container in product_containers:
    # extract the price for the current product
    price = container.find("div", class_="prc").text.strip()
    # extract the product name for the current product
    name = container.find("a", class_="core").text.strip()
    print(name + " - " + price)
