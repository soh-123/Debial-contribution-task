import unittest
from unittest.mock import patch, mock_open
from wiki import fetch_webpage_content, convert_to_markdown


class TestWiki(unittest.TestCase):
    @patch('requests.get')
    def test_fetch_webpage_content(self, mock_requests_get):
        mock_content = '<html><body>Mocked Webpage Content</body></html>'

        mock_requests_get.return_value.text = mock_content

        wiki_url = "https://wiki.debian.org/News"
        content_element = fetch_webpage_content(wiki_url)

        self.assertIsNotNone(content_element)
        self.assertEqual(content_element, mock_content)

    @patch('builtins.open', new_callable=mock_open)
    def test_convert_to_markdown(self, mock_open):
        sample_html = "<h2>Sample HTML</h2>"

        # Mock the file object returned by open
        mock_file = mock_open.return_value

        # Call the function
        convert_to_markdown(sample_html, "test_output")

        # Assertions
        mock_file.write.assert_called_once_with("Sample HTML\n-----------\n\n")

if __name__ == "__main__":
    unittest.main()
