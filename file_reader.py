def read_text(path):
    quotes = open(path)
    content = quotes.read()
    print(content)

read_text("./quotes.txt")
