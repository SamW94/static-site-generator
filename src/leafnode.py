from htmlnode import HTMLNode

class LeafNode(HTMLNode):

    def __init__(self, tag, value, props=None):
        super().__init__(tag=tag, value=value, props=props)
        self.children = None
        if value == None:
            raise ValueError

    def to_html(self):
        if self.tag is None:
            return self.value
        else:
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
