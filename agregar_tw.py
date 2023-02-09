from flask import Flask, render_template, jsonify, Response
import database as dbase
from tweet import Tweet

app = Flask(__name__)
db = dbase.dbConection()

@app.route('/tweet')
def addTweets(fecha, usuario, recuperados,nuevosCasos,fallecidos,muestras,pcr,antigeno,totalRecuperados,totalCasos,totalFallecidos,totalMuestrasPorcesadas,totalActivos):
    tweets = db['tweets']
    fechaTweet = fecha
    usua = usuario
    recupera = recuperados
    nuevosCas = nuevosCasos
    falleci = fallecidos
    muest = muestras
    pc = pcr
    antige = antigeno
    totalRecuper = totalRecuperados
    totalCa = totalCasos
    totalFalle = totalFallecidos
    totalMuestrasPorc = totalMuestrasPorcesadas
    totalActi = totalActivos

    tweet = Tweet(fechaTweet,usua,recupera,nuevosCas,falleci,muest,pc,antige,totalRecuper,totalCa,totalFalle,totalMuestrasPorc,totalActi)
    tweets.insert_one(tweet.toDBColecction())

    response = jsonify({
        'fecha':fechaTweet,
        'usuario':usua
    })
