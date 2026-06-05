
import requests
from bs4 import BeautifulSoup
import csv
url = "https://quotes.toscrape.com"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
quotes = soup.find_all("div", class_="quote")
with open("quotes.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Quote", "Author"])
    for q in quotes:
        quote = q.find("span", class_="text")
        author = q.find("small", class_="author")
        if quote and author:
            writer.writerow([quote.text, author.text])
            print("Data saved successfully!")
           
 