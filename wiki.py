
import requests
import bs4

wiki_page = input("Search:")
res = requests.get(f"https://en.wikipedia.org/wiki/{wiki_page}")
res.raise_for_status()

wiki = bs4.BeautifulSoup(res.text, "html.parser")

# Open a file named after the wiki page in write mode
with open(f"{wiki_page}.txt", "w", encoding="utf-8") as f:
    for paragraph in wiki.select("p"):
        f.write(paragraph.getText())


