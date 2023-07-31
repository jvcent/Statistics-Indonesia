from pygooglenews import GoogleNews # error module 'base64' has no attribute 'decodestring'
import pandas as pd

#create the Google News API
gn = GoogleNews(lang='en',country="ID")

#lets create the search
search = gn.search('jakarta poverty')

#lets look at the entries
# for i in search['entries']:
#   print(i)
  
#loop through the actual titles
articles = search['entries']
# for i in articles:
#   print(i.title)
  
#lets create a function that allows us to enter the keyword we want to search
def get_titles(search):
  gn=GoogleNews(lang='en',country='ID')
  search = gn.search(search)
  articles = search['entries']
  for i in articles:
   print(i.title)
  return

get_titles("poverty")

# lets create a dictionary so that we can get the date of publish, link and title
def get_titles(keyword):
  news= []
  gn=GoogleNews(lang='en',country='ID')
  search = gn.search(keyword)
  articles = search['entries']
  for i in articles:
   article= {'title': i.title, 'link': i.link,"published":i.published}
   news.append(article)
  return news

data = get_titles("ポケットモン")

#lets save a data frame so that we can start translating what we have
df = pd.DataFrame(data)

# here is texblob our natural lanaguage processing library
from textblob import TextBlob

# we feed the function the term that we are interested in
blob = TextBlob('Poverty')

# we use translate to with a from language to language
#blob.translate(from_lang='id', to='en')

# let's create a function that bring back sentiment and translateions
def translation(text):
  blob =TextBlob(text)
  return str(blob.translate(from_lang='ja', to='en'))

def sentiment(text):
  blob=TextBlob(text)
  return blob.sentiment.polarity

df['translation'] = df['title'].apply(translation)
df['sentiment'] =df['translation'].apply(sentiment)

# lets create an actual class
import numpy as np

df['Sentiment Class']  = np.where(df['sentiment']<0,"negative",
                                  np.where(df['sentiment']>0,"positive",
                                           "neutral"))

df['Sentiment Class'].value_counts(normalize=True)

df['Date'] = pd.to_datetime(df['published'])
df['Date'] =df['Date'].dt.date

df = df.sort_values(by='Date', ascending=False)
