#enconding:utf-8
import tweepy
import configparser
import pandas as pd
import pymysql
from agregar_tw import addTweets

#leer el archivo de configuracion de tokens de twitter

config = configparser.ConfigParser()
config.read('config.ini')

api_key = config['twitter']['api_key']
api_key_secret = config['twitter']['api_key_secret']

access_token = config['twitter']['access_token']
access_token_secret = config['twitter']['access_token_secret']

#autenticacion
auth = tweepy.OAuthHandler(api_key,api_key_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
    
# Usuario del que vamos a extraer los twetts
user = 'MinSaludCol'

# Setear usuario para api.search_tweets
query_user = 'from:MinSaludCol'

# Construir hashtags
keywords = ['#ReporteCOVID19', 'from:MinSaludCol']
q_keywords = ' '.join(keywords)

# Usuarios
users = []
query = ''.join(q_keywords)
keywords = '#ReporteCOVID19'
limit=100

#Cursor para obtener los tweets
tweets = tweepy.Cursor(api.search_tweets, q=query, count=limit, tweet_mode='extended').items(limit)


columns=['Date','User','Tweet']
data=[]

for tweet in tweets:
    data.append([tweet.created_at, tweet.user.screen_name, tweet.full_text])

df = pd.DataFrame(data, columns=columns)
print(df)

connection = pymysql.connect(

    host="localhost",
    user="root",
    password="sergio",
    db="bigdata"
)

cursor = connection.cursor()


for fecha,userTw,tweet  in data:
    listatweet = tweet.split()
    posicion = 0

    if listatweet[0] == '#ReporteCOVID19':
        for i in listatweet:
            if i == 'recuperados':
                posicion = listatweet.index(i) - 1
        
        listatweet[0:posicion] = []
        listanew = listatweet

        print(listanew)

        recuperados = listanew[0]
        nuevosCasos= listanew[2]
        fallecidos= listanew[5]
        muestras= listanew[8]
        pcr= listanew[10]
        antigeno= listanew[12]
        recuperadosTotal= listanew[14]
        casos= listanew[16]
        fallecidosTotal= listanew[18]
        muestrasProcesadas= listanew[20]
        activos= listanew[23]

        sql = "INSERT INTO tweets(fecha, usuario, recuperados,nuevosCasos,fallecidos,muestras,pcr,antigeno,totalRecuperados,totalCasos,totalFallecidos,totalMuestrasPorcesadas,totalActivos) VALUES ('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}','{9}','{10}','{11}','{12}')".format(fecha,userTw,recuperados,nuevosCasos,fallecidos,muestras,pcr,antigeno,recuperadosTotal,casos,fallecidosTotal,muestrasProcesadas,activos)
        cursor.execute(sql)
        connection.commit()
        addTweets(fecha,userTw,recuperados,nuevosCasos,fallecidos,muestras,pcr,antigeno,recuperadosTotal,casos,fallecidosTotal,muestrasProcesadas,activos)
        
        