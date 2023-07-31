from requests_html import HTMLSession
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

session = HTMLSession()
url = 'https://news.google.com/search?q=democracy%20jakarta&hl=en-ID&gl=ID&ceid=ID%3Aen' 

r = session.get(url)
r.html.render(sleep=1, scrolldown=5, timeout=50) # opens browser in the background

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

def sentiment_scores(sentence):
 
    # Create a SentimentIntensityAnalyzer object.
    sid_obj = SentimentIntensityAnalyzer()
 
    # polarity_scores method of SentimentIntensityAnalyzer
    # object gives a sentiment dictionary.
    # which contains pos, neg, neu, and compound scores.
    sentiment_dict = sid_obj.polarity_scores(sentence)

    return sentiment_dict['compound']
     
    # print("Overall sentiment dictionary is : ", sentiment_dict)
    # print("sentence was rated as ", sentiment_dict['neg']*100, "% Negative")
    # print("sentence was rated as ", sentiment_dict['neu']*100, "% Neutral")
    # print("sentence was rated as ", sentiment_dict['pos']*100, "% Positive")
 
    # print("Sentence Overall Rated As", end = " ")
 
    # # decide sentiment as positive, negative and neutral
    # if sentiment_dict['compound'] >= 0.05 :
    #     print("Positive")
 
    # elif sentiment_dict['compound'] <= - 0.05 :
    #     print("Negative")
 
    # else :
    #     print("Neutral")

compound_scores = []
for news in newslist:
    compound_scores.append(sentiment_scores(news['title']))

average = sum(compound_scores) / len(compound_scores)


print("Average Compound Sentiment: " + str(average))
if average >= 0.05 :
    print("Positive")
elif average <= -0.05 :
    print("Negative")
else :
    print("Neutral")