import unittest
from extract_markdown_regex import *

class TextExtractMarkdownRegex(unittest.TestCase):

    def test_images(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        output = extract_markdown_images(text)
        expected_output = [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]
        self.assertEqual(output, expected_output)

    def test_links(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        output = extract_markdown_links(text)
        expected_output = [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")]
        self.assertEqual(output, expected_output)

    def test_no_images(self):
        text = "This is text with no images."
        output = extract_markdown_images(text)
        self.assertEqual(output, "There is no text formatted as a markdown image.")

    def test_no_links(self):
        text = "This is text with no links."
        output = extract_markdown_links(text)
        self.assertEqual(output, "There is no text formatted as a markdown link.")

if __name__ == "__main__":
    unittest.main()
