from flask import Flask
import json

app = Flask(__name__)

def read_json(file_path):
    with open(file_path, "r") as file:
        return json.load(file)


@app.route("/notes")
def notes():
    notes = read_json("notes.json")

    html = "<h1>My Notes</h1>"

    html += "<hr>"
    for note in notes:
        html += f"<h2>{note['title']}</h2>"
        html += f"<p>{note['content']}</p>"
        html += "<hr>"


    return html

app.run()