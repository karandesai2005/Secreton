import json
import os
from datetime import datetime
import re
"""
--> so first we gonna make a simple cli where user can add notes and view notes
    -> decide a json structure in which notes is gonna store in json file
        - 
        { json format
  "notes": [
    {
      "id": 1,
      "title": "Idea: Secreton",
      "content": "A CLI vault to store notes securely and access via SSH.",
      "created_at": "2025-08-22 02:55:00"
    },
    {
      "id": 2,
      "title": "Feature list",
      "content": "Add, list, view, delete notes. Later: encryption + FastAPI.",
      "created_at": "2025-08-22 03:00:00"
    }
  ]
}
 
"""
import os
import json
from datetime import datetime

FILENAME = "notes.json"

def load_data():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as f:
            return json.load(f)
    else:
        return {"last_id": 0, "notes": []}

def save_data(data):
    with open(FILENAME, "w") as f:
        json.dump(data, f, indent=4)

def add():
    data = load_data()
    
    user_title = input("enter title of your note: ")
    print("enter content (type '::q' on a new line to finish):")

    lines = []
    while True:
        line = input()
        if line.strip() == "::q":
            break
        lines.append(line)

    user_content = "\n".join(lines)

    new_id = data["last_id"] + 1
    new_note = {
        "id": new_id,
        "title": user_title,
        "content": user_content,
        "created_at": str(datetime.now())
    }

    data["notes"].append(new_note)
    data["last_id"] = new_id
    save_data(data)

    print(f"\nnote added successfully with id {new_id}")

def list_notes():
    data = load_data()
    if not data["notes"]:
        print("No notes found.")
        return
    
    print("\nYour Notes:")
    for note in data["notes"]:
        print(f"[{note['id']}] {note['title']} (created: {note['created_at']})")

def delete_note():
    data = load_data()
    if not data["notes"]:
        print("No notes to delete.")
        return
    
    note_id = input("Enter the ID of the note to delete: ")
    try:
        note_id = int(note_id)
    except ValueError:
        print("Invalid ID.")
        return
    
    updated_notes = [note for note in data["notes"] if note["id"] != note_id]

    if len(updated_notes) == len(data["notes"]):
        print(f"No note found with ID {note_id}.")
        return

    data["notes"] = updated_notes
    save_data(data)
    print(f"Note with ID {note_id} deleted successfully.")

def view_note():
    data = load_data()
    if not data["notes"]:
        print("no notes available!!!")
        return
    note_id = input("enter the note_id u wanna view!!")
    try:
        note_id = int(note_id)
    except ValueError:
        print("Invalid note_id!!")
        return
        
    for note in data["notes"]:
        if note["id"] == note_id:
            print("\n--- Note ---")
            print(f"ID: {note['id']}")
            print(f"Title: {note['title']}")
            print(f"Created: {note['created_at']}")
            print("Content:\n")
            print(note["content"])
            return
    print(f"No note found with ID {note_id}.")


if __name__ == "__main__":
    while True:
        print("\n--- Secreton CLI ---")
        print("1. Add Note")
        print("2. List Notes")
        print("3. Delete Note")
        print("4. View Note")
        print("5. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            add()
        elif choice == "2":
            list_notes()
        elif choice == "3":
            delete_note()
        elif choice == "4":
            view_note()
        elif choice == "5":
            print("BBYEEE")
            break
        else:
            print("Invalid choice. Try again.")

