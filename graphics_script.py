

import tweepy
from tweepy import OAuthHandler

--------

#Para tener acceso a la API se debe crear una cuenta de desarrollador en Twitter la cual proporcionará unas credenciales que usarás en el siguiente fragmento de código, y crearás el acceso a la API con ella
import twitterCredentials

apy_key = twitterCredentials.api_key
api_secret = twiterCredentials.api_secret
access_token = twitterCredentials.access_token
access_secret = twitterCredentials.access_secret

auth = OAuthHandler(api_key, api_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

------------

import csv
import emoji

timeline = api.user_timeline(id="BBVA", count=100, tweet_mode="extended"

#Luego crea el archivo CSV y configura una cabecera de referencia para el manejo de los datos

with open('testcsv.csv', 'w', newline='', encoding='utf-8') as file:
	writer = csv.writer(file)
	writer.writerow(["Date", "Day", "Tweet", "Retweets", "Likes"])
	
	for tweet in timeline:
	text_tweet = tweet.full_text]
	allchars = [str for str in text_tweet]
	emoji_list = [c for c in alchars if c in emoji.UNICODE_EMOJI]
	clean_text = ' '.join([str for str in text_tweet.split() if not any(i in str for i in emoji_list)])
	data = [tweet.created_at.date().strftime("%b %d %Y "), tweet.created_at.date().strftime(%b%d"), cleant_text, tweet.retweet_count, tweet.favorite_count]
	writer.writerow(data)
	
---------------

import pasda as pd
data = pd.read_csv(testcsv.csv")
data

-------------

#Paso 2 Procesamiento

#En un nuevo slot de Jupyter Notebook importa la librería textblob y crea un array que te ayudará a almacenar el valor del sentimiento de cada tweet

from textblob import TextBlob

popularyty_list = []

----------

#Dentro de un ciclo for recorre todos los tweets e imprime el resultado:

for tweet in data ['Tweet']:
	print(tweet)
	
	analysis = TextBlob(tweet)
	analysis = analysis.sentiment
	print(analysis)
	popularity = analysis.polarity
	popularity_list.append(popularity)

-------------

#Paso 3 Despliegue
'''Para mostrar los datos, se necesita de la ayuda de las librerías 
matplolib, que posee una gran variedad de figuras para hacer un gráfico de 
los resultados, y wordcloud que como su nombre lo indica creará una nube de 
palabras con los textos suministrados.'''
'''Con matplotlib realiza la configuración de los parámetros deseados. En este 
caso se configura el tamaño del gráfico, las etiquetas de los ejes y los 
datos a cruzar que pertenecen al día en qué se publicó el tweet contra el 
resultado del sentimiento obtenido en el paso anterior de la siguiente manera'''

%matplotlib inline
import matplotlib.pyplot as plt

-----------

plt.figure(figsize=(20,10))
plt.scatter(data['Day'], popularity_list)
plt title("Sentiments about BBVA and Covid")
pltxlabel("Tweets")
pltylabel("Sentiment")
plt.show()

---------
#Por otra parte, importa la librería wordcloud y configura los parámetros requeridos de color de fondo, tamaño máximo de fuente, etiquetas y el texto a mostrar. En este caso solo se utilizará el texto de uno de los tweets de la siguiente manera:

from wordcloud import WordCloud

# Create and generate a word cloud image:

wordcloud = WordCloud(background_color="white", colormap="Dark2", max_font_sice=150, random_state=42).generate(text_tweet)

#Displayy on the generated image

plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.tittle("BBVA and Covid")
plt.show()











