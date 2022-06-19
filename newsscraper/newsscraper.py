import requests
from bs4 import BeautifulSoup
import re
def scrape(search):
    url = "https://www.bbc.co.uk/news/world"
    res = requests.get(url)
    doc = BeautifulSoup(res.text, "html.parser")
    guid = doc.find_all("p",text = re.compile(search))
    this_set =set({})
    for art in guid:
        this_set.add(art.string)
    art_arr = []
    for clean_art in this_set:
        art_arr.append(clean_art)
    if not art_arr and search[0] != search[0].upper():
        new_search = search[0].upper() + search[1:]
        art_arr = scrape(new_search)
    return art_arr