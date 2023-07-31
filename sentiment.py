from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import requests
# SSL: CERTIFICATE_VERIFY_FAILED

root = 'https://www.google.com/'
link = 'https://www.google.com/search?client=safari&rls=en&q=jakarta&ie=UTF-8&oe=UTF-8'

req = Request(link, headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()
print(webpage)