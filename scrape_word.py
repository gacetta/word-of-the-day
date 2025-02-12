import requests
from datetime import date
from bs4 import BeautifulSoup

# get the HTML from the URL source
word_of_the_day_url = "https://www.merriam-webster.com/word-of-the-day/"
response = requests.get(word_of_the_day_url)
if response:
    print("Success!")
else:
    print("Failed to retrieve the page")
    exit()
html_content = response.content

# "Scrape" the html content for what we need
soup = BeautifulSoup(html_content, "html.parser")
word = soup.find('div', class_='word-and-pronunciation').find('h2', class_='word-header-txt').text
definition = soup.select_one('div.wod-definition-container > p').text
part_of_speech = soup.find("span", class_="main-attr").text.strip()
syllables = soup.find("span", class_="word-syllables").text.strip()

# "construct" additional content for md file
link = "https://www.merriam-webster.com/dictionary/" + word
today_date = date.today().strftime("%b %d, %Y")

# Format the data for markdown
markdown = f"""###### *{today_date}*
### [{word}]({link})
<small>*{part_of_speech}*</small> | <small>{syllables}</small>

{definition}

---
"""

# Write to the existing file.
file_path = "word_of_the_day.md"
with open(file_path, "a") as f:
    f.write(markdown)