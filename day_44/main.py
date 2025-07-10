from bs4 import BeautifulSoup
import lxml

with open("day_44\website.html", 'r') as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")
# soup = BeautifulSoup(contents, "lxml")

# print(soup.title)
# print(soup.title.string)
# print(soup.prettify())

# print(soup.a)

all_anchor_tags = soup.find_all(name = "a")
print(all_anchor_tags)

for tag in all_anchor_tags:
    print(tag.getText())

for tag in all_anchor_tags:
    print(tag.get("href"))

heading = soup.find(name="h1", id="name")
print(heading)

# section_heading = soup.find(name="h3", class="heading") "class" keyword is reserved
section_heading = soup.find(name="h3", class_="heading")
print(section_heading)

h3_heading = soup.select_one(selector="p a")
print(h3_heading)