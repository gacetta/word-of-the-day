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
link = "https://www.merriam-webster.com/dictionary/" + word
today_date = date.today().strftime("%b %d, %Y")

# Format the data for markdown
markdown = f"""
###### *{today_date}*
### [{word}]({link})
{definition}\n

---
"""

# Write to the existing file.
file_path = "word_of_the_day.md"
with open(file_path, "a") as f:
    f.write(markdown)