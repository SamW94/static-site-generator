class HTMLNode():

    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def __repr__(self):
        return f"HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props})"

    def __eq__(self, other):
        return self.tag == other.tag and self.value == other.value and self.children == other.children and self.props == other.props 

    def props_to_html(self):
        if self.props is None:
            return ""
        else:
            list_formatted_attributes = []
            for x in self.props:
                list_formatted_attributes.append(f'{x}="{self.props[x]}"')
            return_string = " ".join(list_formatted_attributes)
        return f" {return_string.rstrip()}"