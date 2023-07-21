from gnews import GNews

google_news = GNews()
newslist = google_news.get_news('Poverty')
print(newslist[0:5])