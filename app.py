from flask import Flask, render_template, request, redirect
from notes import check_create_file, read_json, file_path, save_note

app = Flask(__name__)

check_create_file(file_path)


@app.route("/")
def home():
    return render_template(
        "home.html",
        name="Yanny",
        notes = read_json(file_path)
    )

@app.route("/add", methods=["POST"])
def add_note_route():
    print(request.form)
    title = request.form["title"]
    content = request.form["content"]

    save_note(file_path, title, content)
    return redirect("/")  

if __name__ == "__main__":
    app.run()
