from textnode import TextNode, TextType

def main():
    object = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
    print(object)

if __name__ == "__main__":
    main()