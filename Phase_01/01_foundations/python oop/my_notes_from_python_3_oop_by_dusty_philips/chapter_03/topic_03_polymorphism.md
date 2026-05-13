# Polymorphism

## What is Polymorphism?

**Polymorphism** means "different behaviors happen depending on which subclass is being used, without having to explicitly know what the subclass actually is."

Different objects can respond to the same message (method call) in different ways.

---

## Example: Audio File Player

Imagine a media player that plays different audio formats.

### Without Polymorphism

```python
def play_audio(audio_file):
    if audio_file.type == "mp3":
        # Decompress MP3
        print("playing as mp3")
    elif audio_file.type == "wav":
        # Extract WAV
        print("playing as wav")
    elif audio_file.type == "ogg":
        # Decompress OGG
        print("playing as ogg")
    else:
        raise Exception("Unknown format")
```

**Problem:** Media player needs to know about every file type. Adding a new format requires changing the media player code.

### With Polymorphism

```python
# Media player code (simple and clean):
audio_file.play()
```

That's it! The specific file type handles its own decompression.

---

## Polymorphism with Inheritance

Each file type is a subclass with its own `play()` implementation:

```python
class AudioFile:
    def __init__(self, filename):
        if not filename.endswith(self.ext):
            raise Exception("Invalid file format")
        self.filename = filename

class MP3File(AudioFile):
    ext = "mp3"
    
    def play(self):
        print(f"playing {self.filename} as mp3")

class WavFile(AudioFile):
    ext = "wav"
    
    def play(self):
        print(f"playing {self.filename} as wav")

class OggFile(AudioFile):
    ext = "ogg"
    
    def play(self):
        print(f"playing {self.filename} as ogg")
```

### How It Works

```python
>>> ogg = OggFile("myfile.ogg")
>>> ogg.play()
playing myfile.ogg as ogg

>>> mp3 = MP3File("myfile.mp3")
>>> mp3.play()
playing myfile.mp3 as mp3

>>> not_an_mp3 = MP3File("myfile.ogg")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "polymorphic_audio.py", line 4, in __init__
    raise Exception("Invalid file format")
Exception: Invalid file format
```

### Polymorphic Magic

Notice how `AudioFile.__init__` accesses `self.ext` from the subclass, even though the parent class doesn't know which subclass is being used.

The media player just calls `play()` on any AudioFile, and the correct implementation runs automatically.

---

## Polymorphism in Python: Duck Typing

Python goes beyond traditional inheritance polymorphism. You don't need to inherit from a common parent to be polymorphic.

### Without Inheriting from AudioFile

```python
class FlacFile:
    def __init__(self, filename):
        if not filename.endswith(".flac"):
            raise Exception("Invalid file format")
        self.filename = filename
    
    def play(self):
        print(f"playing {self.filename} as flac")
```

**No inheritance from AudioFile!**

### It Works Anyway

```python
# Media player code works with any object that has a play() method:
audio_file.play()
```

This works whether `audio_file` is an `MP3File`, `WavFile`, `FlacFile`, or any other object with a `play()` method.

**This is duck typing:** "If it walks like a duck and quacks like a duck, it's a duck."

---

## Duck Typing Reduces Need for Inheritance

Because Python's duck typing allows any object with the right interface to work, you can:

1. **Skip creating a common superclass** — Not all file types need to inherit from AudioFile
2. **Reduce multiple inheritance** — When one interface is needed, duck typing often works
3. **Add new types easily** — Just create a class with the required methods

### Benefits

- **Flexibility** — New types don't need to know about or inherit from existing code
- **Decoupling** — Objects are independent; they just need to provide the interface
- **Simplicity** — Less inheritance hierarchy to maintain

---

## Important: Interface Must Make Sense

Just because an object has the right method **doesn't mean it will work correctly.**

### Bad Example

```python
class ChessAI:
    def play(self):
        print("moving chess piece")
```

`ChessAI` has a `play()` method, but it's not an audio file!

```python
audio_player = ChessAI()
audio_player.play()  # Prints "moving chess piece"—NOT playing audio!
```

**Lesson:** An object must fulfill the interface in a way that **makes sense for the system**, not just provide the right method names.

---

## Duck Typing: Only Implement What's Used

You don't need to implement the entire interface of an object—just the methods that are **actually accessed**.

### Example: File-like Object

If code only reads from a file (doesn't write), create a minimal object:

```python
class FakeFile:
    def read(self):
        return "fake file content"
    
    # Don't need write() if code never calls it!
```

### Full File Interface (All Methods)

```python
class RealFile:
    def read(self):
        pass
    
    def write(self, data):
        pass
    
    def close(self):
        pass
    
    def seek(self, position):
        pass
```

### Duck Typing Advantage

- `FakeFile` works fine with read-only code
- No need to implement methods that won't be called
- Simpler, less code

---

## Polymorphism with Multiple Methods

An interface can include multiple methods and attributes:

```python
class MediaPlayer:
    def play(self, audio_file):
        audio_file.play()
    
    def get_duration(self, audio_file):
        return audio_file.duration
    
    def get_title(self, audio_file):
        return audio_file.title
```

For this interface, objects need:
- `play()` method
- `duration` attribute
- `title` attribute

### Satisfying the Interface

```python
class MP3File:
    def __init__(self, filename):
        self.filename = filename
        self.title = filename
        self.duration = 180  # seconds
    
    def play(self):
        print(f"playing {self.filename} as mp3")

# Works with MediaPlayer!
player = MediaPlayer()
mp3 = MP3File("song.mp3")
player.play(mp3)
player.get_duration(mp3)  # Returns 180
```

---

## Polymorphism Benefits

✓ **Code reuse** — Media player code works with any audio format  
✓ **Extensibility** — Add new formats without changing existing code  
✓ **Encapsulation** — Details of playing different formats are hidden  
✓ **Flexibility** — Duck typing means inheritance is optional  
✓ **Simplicity** — Cleaner code without type checking

---

## Polymorphism vs Duck Typing

| Aspect | Polymorphism | Duck Typing |
|--------|--------------|------------|
| **Requires inheritance?** | Traditional: Yes | Python: No |
| **Common superclass needed?** | Yes | No |
| **When methods are called** | Runtime dispatches to correct subclass | Runtime calls whatever method exists |
| **Interface definition** | Explicit (parent class) | Implicit (methods used) |
| **Flexibility** | Good | Better |

---

## Complete Audio Player Example

```python
class AudioFile:
    """Base class with validation."""
    def __init__(self, filename):
        if not filename.endswith(self.ext):
            raise Exception("Invalid file format")
        self.filename = filename

class MP3File(AudioFile):
    ext = "mp3"
    def play(self):
        print(f"playing {self.filename} as mp3")

class WavFile(AudioFile):
    ext = "wav"
    def play(self):
        print(f"playing {self.filename} as wav")

class OggFile(AudioFile):
    ext = "ogg"
    def play(self):
        print(f"playing {self.filename} as ogg")

class FlacFile:
    """Doesn't inherit from AudioFile—duck typing!"""
    def __init__(self, filename):
        if not filename.endswith(".flac"):
            raise Exception("Invalid file format")
        self.filename = filename
    
    def play(self):
        print(f"playing {self.filename} as flac")

# Media player code—works with all formats
def play_files(files):
    for audio_file in files:
        audio_file.play()

# Usage:
files = [
    MP3File("song.mp3"),
    WavFile("audio.wav"),
    OggFile("music.ogg"),
    FlacFile("lossless.flac")
]

play_files(files)
# Output:
# playing song.mp3 as mp3
# playing audio.wav as wav
# playing music.ogg as ogg
# playing lossless.flac as flac
```

One function plays all formats!

---

## Key Rules

✓ Polymorphism lets different subclasses respond to the same message differently  
✓ Use inheritance when classes share code and semantic meaning  
✓ Use duck typing when you just need an interface (Python's way)  
✓ Objects must fulfill the interface **meaningfully**, not just provide the method names  
✓ Only implement methods and attributes that are actually **used**  
✓ Polymorphic code is simpler and more extensible  
✓ One function can work with many different types  
✓ Media player example: `audio_file.play()` works for any audio format