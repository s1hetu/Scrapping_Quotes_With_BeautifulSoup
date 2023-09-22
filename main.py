from bs4 import BeautifulSoup
import requests

import csv

response = requests.get('https://www.passiton.com/inspirational-quotes')
soup = BeautifulSoup(response.content, 'html.parser')
all_quotes = soup.find('div', id='all_quotes')
quotes = []
for i in all_quotes.find_all('div', class_="col-6 col-lg-4 text-center margin-30px-bottom sm-margin-30px-top"):
    topic = i.find('h5').text
    link = i.select_one('h5 a')['href']
    img = i.select_one('a img')
    src = img['src']
    title = img['alt'].split('#')[0]
    quote = {
        'topic': topic,
        'title': title,
        'src': src,
        'link': f"https://www.passiton.com/{link}",
    }
    quotes.append(quote)

filename = 'quotes.csv'
# with open(filename, 'w', newline='') as f:
with open(filename, 'w') as f:
    columns = csv.DictWriter(f, ['topic', 'title', 'src', 'link'])
    columns.writeheader()
    for q in quotes:
        columns.writerow(q)
