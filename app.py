from flask import Flask, request, render_template
from stories import Story

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/story")
def story():
    place = request.args.get("place")
    noun = request.args.get("noun")
    verb = request.args.get("verb")
    adjective = request.args.get("adjective")
    plural_noun = request.args.get("plural_noun")
    return render_template("story.html", place=place, noun=noun, verb=verb, adjective=adjective, plural_noun=plural_noun)