import unittest

from extract_title import extract_title

class TestExtractTitle(unittest.TestCase):

    def test_with_title(self):
        markdown = "# This is a title block\n\nThis is a paragraph block."
        title = extract_title(markdown)
        expected_output = "This is a title block"
        self.assertEqual(title, expected_output)

    def test_with_no_title(self):
        markdown = "## This is trying to be a title\n\nThis is a paragraph block."
        with self.assertRaises(Exception) as context:
            extract_title(markdown)
            self.assertEqual(context, "Markdown file does not contain a valid title.")

    def test_with_large_complex_markdown(self):
        markdown = "# Tolkien Fan Club\n\n**I like Tolkien**. Read my [first post here](/majesty) (sorry the link doesn't work yet)\n\n> All that is gold does not glitter\n\n## Reasons I like Tolkien\n\n* You can spend years studying the legendarium and still not understand its depths\n* It can be enjoyed by children and adults alike\n* Disney *didn't ruin it*\n* It created an entirely new genre of fantasy\n\n## My favorite characters (in order)\n\n1. Gandalf\n2. Bilbo\n3. Sam\n4. Glorfindel\n5. Galadriel\n6. Elrond\n7. Thorin\n8. Sauron\n9. Aragorn\n\nHere's what `elflang` looks like (the perfect coding language):\n\n```func main(){\n fmt.Println('Hello, World!')}\n```"
        title = extract_title(markdown)
        expected_output = "Tolkien Fan Club"
        self.assertEqual(title, expected_output)

if __name__ == "__main__":
    unittest.main()
