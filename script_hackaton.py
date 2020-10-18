
  
#!/usr/bin/env python
# coding: utf-8

# In[23]:


#pip install tinys3


# In[30]:


#pip install -U textblob


# In[28]:


#pip install -U emoji


# In[26]:


#pip install -U wordcloud


# In[7]:


#pip install -U git+https://github.com/tweepy/tweepy.git@2efe385fc69385b57733f747ee62e6be12a1338b
#es necesario instalar tweepy antes de ejecutar los import


# In[47]:


import tweepy
import json
import os
import pandas as pd
from collections import OrderedDict
import requests
import boto3 
comprehend = boto3.client('comprehend', region_name='us-east-1')
from dotenv import load_dotenv


# In[48]:


sample_tweet="It’s always a great day when I can randomly put my equestrian knowledge to good use at work! #AWS #BePeculiar"   

# Key phrases
phrases = comprehend.detect_key_phrases(Text=sample_tweet, LanguageCode='en')

# Entities
entities = comprehend.detect_entities(Text=sample_tweet, LanguageCode='en')

#Sentiments
sentiments = comprehend.detect_sentiment(Text=sample_tweet, LanguageCode='en')


# Print the phrases:
print('------- phrases ---------')
for i in range(0, len(phrases['KeyPhrases'])):
    print((phrases['KeyPhrases'][i]['Text']))
    

# Print the entities with entitity type:
print('------- entity : entity type ---------')
for i in range(0, len(entities['Entities'])):
    print(entities['Entities'][i]['Text'] + ' : ' + entities['Entities'][i]['Type'] )
    
# Print the sentiment:
print('------- sentiment ---------')
print(sentiments['Sentiment'])


# In[49]:


api_key = 'XXXXXX'
api_secret = 'XXXXXXX'
access_token = 'XXXXXXXXXX'
access_secret = 'XXXXXXXXXX'


# In[50]:


#Envoltorio de Python para la API de Twitter
#%%bash
#pip install tweepy


# In[51]:



auth = tweepy.OAuthHandler(api_key, api_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)


# In[75]:


import csv
import emoji

date_since = "2020-01-01"
geocodes = "40.42955,-3.67930,100km"
contry = "Madrid"

#tag = '(bbva OR BBVA) AND (covid OR Covid-19 OR "COVID 19")'
tag = 'BBVA'
#tag = '(BBVA OR bbva OR bancomer OR Bancomer OR BANCOMER OR BBV OR "banco bilbao vizcaya" OR "Banco Bilbao Vizcaya" OR Bancomer OR "Blue Bank" OR "blue bank") AND (covid OR Covid OR COVID)'
#tag = ' AND (virus OR coronavirus OR covid OR covid-19 OR "covid 19" OR pandemia OR antiviral OR N95 OR máscara OR mascarilla OR infectado OR "distanciamiento social" OR SARS-CoV-2 OR SARS OR cov OR síntomas OR "falsos positivos" OR "falso positivo" OR paciente OR pacientes OR serología OR prueba OR "crisis de salud pública" OR "crisis de salud" OR "equipo de protección personal" OR infección OR infecciones OR "riesgo de transmisión" OR desinfectante OR "máscaras faciales" OR "mascarillas faciales" OR infeccioso OR infectado OR contagiado OR infecciosos OR infectados OR contagiados OR virología OR médico OR "este difícil momento" OR sanear OR pruebas OR cuarentena OR cuarentena OR tos OR toser OR fiebre OR hidroxicloroquina OR respiratorio OR respirar OR postmortem OR inflamatoria OR inflamación OR vacuna OR enfermedad OR enfermedades OR enfermedad OR contagioso OR epidemia OR epidemiológico OR epidemiológica OR "la crisis actual" OR emergencia OR "instalaciones de salud" OR máscaras OR máscara OR desinfectante OR antiséptico OR test OR tests OR Virus OR Coronavirus OR Covid OR Covid-19 OR "Covid 19" OR Pandemia OR Antiviral OR N95 OR Máscara OR Mascarilla OR Infectado OR "Distancia social" OR SARS-CoV-2 OR SARS OR Cov OR Síntomas OR "Falsos positivos" OR "Falso positivo" OR Paciente OR Pacientes OR Serología OR Prueba OR "Crisis de salud pública" OR "Crisis de salud" OR "Equipo de protección personal" OR "Infección OR Infecciones" OR "Riesgo de transmisión" OR Desinfectante OR "Máscaras faciales" OR "Mascarillas faciales" OR Infeccioso OR Infectado OR Contagiado OR Infecciosos OR Infectados OR Contagiados OR Virología OR Médico OR "Este difícil momento" OR Sanear OR Pruebas OR "Cuarentena OR Auto-cuarentena" OR "En cuarentena" OR Cuarentena OR "distanciamiento social" OR Tos OR Toser OR Fiebre OR Hidroxicloroquina OR Respiratorio OR Respirar OR Postmortem OR Inflamatoria OR Inflamación OR Vacuna OR Enfermedad OR Enfermedades OR Enfermedad OR Contagioso OR Epidemia OR Peligroso OR Peligro OR Epidemiológico OR Epidemiológica OR "La crisis actual" OR Emergencia OR "Instalaciones de salud" OR Máscaras OR Máscara OR Desinfectante OR Antiséptico OR Test OR Tests)'
#API.search(q[, geocode][, lang][, locale][, result_type][, count][, until][, since_id][, max_id][, include_entities])
tweets = api.search(q=tag, count=100)


# In[76]:


with open('testcsv_100_tweepy_'+contry+'_'+date_since+'.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["Date", "Day", "Tweet", "Retweets", "Likes", "Contry"])

    for tweet in tweets:
        text_tweet = tweet.text
        allchars = [str for str in text_tweet]
        emoji_list = [c for c in allchars if c in emoji.UNICODE_EMOJI]
        clean_text = ' '.join([str for str in text_tweet.split() if not any(i in str for i in emoji_list)])
        data = [tweet.created_at.date().strftime("%b %d %Y %H:%M:%S "),
                tweet.created_at.date().strftime("%b%d "), 
                clean_text, 
                tweet.retweet_count, 
                tweet.favorite_count,
                contry]
        writer.writerow(data)


# In[77]:


import pandas as pd
data = pd.read_csv("testcsv_100_tweepy_"+contry+"_"+date_since+".csv")
data


# In[96]:


posts = []
timestamp = []
locations = []
sentiments = []
positive = []
negative = []
neutral = []

for i in range(len(tweets)):
    d = tweets[i].text
    ts = tweets[i].created_at
    l = tweets[i].user.location
    
    if d != '':
        res = comprehend.detect_sentiment(Text=d, LanguageCode='es')
        s = res.get('Sentiment')
        p = res.get('SentimentScore')['Positive']
        neg = res.get('SentimentScore')['Negative']
        neu = res.get('SentimentScore')['Neutral']
        
    #created_at
    timestamp.append(ts)
    #text
    posts.append(d)
    #user.location
    locations.append(l)
    #Sentiment
    sentiments.append(s)
    positive.append(p)
    negative.append(neg)
    neutral.append(neu)


# In[104]:


import pandas as pd
from collections import OrderedDict

result = pd.DataFrame(OrderedDict( {
            'tweets': posts
         , 'location': pd.Series(locations).str.wrap(15)
         , 'timestamp': timestamp
         , 'sentiment': sentiments
         , 'positiveScore': positive
         , 'negativeScore': negative
         , 'neutralScore' : neutral
         }))


# In[105]:


print("BBVA")
result.groupby(by='tweets')['negativeScore'].mean().sort_values(ascending=False)


# In[106]:


result.groupby(by='location', sort = True)['tweets'].count().sort_values(ascending=False)


# In[117]:


from textblob import TextBlob

popularity_list = []


# In[118]:


for tweet in data ['Tweet']:
    print(tweet)

    analysis = TextBlob(tweet)
    analysis = analysis.sentiment
    print(analysis)
    popularity = analysis.polarity
    popularity_list.append(analysis)


# In[119]:


get_ipython().magic('matplotlib inline')
import matplotlib.pyplot as plt


# In[120]:


plt.figure(figsize=(20,10))
plt.scatter(data['Day'], popularity_list)
plt.title("ZYAN - Sentiments about BBVA in twitter")
plt.xlabel("Tweets")
plt.ylabel("Sentiment")
plt.show()


# In[121]:


from wordcloud import WordCloud

# Create and generate a word cloud image:

wordcloud = WordCloud(background_color="white", colormap="Dark2", max_font_size=150, random_state=42).generate(text_tweet)

#Displayy on the generated image

plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.title("BBVA + COVID 19")
plt.show()


# In[ ]:


api = tweepy.API(auth)
places = api.geo_search(query="USA",granularity="country")
place_id = places[0].id
tweets = api.search(q="place:%s" % place_id)

