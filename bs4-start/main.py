from bs4 import BeautifulSoup

import requests

response = requests.get("https://news.ycombinator.com/news")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
print(soup.title)

article_tag = soup.find("span", class_ = "titleline")
article_text = article_tag.getText()
article_link = article_tag.get("href")
# article_upvote = soup.find_all(name="span", class_="score").getText

print(article_tag)
print(article_text)
print(article_link)
# print(article_upvote)


























# import lxml
#
# with open("website.html") as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, "html.parser")
# print(soup.title)
#
# all_anchor_tag = soup.find_all(name="a")
# print(all_anchor_tag)