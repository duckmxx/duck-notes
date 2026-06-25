import json
import os
import uuid

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



def write_json(notes, file_path):
    with open(file_path, "w") as file:
        json.dump(notes, file, indent=2)

def read_json(file_path):
    with open(file_path, "r") as file:
        return json.load(file)

def display_json(file_path):
    notes = read_json(file_path)
    if not notes:               # Empty list evaluates to falsy
        print("Wow, so empty.\n")
        return
    for index, note in enumerate(notes):
        print(f"Notes entry number {index + 1}.")
        print(f"UUID: {note['id']}")
        print(f"Title: {note['title']}")
        print(f"Contents: {note['content']}")
        print("--------------------------")

def create_empty_note(file_path):
    notes = read_json(file_path)
    note = {
        "id": str(uuid.uuid4()),
        "title": "",
        "content": ""
    }

    notes.append(note)
    write_json(notes, file_path)
    print(f"Note {note['id']} appended.")
    return note

def edit_note(file_path, note_id, new_title=None, new_content=None):
    notes = read_json(file_path)

    for note in notes:
        if note["id"] == note_id:
            
            changed_fields=[]
            
            if new_title is not None and new_title != note["title"]:
                note["title"] = new_title
                changed_fields.append("title")
            if new_content is not None and new_content != note["content"]:
                note["content"] = new_content
                changed_fields.append("content")
            write_json(notes, file_path)
            print(f"Edited note: {note_id}: {', '.join(changed_fields) if changed_fields else 'no changes'}")
            
            return True

    print(f"Edit failed: note not found {note_id}")

    return False


def delete_note(file_path, note_id):
    notes = read_json(file_path)
    
    for index, note in enumerate(notes):
        if note["id"] == note_id:
            deleted_note = notes.pop(index)
            write_json(notes, file_path)
            print(f"Deleted note: {note['id']}")
            
            return deleted_note

            

def delete_empty_notes(file_path):
    notes = read_json(file_path)

    kept_notes = []
    deleted_count = 0

    for note in notes:
        title = note["title"].strip()
        content = note["title"].strip()

        if title or content:
            kept_notes.append(note)
        else:
            deleted_count += 1
            print(f"Deleted empty note: {note['id']}")
        
    if deleted_count > 0:
        write_json(kept_notes, file_path)
        print(f"Cleanup finished: removed {deleted_count} empty note(s)")
    else:
        print("No empty notes found")




        


def main():
    check_create_file(file_path)

    while True:
        print("1. Read existing notes")
        print("2. Write a note")
        print("3. Edit note")
        print("4. Delete note")
        print("Q. Quit")
        choice = input("Please enter your choice: ")
        
        match choice.lower():
            case "1":
                display_json(file_path)
                print()
            case "2":
                title = input("What is the title?: ")
                content = input("What is the contents?: ")
                save_note(file_path, title, content)
            case "3":
                display_json(file_path)
                try:
                    note_index = int(input("What note would you like to edit?: "))
                except ValueError:
                    print("Please enter a valid number.\n")
                    continue
                print("1. Edit title")
                print("2. Edit contents")
                edit_choice = input("Choice: ")
                if edit_choice == "1":
                    new_title = input("New title: ")
                    edit_note(file_path, note_index, new_title=new_title)
                elif edit_choice == "2":
                    new_content = input("New content: ")
                    edit_note(file_path, note_index, new_content=new_content)
                else:
                    print("Invalid input.\n")
            case "4":
                display_json(file_path)
                try:
                    note_index = int(input("What note would you like to delete?: "))
                    delete_note(file_path, note_index)
                except ValueError:
                    print("Please enter a valid number.\n")
            case "q":
                break
            case _:
                print("Invalid input.\n")


if __name__ == "__main__":
    main()