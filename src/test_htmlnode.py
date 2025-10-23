import unittest

from htmlnode import *


class TestTextNode(unittest.TestCase):

    def test_null(self):
        html_node = HTMLNode(tag="p", value="time to crush", children=None, props={"href": "https://www.google.com"})
        self.assertIsNotNone(html_node.tag)

    def test_eq(self):
        html_node_00 = HTMLNode(tag="p", value="time to crush", children=None, props={"href": "https://www.google.com"})
        html_node_01 = HTMLNode(tag="p", value="time to crush", children=None, props={"href": "https://www.google.com"})
        #print(f"//{html_node_00}//")
        self.assertEqual(html_node_00, html_node_01)

    def test_not_eq(self):
        html_node_00 = HTMLNode(tag="a", value="time to crush", children=None, props={"href": "https://www.google.com", "target": "_blank"})
        html_node_01 = HTMLNode(tag="p", value="time to crush", children=None, props={"href": "https://www.google.com"})
        #print(f"##{html_node_00.props_to_html()}")
        self.assertNotEqual(html_node_00, html_node_01)