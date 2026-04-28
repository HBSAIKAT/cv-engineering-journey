# A Case Study: Notebook Application

## Application Design

A simple command-line notebook application with two main object types:

1. **Note** — Individual note with memo, tags, creation date, and unique ID
2. **Notebook** — Container holding multiple notes with search and modify functionality

Other data (tags, dates) use Python's standard library and simple strings—no separate classes needed.

---

## Project Structure

```
parent_directory/
    notebook.py      # Note and Notebook classes
    menu.py          # Menu interface (executable)
    command_option.py # Placeholder for future command-line interface
```

**Design principle:** Keep the Notebook class separate from the interface. This allows future interfaces (GUI, web) to use the same Notebook objects.

---

## Class Design

### Note Class

**Attributes:**
- `memo` — The note content
- `tags` — Space-separated tags
- `creation_date` — Automatically set to today
- `id` — Unique integer ID (auto-generated)

**Methods:**
- `match(filter)` — Check if note matches a search string (case-sensitive, searches memo and tags)

### Notebook Class

**Attributes:**
- `notes` — List of Note objects

**Methods:**
- `new_note(memo, tags='')` — Create and add a new note
- `modify_memo(note_id, memo)` — Update note content
- `modify_tags(note_id, tags)` — Update note tags
- `search(filter)` — Return list of notes matching filter
- `_find_note(note_id)` — (Internal) Find note by ID

---

## Note Class Implementation

```python
import datetime

# Store the next available id for all new notes
last_id = 0

class Note:
    '''Represent a note in the notebook. Match against a
    string in searches and store tags for each note.'''
    
    def __init__(self, memo, tags=''):
        '''Initialize a note with memo and optional
        space-separated tags. Automatically set the note's
        creation date and a unique id.'''
        self.memo = memo
        self.tags = tags
        self.creation_date = datetime.date.today()
        global last_id
        last_id += 1
        self.id = last_id
    
    def match(self, filter):
        '''Determine if this note matches the filter
        text. Return True if it matches, False otherwise.
        Search is case sensitive and matches both text and
        tags.'''
        return filter in self.memo or filter in self.tags
```

**Key points:**
- Uses module-level `last_id` variable to auto-increment IDs
- Uses `global` keyword to modify module-level variable
- `match()` searches both memo and tags

---

## Notebook Class Implementation

```python
class Notebook:
    '''Represent a collection of notes that can be tagged,
    modified, and searched.'''
    
    def __init__(self):
        '''Initialize a notebook with an empty list.'''
        self.notes = []
    
    def new_note(self, memo, tags=''):
        '''Create a new note and add it to the list.'''
        self.notes.append(Note(memo, tags))
    
    def _find_note(self, note_id):
        '''Locate the note with the given id.'''
        for note in self.notes:
            if str(note.id) == str(note_id):
                return note
        return None
    
    def modify_memo(self, note_id, memo):
        '''Find the note with the given id and change its
        memo to the given value.'''
        note = self._find_note(note_id)
        if note:
            note.memo = memo
            return True
        return False
    
    def modify_tags(self, note_id, tags):
        '''Find the note with the given id and change its
        tags to the given value.'''
        note = self._find_note(note_id)
        if note:
            note.tags = tags
            return True
        return False
    
    def search(self, filter):
        '''Find all notes that match the given filter
        string.'''
        return [note for note in self.notes if note.match(filter)]
```

**Key points:**
- `_find_note()` is internal (single underscore) but accessible if needed
- String comparison in `_find_note()` handles both string and int IDs
- `modify_*` methods return `True`/`False` for success/failure
- `search()` uses list comprehension

---

## Menu Class Implementation

```python
import sys
from notebook import Notebook, Note

class Menu:
    '''Display a menu and respond to choices when run.'''
    
    def __init__(self):
        self.notebook = Notebook()
        self.choices = {
            "1": self.show_notes,
            "2": self.search_notes,
            "3": self.add_note,
            "4": self.modify_note,
            "5": self.quit
        }
    
    def display_menu(self):
        print("""
Notebook Menu
1. Show all Notes
2. Search Notes
3. Add Note
4. Modify Note
5. Quit
""")
    
    def run(self):
        '''Display the menu and respond to choices.'''
        while True:
            self.display_menu()
            choice = input("Enter an option: ")
            action = self.choices.get(choice)
            if action:
                action()
            else:
                print("{0} is not a valid choice".format(choice))
    
    def show_notes(self, notes=None):
        if not notes:
            notes = self.notebook.notes
        for note in notes:
            print("{0}: {1}\n{2}".format(note.id, note.tags, note.memo))
    
    def search_notes(self):
        filter = input("Search for: ")
        notes = self.notebook.search(filter)
        self.show_notes(notes)
    
    def add_note(self):
        memo = input("Enter a memo: ")
        self.notebook.new_note(memo)
        print("Your note has been added.")
    
    def modify_note(self):
        id = input("Enter a note id: ")
        memo = input("Enter a memo: ")
        tags = input("Enter tags: ")
        if memo:
            self.notebook.modify_memo(id, memo)
        if tags:
            self.notebook.modify_tags(id, tags)
    
    def quit(self):
        print("Thank you for using your notebook today.")
        sys.exit(0)

if __name__ == "__main__":
    Menu().run()
```

**Key points:**
- `choices` dictionary maps menu options to methods (lightweight command pattern)
- `action()` calls the method without parameters
- `show_notes()` has optional parameter for filtered display
- `__name__ == "__main__"` guard so notebook can be imported

---

## Design Patterns Used

### Command Pattern (Lightweight)

```python
self.choices = {
    "1": self.show_notes,
    "2": self.search_notes,
    "3": self.add_note,
    "4": self.modify_note,
    "5": self.quit
}

action = self.choices.get(choice)
if action:
    action()
```

Maps user input (strings) to method calls without `if/elif` chains.

---

## Bugs and Fixes

### Bug 1: String vs Integer ID

**Problem:** User enters ID as string "1", but note IDs are integers.

**Fix:** Convert both to strings before comparing:

```python
def _find_note(self, note_id):
    '''Locate the note with the given id.'''
    for note in self.notes:
        if str(note.id) == str(note_id):
            return note
    return None
```

### Bug 2: Invalid Note ID Crashes

**Problem:** If user enters non-existent ID, program crashes.

**Fix:** Check if note is found before modifying:

```python
def modify_memo(self, note_id, memo):
    '''Find the note with the given id and change its memo.'''
    note = self._find_note(note_id)
    if note:
        note.memo = memo
        return True
    return False
```

Return `True`/`False` so menu can display error message.

---

## Testing

### Test Note class

```python
>>> from notebook import Note
>>> n1 = Note("hello first")
>>> n2 = Note("hello again")
>>> n1.id
1
>>> n2.id
2
>>> n1.match('hello')
True
>>> n2.match('second')
False
```

### Test Notebook class

```python
>>> from notebook import Note, Notebook
>>> n = Notebook()
>>> n.new_note("hello world")
>>> n.new_note("hello again")
>>> n.notes[0].memo
'hello world'
>>> n.search("hello")
[<notebook.Note object at 0xb730a78c>, <notebook.Note object at 0xb73103ac>]
>>> n.search("world")
[<notebook.Note object at 0xb730a78c>]
>>> n.modify_memo(1, "hi world")
>>> n.notes[0].memo
'hi world'
```

---

## Design Principles Applied

✓ **Separation of concerns** — Notebook logic separate from menu interface  
✓ **Extensibility** — Menu can be replaced with CLI or GUI  
✓ **Single responsibility** — Each class has one clear purpose  
✓ **Don't trust user input** — Validate and handle errors  
✓ **Reusable methods** — `show_notes()` works for all/filtered notes  
✓ **Internal methods** — `_find_note()` marked as internal