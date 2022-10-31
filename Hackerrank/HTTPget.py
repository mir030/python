import requests
topic = "pizza"
page = requests.get("https://en.wikipedia.org/w/api.php?action=parse&section=0&prop=text&format=json&page=" + topic)
content = str(page.content)
print(content.count(topic))