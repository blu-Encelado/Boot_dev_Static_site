class HTMLNode():

    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if self.props == None:
            return ""
        
        final = ""

        for key in list(self.props.keys()):
            final += f' {key}="{self.props[key]}"'

        return final
    
    def __eq__(self, other):
        return (self.tag == other.tag
                and self.value == other.value
                and self.children == other.children
                and self.props == other.props
        )

    def __repr__(self):
        return f"tag:{self.tag}, value:{self.value}, children:{self.children}, props:{self.props}"
    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value == None:
            raise ValueError("No Value")
        if self.tag == None:
            return f"{self.value}"
        if self.props == None:
            return f"<{self.tag}>{self.value}</{self.tag}>"
        
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    
    def __eq__(self, other):
        return (self.tag == other.tag
                and self.value == other.value
                and self.props == other.props
        )

    def __repr__(self):
        return f"LeafNode // tag:{self.tag}, value:{self.value}, props:{self.props}"
    
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)
    
    def to_html(self):
        if self.tag == None:
            raise ValueError("No Tag")
        if self.children == None:
            raise ValueError("No Children")
        children_string = ""

        for child in self.children:
            children_string += child.to_html()

        return f"<{self.tag}{self.props_to_html()}>{children_string}</{self.tag}>"
    
    def __eq__(self, other):
        return (self.tag == other.tag
                and self.children == other.children
                and self.props == other.props
        )

    def __repr__(self):
        return f"ParentNode// tag:{self.tag}, children:{self.children}, props:{self.props}"