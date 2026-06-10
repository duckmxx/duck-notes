import json

# note1 = {"title": "My first note", "content": "learning json parsing"}
file_path = "notes.json"

def read_json(file_path):
    with open(file_path, "r") as file:
        return json.load(file)

def display_json(file_path):
    notes = read_json(file_path)
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

while True:
    print("1. Read existing notes")
    print("2. Write a note")
    print("Q. Quit")
    choice = input("Please enter your choice: ")
    
    if choice == "1":
        display_json(file_path)
        print()
    elif choice == "2":
        title = input("What is the title?: ")
        content = input("What is the contents?: ")

        save_json(file_path, title, content)
        print()
    else: 
        break
