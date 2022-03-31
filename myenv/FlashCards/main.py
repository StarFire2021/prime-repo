from flask import Flask, render_template, request
import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["myflashcards"]
collection = db["set1"]

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def index():
    return render_template("index.html")


@app.route("/edit", methods=['GET', 'POST'])
def edit_cards():
    add = collection.insert_one(request.form.to_dict())
    return render_template("edit.html")


@app.route("/next", methods=['GET', 'POST'])
def next():
    n = 0
    if request.method == "POST":
        card = list(collection.find())
        if n == len(card):
            n = 0
            return render_template("index.html", upper=card[n])
        else:
            n = n+1
            return render_template("index.html", upper=card[n])
    else:
        return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)
