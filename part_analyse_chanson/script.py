from collections import Counter
import json
import requests
from bs4 import BeautifulSoup
from pprint import pprint
from pathlib import Path

CURRENT_FILE = Path(__file__).parent
artists = {"PNL" : 335710, "JUL" : 74283, "DAMSO": 45855, "NEKFEU" : 13063, "Johnny Hallyday" : 96830, "Patrick Bruel" : 29743}

def extract_lyrics(url,word_length = 3):
    
    print(f"Fetching lyrics ... {url}")
    r = requests.get(url)
    soup = BeautifulSoup(r.content,"html.parser")
    text = soup.find_all("div", attrs={"data-lyrics-container":"true"})
    
    all_words = []
    not_wanted_char = ["[","]","(",")"]
    for line in text:
        for line_clean in line.stripped_strings:
            sentence_words = [word.strip(",").strip(".").strip("(").strip(")").lower() for word in line_clean.split() if len(word) > word_length and "[" not in word and "]" not in word and "(" not in word and ")" not in word]
            all_words.extend(sentence_words)
    return all_words


def get_all_urls(number_artist):
    page_number = 1
    r = requests.get(f"https://genius.com/api/artists/{number_artist}/songs?page={page_number}&sort=popularity")
    response = r.json().get('response', {})
    next_page = response.get('next_page')
    links = []
    
    if r.status_code == 200:
        while next_page:
            print(f"Fetching page ... {page_number}")
            songs = response.get("songs")
            links.extend([song.get("url") for song in songs])
            # for song in songs: #     link = song.get("url") #     links.append(link)            
            r = requests.get(f"https://genius.com/api/artists/{number_artist}/songs?page={page_number}&sort=popularity")
            response = r.json().get('response', {})
            next_page = response.get('next_page')
            page_number += 1
        print("No more page to fetch")
        return links
    else:
        print("Problème d'URL")

def get_all_words():
    urls = get_all_urls(artists["Patrick Bruel"])
    words = []
    for url in urls:
        lyrics = extract_lyrics(url)
        words.extend(lyrics)
    counter = Counter(words)
    count_words = counter.most_common()
    # print(counter.most_common(15))
    dict_words = {}
    with open(CURRENT_FILE / f"data_json_{artists['NEKFEU']}" ,"w",encoding="utf-8") as f :
        for word in count_words:
            dict_words[word[0]] = word[1]
        json.dump(dict_words,f, indent=4,ensure_ascii=False)
        

get_all_words()