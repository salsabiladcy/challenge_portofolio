import os
from os.path import join, dirname
from dotenv import load_dotenv
from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

MONGODB_URL = os.environ.get("MONGODB_URI")
DB_NAME =  os.environ.get("DB_NAME")

client = MongoClient(MONGODB_URL)
db = client[DB_NAME]

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/#contact", methods=["POST"])
def contactme_post():
    name_receive = request.form['name_give']
    email_receive = request.form['email_give']
    pesan_receive = request.form['pesan_give']
    doc = {
        'Nama Lengkap' : name_receive,
        'Email' : email_receive,
        'Pesan' : pesan_receive
    }
    db.contact.insert_one(doc)
    return jsonify({'msg': 'Data Saved!'})

if __name__ == '__main__':
    app.run(port=5000, debug=True)