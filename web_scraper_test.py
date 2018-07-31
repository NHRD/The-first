import requests
import urllib
import bs4

#this is a comment for test of git push

res = requests.get("https://landing.google.com/sre/book/chapters/foreword.html")
print(type(res))
#print(res.status_code)
soup = bs4.BeautifulSoup(res.text, "html.parser")
so = soup.find_all("a")
print(type(so))

#print(len(so))

"""
res = urllib.request.urlopen("https://news.google.com/")
print(type(res))
html = res.read()
parser = "html.parser"
soup = bs4.BeautifulSoup(html, parser)
so = soup.find_all("a")
print(type(so))

print(len(so))

"""
for tag in soup.find_all("a"):
    url = tag.get("href")
    if url == None:
        continue
    if "html" in url:
        print("\n" + url)
"""