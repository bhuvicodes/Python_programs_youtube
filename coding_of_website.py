from urllib.request import urlopen
page = urlopen("http://wikipedia.com/")
content = page.read()
print(content)