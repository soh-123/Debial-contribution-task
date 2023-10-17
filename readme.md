## Convert HTML Webpage to Markdown File

This Python project is designed to fetch webpage content from a provided URL, convert it from HTML to Markdown format, and save it to a file.

### Features
- Fetches webpage content from a URL.
- Converts HTML content to Markdown format.
- Saves the Markdown content to a file.

### Installation

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/yourusername/Debian-Contribution-Task
   ```

2. Navigate to the project directory:

   ```bash
   cd Debian-Contribution-Task
   ```

3. Install the required Python libraries using pip:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the script:

   ```bash
   python wiki.py
   ```

5. After running the script, a file will be generated in the project directory containing Debian web content in Markdown format.

### Usage
1. Open the '**wiki.py**' file and customize the wiki_page and '**wiki_url**' variables with your desired webpage details.

2. Run the script:

```bash
python wiki.py
```
This will fetch the webpage content, convert it to Markdown, and save it to a file.

### Testing
This project includes unit tests to verify the functionality of the HTML to Markdown conversion. You can run the tests using the following command:

```bash
python -m unittest test_wiki.py
 ```


### Dependencies

- [requests](https://pypi.org/project/requests/): Used for making HTTP requests to the Debian Wiki.
- [BeautifulSoup](https://pypi.org/project/beautifulsoup4/): Used for parsing the HTML content of the Debian Wiki.
- [markdownify](https://pypi.org/project/markdownify/): Used for converting HTML content to Markdown format.

### License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.