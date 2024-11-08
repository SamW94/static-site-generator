from textnode import TextNode, TextType
from htmlnode import HTMLNode

def main():
    textnodeobject = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
    print(textnodeobject)

if __name__ == "__main__":
    main()