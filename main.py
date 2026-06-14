import json
import os

file_path = "notes.json"

def check_create_file(file_path):
    if not os.path.exists(file_path):
        with open(file_path, "w") as file:
            json.dump([], file)
    try:
        read_json(file_path)
    except json.decoder.JSONDecodeError:
        with open(file_path, "w") as file:
            json.dump([], file)

def read_json(file_path):
    with open(file_path, "r") as file:
        return json.load(file)

def display_json(file_path):
    notes = read_json(file_path)
    if not notes:               # Empty list evaluates to falsy
        print("Wow, so empty.")
        return
    for index, note in enumerate(notes):
        print(f"Notes entry number {index + 1}.")
        print(f"Title: {note['title']}")
        print(f"Contents: {note['content']}")
        print("--------------------------")

def save_json(file_path, title, content):
    notes = read_json(file_path)
    notes.append({"title": title, "content": content})
    
    with open(file_path, "w") as file:
        json.dump(notes, file, indent=2)


def delete_note(file_path, note_index):
    notes = read_json(file_path)
    if not notes:
        print("Wow, can't delete nothing can you")
        return
    else:
        note_to_delete = notes[note_index - 1]
        print(f'Deleting note "{note_to_delete["title"]}"')
        notes.pop(note_index - 1)
        with open(file_path, "w") as file:
            json.dump(notes, file, indent=2)
        

check_create_file(file_path)

while True:
    print("1. Read existing notes")
    print("2. Write a note")
    print("3. Delete note")
    print("Q. Quit")
    choice = input("Please enter your choice: ")
    
    match choice.lower():
        case "1":
            display_json(file_path)
            print()
        case "2":
            title = input("What is the title?: ")
            content = input("What is the contents?: ")
            save_json(file_path, title, content)
        case "3":
            note_index = int(input("What note would you like to delete?: "))
            delete_note(file_path, note_index)
        case "q":
            break
        case _:
            print("Invalid choice.")