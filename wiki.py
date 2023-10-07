import requests
from bs4 import BeautifulSoup
from markdownify import markdownify

wiki_url = "https://wiki.debian.org/News"
HEADER = {
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
    "Accept-Language":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding":"gzip, deflate, br"
}

response = requests.get(url=wiki_url, headers=HEADER).text
soup = BeautifulSoup(response, "html.parser")

content_element = soup.find("div", {"id": "page"})
markdown_content = markdownify(str(content_element))

# Write the content to a Markdown file
with open("debian_news.md", "w", encoding="utf-8") as markdown_file:
    markdown_file.write(markdown_content)

