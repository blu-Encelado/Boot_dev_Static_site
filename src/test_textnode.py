import unittest

from textnode import TextNode, TextType
from split_node import split_nodes_delimiter


class TestTextNode(unittest.TestCase):
    
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_null(self):
        node = TextNode("This is a text node", TextType.ITALIC, "https://www.boot.dev")
        self.assertIsNotNone(node.url)

    def test_not_eq(self):
        node = TextNode("Let me seee", TextType.ITALIC, "https://www.google.it")
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_split_node(self):
        #node = TextNode("This is text with a `code block` word", TextType.TEXT)
        node = TextNode("Despacito is a _great, amazing, incredible_ song to listen", TextType.TEXT)
        new_nodes = f"{split_nodes_delimiter([node], "_", TextType.ITALIC)}"
        string = "[TextNode(Despacito is a , text, None), TextNode(great, amazing, incredible, italic, None), TextNode( song to listen, text, None)]"
        self.assertEqual(new_nodes, string)