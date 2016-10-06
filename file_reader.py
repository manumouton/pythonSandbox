import urllib.request
import urllib.parse
import urllib.error


def read_text(path):
    quotes = open(path)
    content = quotes.read()
    print(content)
    check_profanity(content)
    quotes.close()


def check_profanity(text_to_check):
    url = 'http://www.purgomalum.com/service/containsprofanity?text=' + text_to_check
    print(url)
    req = urllib.request.Request(url)
    try:
        response = urllib.request.urlopen(req)
        output = response.read()
        print("output: " + output.decode())
    except urllib.error.URLError as e:
        print(e.reason)


read_text("./quotes.txt")
