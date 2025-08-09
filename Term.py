from rich.console import Console
import datetime as dt
import random as r
import time
import glob
import ast
import os

notes_location = "Notes"
notes = glob.glob(f"{notes_location}/*.term")
current_heading = ""

class note():
    def __init__(self, content):
        self.content = content
        self.heading = f"[bold] {self.content["heading"]} [/bold]"
        self.date = self.content["date"]
        self.body = self.content["body"]
        self.id = f"[dim] {self.content["id"]} [/dim]"

    def print_this(self):
        Note = f"""+{"-"*20}+
{self.heading}
{self.date}
{self.body}
{self.id}
+{"-"*20}+
        """
        return Note

console = Console()

while True:
    console.clear()
    console.print("""[green]
░▀█▀░█▀▀░█▀▄░█▄█░░░░░
░░█░░█▀▀░█▀▄░█░█░░░░░
░░▀░░▀▀▀░▀░▀░▀░▀░░░▀░
    """)
    for note_ in notes:
        with open(f"{note_}", "r") as file:
            note_content = file.read()
            file.close()
        console.print(note(ast.literal_eval(note_content)).print_this())
    
    action = input("> ")
    action_mod = action.split()[0]
    current_heading = "".join(action.split()[1:])

    if action_mod == "+":
        console.clear()
        print("Body:")
        new_body = input("> ")
        new_note = {"heading": current_heading, "date": str(dt.datetime.now().strftime("%Y-%m-%d %H:%M")), "body": new_body, "id": r.randint(1000, 9999)}
        note(new_note)
        notes.append(f"{notes_location}/{current_heading}.term")
        with open(f"{notes_location}/{current_heading}.term", "w") as file:
            file.write(f"{new_note}")
            file.close()
        print(f'Note "{current_heading}" created!')
        time.sleep(1)
    elif action_mod == "-":
        try:
            os.system(f"rm {notes_location}/{current_heading}.term")
            notes.remove(f"{notes_location}/{current_heading}.term")
        except:
            console.print("Not Found!")
            time.sleep(0.5)
    elif action_mod == "=":
        console.clear()
        with open(f"{notes_location}/{current_heading}.term", "r") as file:
            read_note = file.read()
            file.close()
        print(f"Body: {ast.literal_eval(read_note)['body']}")
        new_body = input("> ")
        new_note = {"heading": current_heading, "date": str(dt.datetime.now().strftime("%Y-%m-%d %H:%M")), "body": new_body, "id": r.randint(1000, 9999)}
        note(new_note)
        with open(f"{notes_location}/{current_heading}.term", "w") as file:
            file.write(f"{new_note}")
            file.close()
        print(f'Note "{current_heading}" edited!')
        time.sleep(1)
    elif action_mod == "/":
        break
    
