## Debian News Scraper

This project is a Python script that scrapes text from a web page and converts it into a Markdown file. It utilizes the `requests`, `BeautifulSoup`, and `markdownify` libraries to achieve this functionality.

### Usage

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/yourusername/debian-news-scraper.git
   ```

2. Navigate to the project directory:

   ```bash
   cd debian-news-scraper
   ```

3. Install the required Python libraries using pip:

   ```bash
   pip install requests beautifulsoup4 markdownify
   ```

4. Run the script:

   ```bash
   python debian_news_scraper.py
   ```

5. After running the script, a file named `debian_news.md` will be generated in the project directory containing the latest Debian news in Markdown format.

### Dependencies

- [requests](https://pypi.org/project/requests/): Used for making HTTP requests to the Debian Wiki.
- [BeautifulSoup](https://pypi.org/project/beautifulsoup4/): Used for parsing the HTML content of the Debian Wiki.
- [markdownify](https://pypi.org/project/markdownify/): Used for converting HTML content to Markdown format.

### License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.