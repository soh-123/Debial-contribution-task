import unittest
import wiki
from unittest.mock import patch

class TestWiki(unittest.TestCase):

    @patch("requests.get")
    def test_fetch_webpage_content(self, mock_requests_get):
        mock_response = mock_requests_get.return_value
        mock_response.text = "<html><body><div id='page'>Mocked Content</div></body></html>"

        # Call the function with a mock URL
        content_element = wiki.fetch_webpage_content("https://wiki.debian.org/News")

        # Check if the function correctly returns the content element
        self.assertIsNotNone(content_element)
        self.assertEqual(content_element.text.strip(), "Mocked Content")

    def test_convert_to_markdown(self):
        mock_html = "<div id='page'>Mocked HTML Content</div>"

        # Call the function to convert to Markdown
        wiki.convert_to_markdown(mock_html, "test_output")

        # Check if the Markdown file was created and has content
        with open("test_output.md", "r", encoding="utf-8") as markdown_file:
            markdown_content = markdown_file.read()
            self.assertTrue(markdown_content.startswith("#"))
            self.assertIn("Mocked HTML Content", markdown_content)

if __name__ == "__main__": 
    unittest.main()