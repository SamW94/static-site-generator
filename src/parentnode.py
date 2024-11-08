from htmlnode import HTMLNode

class ParentNode(HTMLNode):

    def __init__(self, tag, children, props=None): 
        super().__init__(tag=tag, children=children, props=props)
        self.value = None
        
    def to_html(self):
        if self.tag is None:
            raise ValueError("A parent node must have tags.")
        if self.children is None or len(self.children) == 0:
            raise ValueError("A parent node must have children.")
        else:
            all_children = ""
            for child in self.children:
                all_children += child.to_html()
            return f"<{self.tag}{self.props_to_html()}>{all_children}</{self.tag}>"