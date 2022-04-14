from flask import Flask, render_template, request
import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["myflashcards"]
collection = db["set1"]

app = Flask(__name__)
i = 0


@app.route("/", methods=['GET', 'POST'])
def index():
    return render_template("index.html", upper="Hit NEXT to start")


@app.route("/edit", methods=['GET', 'POST'])
def edit():
    return render_template("edit.html")

@app.route("/submit_new", methods=['GET', 'POST'])
def submit_new():
    add = collection.insert_one(request.form.to_dict())
    return render_template("edit.html")


@app.route("/next", methods=['GET', 'POST'])
def next():
    card = list(collection.find())
    global i
    if i < (len(card)-1):
        i = i + 1
    elif i >= (len(card)-1):
        i=0
    return render_template("index.html", upper=card[i]['upper_card'], lower=card[i]['lower_card'])

@app.route("/previous", methods=['GET', 'POST'])
def previous():
    card = list(collection.find())
    global i
    if i <= 0:
        i=(len(card)-1)
    else:
        i = i-1
    return render_template("index.html", upper=card[i]['upper_card'], lower=card[i]['lower_card'])


if __name__ == '__main__':
    app.run(debug=True)
