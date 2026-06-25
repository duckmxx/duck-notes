from flask import Flask, render_template, request, redirect
from notes import check_create_file, read_json, file_path, save_note, edit_note

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

@app.route("/note/<note_id>")
def view_note(note_id):
    notes = read_json(file_path)

    for note in notes:
        if note["id"] == note_id:
            return render_template("note.html", note=note)
        
    return "Note not found", 404


@app.route("/note/<note_id>/edit", methods=["POST"])
def edit_note_route(note_id):
    was_edited = edit_note(file_path, note_id, new_title=request.form["title"], new_content=request.form["content"])

    if not was_edited:
        return "Note not found", 404

    return redirect(f"/note/{note_id}")

if __name__ == "__main__":
    app.run()
