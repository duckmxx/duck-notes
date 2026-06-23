from flask import Flask, render_template
import json
from notes import check_create_file, read_json, file_path

app = Flask(__name__)

check_create_file(file_path)

notes_data = read_json(file_path)

@app.route("/")
def home():
    return render_template(
        "home.html",
        name="Yanny",
        notes = notes_data
    )

app.run()