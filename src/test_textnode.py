import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_null(self):
        node = TextNode("This is a text node", TextType.ITALIC, "https://www.boot.dev")
        self.assertIsNotNone(node.url)

    def test_not_eq(self):
        node = TextNode("Let me seee", TextType.ITALIC, "https://www.inculo.it")
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)


if __name__ == "__main__":
    unittest.main()