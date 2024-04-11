class Note:

    def __init__(self, title, text):
        self.title = title
        self.text = text

class Notebook:

    def __init__(self):
        self.notebook = []

    def add_note(self, note):
        if note not in self.notebook:
            self.notebook.append(note)
        else:
            return "Такая запись уже есть"

    def show_note(self, note):
        if note in self.notebook:
           return [i.title for i in self.notebook if i == note]
        else:
            return "Такой записи не существует"
        
    def delete_note(self, note):
        if note in self.notebook:
            self.notebook.remove(note)
        else:
            return "Такая запись не существует"
        
x = Note("hello", "hello")
z = Note("Bye", "Bye")
y = Notebook()
y.add_note(x)
y.add_note(z)
print(y.show_note(x))
print(y.show_note(z))