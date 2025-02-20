from datetime import datetime

class Note:
    HIGH: str = "HIGH"
    MEDIUM: str = "MEDIUM"
    LOW: str = "LOW"

    def __init__(self, code: str, title: str, text: str, importance: str):
        self.code: str = code
        self.title: str = title
        self.text: str = text
        self.importance: str = importance
        self.creation_date: datetime = datetime.now()
        self.tags: list[str] = []


    def add_tag(self, tag: str):
        if tag not in self.tags:
            self.tags.append(tag)

    def __str__(self)-> str:
        return f"Date: {self.creation_date}\n {self.title}: {self.text}"

class Notebook:
    def __init__(self):
        self.notes: list[Note] = []

    def add_note(self, title: str, text: str, importance: str)-> int:
        note_code: int = len(self.notes) + 1

        for note in self.notes:
            if note.code == str(note_code):
                note_code += 1

        note = Note(str(note_code), title, text, importance)
        self.notes.append(note)
        return note_code

    def delete_note(self, note_code: int):
        for note in self.notes:
            if note.code == str(note_code):
                self.notes.remove(note)
                break


def important_notes(selfself) -> list[Note]:
    resulting_notes: list[Note] = []
    for note in self.notes:
        if note.importance == Note.HIGH or Note.MEDIUM:
            resulting_notes.append(note)
    return resulting_notes


