import pandas as pd
import requests
from bs4 import BeautifulSoup

import requests


standings_url = 'https://fbref.com/en/comps/9/Premier-League-Stats'

data = requests.get(standings_url)

soup = BeautifulSoup(data.text)

standings_table = soup.select('table.stats_table')[0]

links = standings_table.find_all('a')

#select uses css selectors
#find all only finds tags.
#using list comprehension.
#how does list comprehension work


links = [l.get("href") for l in links]

links = [l for l in links if '/squads/' in l]

team_urls = [f"https://fbref.com{l}" for l in links] 

print(team_urls)


team_url = team_urls[0]

data = requests.get(team_url)

matches = pd.read_html(data.text, match="Scores & Fixtures")

print(matches[0])

soup = BeautifulSoup(data.text)
links = soup.find_all('a')
links = [l.get('href')] for l in links]
links = [l for l in links if l and 'all_comps/shooting/' in links]

print(links)

data = requests.get(f"https://fbref.com{links[0]}")

shooting = pd.read_html(data.text, match='Shooting')[0]

shooting.head()