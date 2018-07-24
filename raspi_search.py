import requests
import bs4
import os

tagpath = os.path.abspath("/home/naohisa/Projects/The-first/test.txt")
print(tagpath)

"""
res = requests.get("https://www.google.co.jp/search?ei=giBXW5TRJoSb8wWhn6OQBA&q=raspberry+pi+ubuntu+chrome&oq=rasberry+pi+ubuntu+chrome&gs_l=psy-ab.1.0.0i13i30k1j0i8i13i30k1l6.34404.52208.0.55757.55.42.11.0.0.0.148.4216.8j30.39.0....0...1c.1j4.64.psy-ab..7.48.4270.6..0j35i39k1j0i4i37k1j0i5i30k1j0i4k1j0i67k1j0i10k1j0i10i67k1j0i4i10k1j0i13k1j0i10i203k1j0i10i30k1j0i19k1j0i13i30i19k1.195.8ALRAPC75qg")

res.raise_for_status()

soup = bs4.BeautifulSoup()"""