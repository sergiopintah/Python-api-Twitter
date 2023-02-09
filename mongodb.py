from flask import Flask, render_template, jsonify, Response
import database as dbase
import twitter_api as tw_api

app = Flask(__name__)
db = dbase.dbConection()

#RUTAS DE LA APLICACION
@app.route('/')
def home():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True, port=4000)