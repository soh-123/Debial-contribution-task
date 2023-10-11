import requests
from bs4 import BeautifulSoup
from markdownify import markdownify

HEADER = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
    "Accept-Language": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate, br"
}


def fetch_webpage_content(url):
    """
    Fetches webpage content from the provided URL. 
    Returns the content represented in beatiful soup object
    """
    response = requests.get(url=url, headers=HEADER).text
    soup = BeautifulSoup(response, "html.parser")

    for link in soup.find_all("a"):
        href = link.get("href")
        if href and href.startswith("/"):
            modified_link = "https://wiki.debian.org" + href
            link["href"] = modified_link
    response = str(soup)
    print(response)
    return response


def convert_to_markdown(html_content, file_name):
    """
    Converts HTML content to markdown format and save it to a file.
    """
    markdown_content = markdownify(str(html_content))

    with open(f"{file_name}.md", "w", encoding="utf-8") as markdown_file:
        markdown_file.write(markdown_content)


if __name__ == "__main__":
    wiki_page = "News"
    wiki_url = f"https://wiki.debian.org/{wiki_page}"
    content_element = fetch_webpage_content(wiki_url)
    convert_to_markdown(content_element, wiki_page)
