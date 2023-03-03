from flask import Flask, render_template
import os
from pymongo import MongoClient

app = Flask(__name__, template_folder="templates")

client=MongoClient("mongodb://mongodb:27017/")
db = client["vetements"]
collection = db["marques"]

@app.route("/")
def index():
    datas = collection.find()
    return render_template("template_database.html", objets=datas)

@app.route('/file')
def display_text():
    file_path = os.path.join('/data','file.txt')
    with open(file_path, 'r') as file:
        text = file.read()
    return render_template("template_txt.html", file=text)

if __name__ == "__main__":
    # Start the Flask application, listening on all available interfaces
    app.run(host="0.0.0.0")

