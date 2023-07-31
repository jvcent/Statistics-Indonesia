# Import Packages
import os
import re
from newscatcherapi import NewsCatcherApiClient
import time

import os
import re
import numpy as np
import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# text treatement
import nltk
from nltk.tokenize import word_tokenize
import string
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Initialize NewsCatcher API
newscatcherapi = NewsCatcherApiClient(x_api_key='imf2EaRbPi56b25D8M0QOdBCM9ZPKG6KQnP1S_1_PZs')

# Extract News
jakarta_poverty = []
jakarta_democracy = []
jakarta_politics = []

for i in range(1, 11):
    jakarta_poverty.extend(newscatcherapi.get_search(q='Jakarta Poverty',
                                         lang='en',
                                         from_='2023-07-15',
                                         to_='2023-07-27',
                                         page_size=100,
                                         page=i)['articles'])
    time.sleep(1)
    
    jakarta_democracy.extend(newscatcherapi.get_search(q='Jakarta Democracy',
                                     lang='en',
                                     from_='2023-07-15',
                                     to_='2023-07-27',
                                     page_size=100,
                                     page=i)['articles'])
    
    time.sleep(1)
    
    jakarta_politics.extend(newscatcherapi.get_search(q='Jakarta Politics',
                                     lang='en',
                                     from_='2023-07-15',
                                     to_='2023-07-27',
                                     page_size=100,
                                     page=i)['articles'])

    time.sleep(1)

print(jakarta_poverty)





# Download and load FinBert pretrained model
# tokenizer = AutoTokenizer.from_pretrained("ProsusAI/finbert")

# model = AutoModelForSequenceClassification.from_pretrained("ProsusAI/finbert")

# nlp = pipeline("sentiment-analysis", model = model, tokenizer=tokenizer)

# possible_sentiments = ['negative', 'neutral', 'positive']

# Get sentiments
# def get_sentiments(input_dict, variable_text):

#     for item_ in input_dict:
#         sentiment = sentiment_analysis(item_[variable_text])
#         for item in sentiment:
#             for shade in possible_sentiments:
#                 if item['label'] == shade:
#                     item_[shade] = item['score']
#                 else:
#                     item_[shade] = 0
                    
#     return input_dict

# jakarta_poverty_pd = pd.DataFrame(get_sentiments(jakarta_poverty, 'title')).loc[:, ['negative', 'neutral', 'positive']]
# jakarta_democracy_pd = pd.DataFrame(get_sentiments(jakarta_democracy, 'title')).loc[:, ['negative', 'neutral', 'positive']]
# jakarta_politics_pd = pd.DataFrame(get_sentiments(jakarta_politics, 'title')).loc[:, ['negative', 'neutral', 'positive']]

# total_score_articles = pd.concat([jakarta_poverty_pd.mean(), jakarta_democracy_pd.mean(), jakarta_politics_pd.mean()], axis=1)
# total_score_articles = total_score_articles.transpose()
# total_score_articles = total_score_articles.reset_index()
# total_score_articles.columns = ['Company', 'negative', 'neutral', 'positive']
# total_score_articles['Company'] = ['Poverty', 'Democracy', 'Politics']

# Graph
# fig = px.histogram(total_score_articles,
#                    x='Company',
#                    title='Sentiment Score by Company | News Articles',
#                    y= ['negative', 'neutral','positive'],
#                    barmode='group',
#                   color_discrete_sequence=["red", "blue", "green"])
# fig.update_xaxes( title='Companies').update_yaxes(title='Sentiment score')
# fig.show()