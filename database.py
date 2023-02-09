import pymongo
import certifi


conn_str = "mongodb+srv://sergio:sergio@cluster0.cojbztx.mongodb.net/?retryWrites=true&w=majority"
ca = certifi.where()

def dbConection():

    try:
        client = pymongo.MongoClient(conn_str, serverSelectionTimeoutMS=5000)
        db = client["dbb_tweets"]
    except ConnectionError:
        print("Unable to connect to the server.")
    return db



