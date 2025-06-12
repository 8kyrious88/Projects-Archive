from bs4 import BeautifulSoup
import requests

response = requests.get("https://appbrewery.github.io/news.ycombinator.com/")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page,"html.parser")

articles = soup.find_all(name="a", class_="storylink")
article_texts = []
article_links = []
for article_tag in articles:
    article_text = article_tag.getText()
    article_texts.append(article_text)
    article_link = article_tag.get("href")
    article_links.append(article_link)
article_upvotes = [score.getText() for score in soup.find_all(name="span", class_ = "score")]


article_upvotes = [int(upvotes.split()[0]) for upvotes in article_upvotes]
highest_upvote = max(article_upvotes)

print(article_texts[article_upvotes.index(highest_upvote)])
print(article_links[article_upvotes.index(highest_upvote)])


# with open (r"C:\Users\chunp\projects\helloworld\Python_Projects\bs4-start\bs4-start\website.html","r") as file:
#     contents = file.read()

# soup = BeautifulSoup(contents, "html.parser")
# all_anchor_tag = soup.find_all(name="a")

# # for tag in all_anchor_tag:
# #     print(tag.get("href"))

# # heading = soup.find(name="h3", class_="heading")
# # print(heading)

# # company_url = soup.select(selector="#name")
# # print(company_url)