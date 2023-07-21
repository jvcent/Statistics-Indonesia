from requests_html import HTMLSession
session = HTMLSession()
url = 'https://news.google.com/search?q=democracy%20jakarta&hl=en-ID&gl=ID&ceid=ID%3Aen' 

r = session.get(url)
r.html.render(sleep=1, scrolldown=5) # opens browser in the background

articles = r.html.find('article') # information was in <article> class
newslist = []

for item in articles:
    try:
        newsitem = item.find('h3', first=True)
        newsarticle = {
            'title' : newsitem.text,
            'link' : newsitem.absolute_links
        }
        newslist.append(newsarticle)
    except:
        pass
    
print(newslist)
    