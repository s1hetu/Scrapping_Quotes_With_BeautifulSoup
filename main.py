# import os
# import plivo
# auth_id = "MAZJLJYTU3YZJHNZGXN2"
# auth_token = "NWQyYzIwNGZkMWRlMGVkYmM5NzczOGQzZDY2NmQw"



# client = plivo.RestClient(auth_id, auth_token)
# message_created = client.messages.create(
#     src = '+1573-262-9498',
#     dst = '+1814-377-2883',
#     text='Hello there from Plivo SMS API!'
# )













from bs4 import BeautifulSoup
import requests

# response = requests.get("https://www.tridhya.com/company/team/")
# soup = BeautifulSoup(response.content, "html.parser")
# print(soup, "LLLLLLLLL")
# print(soup.find_all("div", class_="profile-img"))
# member = soup.find_all('div', class_='profile-card-main')
# a=soup.find_all('div', attrs={"class": ['col-md-6', 'col-lg-3', 'profile-card-main']})
# b = soup.find_all("div", class_=["col-md-6","profile-card-main", "col-lg-3", "grid-item-2", "mb-4 profile-card"])
# print(len(member))
# print(len(a))
# print(soup.find("div", class_="col-md-6 col-lg-3 profile-card-main digital-marketing  grid-item-2 mb-4 profile-card"))
# for i in soup.find_all("div", class_="col-md-6 col-lg-3 profile-card-main"):
    # a = i.select("img[src]")
    # print(a, "AAAAAA")

# topic = input("Enter a topic to search on : ")
# topic.replace(' ', '+')
# response = requests.get(f"https://github.com/search?q={topic}")
# data = BeautifulSoup(response.content, 'html.parser')
# for i in data.
#  basic data scrapping -----------------------------------------------------------------
# html_doc = """<html><head><title>The Dormouse's story</title></head>
# <body>
# <p class="title venw" id="hello"><b>The Dormouse's <s>story</s></b><i>WWW</i></p>

# <p class="story">Once upon a time there were three little sisters; and their names were
# <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
# <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
# <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
# and they lived at the bottom of a well.</p>

# <p class="story">...</p>
# """

# soup = BeautifulSoup(html_doc, 'html.parser')
# print(soup.prettify())

# print(soup.p.contents)
# print(soup.p.children)
# print(soup.select('head title')[0].get_text())
# print(soup.select('head > title'))
# print(soup.select('body #link3'))
# print(soup.select('body > #link3'))
# print(soup.select('.sister'))
# print(soup.select('p ~ p'))
# print(soup.find_all(True))

# get all the a tags function based -----------------------------------------------------------
# def my_tag_selector(tag):
# 	# We only accept "a" tags
# 	return tag.name == "a"
# response = requests.get("https://news.ycombinator.com/")
# if response.status_code != 200:
# 	print("Error fetching page")
# 	exit()

# soup = BeautifulSoup(response.content, 'html.parser')

# print(soup.find_all(my_tag_selector), len(soup.find_all(my_tag_selector)))

# get all required tags function based with partial -------------------------------------------------------
# from functools import partial

# def my_tag_selector(tag, tagname):
#     # print(tag)
#     # print(tagname)
#     return tag.name == tagname

# response = requests.get("https://news.ycombinator.com/")
# soup = BeautifulSoup(response.content, 'html.parser')
# soup_x = partial(my_tag_selector, tagname='a')

# print(soup.find_all(soup_x), len(soup.find_all(soup_x)))

# get the site data simple ---------------------------------------------------------------------
# site = requests.get("https://realpython.github.io/fake-jobs/")
# soup = BeautifulSoup(site.content, 'html.parser')
# div_con = soup.find_all('div', class_="column is-half")
# # get all data
# for j,i in enumerate(div_con):
#     designation = i.find('h2', {'class': 'title'}).text
#     company = i.find('h3', class_="company").text
#     location = i.find('p', class_='location').text
#     date = i.find('time').text
#     buttons = i.find_all('a', class_="card-footer-item")

#     print("Id :",j)
#     print("designation :", designation)
#     print("company :", company)
#     print("location :", str(location).strip())
#     print("date :", date)
#     print(f"Buttons are : {buttons[0].text.strip()} ({buttons[0]['href']}) {buttons[1].text.strip()} ({buttons[1]['href']}) \n")

# get the designation exact data --------------------------------------------------------------------
# site = requests.get('https://realpython.github.io/fake-jobs/')
# soup = BeautifulSoup(site.content, 'html.parser')
# match the string (not in string)
# jobs = soup.find_all('h2', class_='title', string="Software")
# for i in jobs:
#     print(i)

# get the designation in title data -----------------------------------------------------------------
# site = requests.get('https://realpython.github.io/fake-jobs/')
# soup = BeautifulSoup(site.content, 'html.parser')
# # The lambda function looks at the text of each <h2> element having class title, converts it to lowercase, and checks whether the substring "python" is found anywhere.
# jobs = soup.find_all('h2', class_="title", string=lambda textki: "python" in textki.lower())
# for i in jobs:
#     print(i.text)
# we cant get these data bcoz we have find the h2 element and there are no elements present inside it, so we cant get the data like this
#     designation = i.find('h2', {'class': 'title'}).text
#     company = i.find('h3', class_="company").text
#     location = i.find('p', class_='location').text

# response = requests.get('https://realpython.github.io/fake-jobs/')
# soup = BeautifulSoup(response.content, 'html.parser')
# h2_match = soup.find_all('h2', class_="title", string=lambda text: "python" in text.lower())
# # We have wrote parent thrice : parent of h2 is media-content(1), parent of media-content is media(2), and parent of media is card-content; inside which all the information is stored
# h2_match_elements = [element.parent.parent.parent for element in h2_match]
# for i in h2_match_elements:
#     designation = i.find('h2', class_='title').text
#     company = i.find('h3', class_='company').text
#     location = i.find('p', class_="location").text
#     time = i.find('time').text.strip()
#     buttons = i.find_all('a', class_='card-footer-item')
#     print("designation", designation)
#     print("company :", company)
#     print("location :", str(location).strip())
#     print("date :", time)
#     for link in buttons:https://github.com/s1hetu/beautifulsoup.githttps://gghpithub.com/s1hetu/beautifulsoup.git
#         print(f"To {link.text}, visit {link['href']}")
    

# response = request.get()
import csv
response = requests.get('https://www.passiton.com/inspirational-quotes')
soup = BeautifulSoup(response.content, 'html.parser')
all_quotes = soup.find('div', id='all_quotes')
quotes= []
for i in all_quotes.find_all('div', class_="col-6 col-lg-4 text-center margin-30px-bottom sm-margin-30px-top"):
    topic = i.find('h5').text
    link = i.select_one('h5 a')['href']
    img = i.select_one('a img')
    src = img['src']
    title = img['alt'].split('#')[0]
    quote = {'topic':topic, 'title':title, 'src':src, 'link':"https://www.passiton.com/"+link}
    quotes.append(quote)
    
filename = 'quotes.csv'
# with open(filename, 'w', newline='') as f:
with open(filename, 'w') as f:
    columns = csv.DictWriter(f, ['topic', 'title', 'src', 'link'])
    columns.writeheader()
    for q in quotes:
        columns.writerow(q)
