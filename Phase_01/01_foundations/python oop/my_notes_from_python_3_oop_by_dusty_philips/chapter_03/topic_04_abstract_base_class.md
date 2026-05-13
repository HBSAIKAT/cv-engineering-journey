# Abstract Base Classes

## What Are Abstract Base Classes?

**Abstract Base Classes (ABCs)** define a set of methods and properties that a class must implement to be considered a proper instance of that class.

ABCs provide a formal way to document and enforce interfaces, especially when working with third-party plugins or libraries.

---

## Using Existing ABCs

Most ABCs in Python's Standard Library live in the `collections` module.

### Example: Container ABC

The `Container` ABC requires one method: `__contains__`

```python
>>> from collections import Container
>>> Container.__abstractmethods__
frozenset(['__contains__'])
```

This method checks if a value is in a container (like `in` keyword does).

### Implementing Container

```python
class OddContainer:
    def __contains__(self, x):
        if not isinstance(x, int) or not x % 2:
            return False
        return True
```

**No inheritance needed!** Just implement `__contains__`.

### Duck Typing Without Inheritance

```python
>>> odd_container = OddContainer()
>>> isinstance(odd_container, Container)
True
>>> issubclass(OddContainer, Container)
True
```

Even though `OddContainer` doesn't inherit from `Container`, Python recognizes it as a Container because it implements the required method.

### Using the in Keyword

Any class with `__contains__` automatically supports the `in` keyword:

```python
>>> 1 in odd_container
True
>>> 2 in odd_container
False
>>> 3 in odd_container
True
>>> "a string" in odd_container
False
```

---

## Why Use ABCs?

1. **Documentation** — Clear contract of what methods are required
2. **Validation** — Python prevents instantiation of incomplete implementations
3. **Type checking** — Use `isinstance()` and `issubclass()` to verify interface compliance
4. **Third-party plugins** — Ensure plugins implement required methods

---

## Creating Your Own ABC

Use the `abc` module to create custom abstract base classes:

```python
import abc

class MediaLoader(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def play(self):
        pass
    
    @abc.abstractproperty
    def ext(self):
        pass
    
    @classmethod
    def __subclasshook__(cls, C):
        if cls is MediaLoader:
            attrs = set(dir(C))
            if set(cls.__abstractmethods__) <= attrs:
                return True
            return NotImplemented
```

**Key syntax:**
- `metaclass=abc.ABCMeta` — Gives class ABC powers
- `@abc.abstractmethod` — Method must be implemented
- `@abc.abstractproperty` — Property must be implemented
- `@classmethod` — Method called on class, not instance
- `__subclasshook__` — Allows duck-typed classes to be recognized as subclasses

---

## Implementing an ABC

### Incomplete Implementation (Fails)

```python
class Wav(MediaLoader):
    pass

>>> x = Wav()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: Can't instantiate abstract class Wav with abstract methods ext, play
```

**Error:** Wav doesn't implement required `ext` and `play`.

### Complete Implementation (Works)

```python
class Ogg(MediaLoader):
    ext = '.ogg'
    
    def play(self):
        print("playing ogg file")

>>> o = Ogg()
>>> o.play()
playing ogg file
```

**Success:** Ogg implements both required `ext` and `play`.

---

## ABC Without Inheritance

The `__subclasshook__` method allows duck-typed classes to be recognized as ABC instances **without inheriting**:

```python
class Ogg:
    ext = '.ogg'
    
    def play(self):
        print("this will play an ogg file")

>>> issubclass(Ogg, MediaLoader)
True
>>> isinstance(Ogg(), MediaLoader)
True
```

Even though `Ogg` doesn't inherit from `MediaLoader`, it's recognized as a `MediaLoader` because it implements the required interface!

---

## Understanding __subclasshook__

### What It Does

The `__subclasshook__` method answers: "Is class C a subclass of this ABC?"

### Line-by-Line Breakdown

```python
@classmethod
def __subclasshook__(cls, C):
```

- `@classmethod` — Can be called on class instead of instance
- `cls` — The ABC class itself (MediaLoader)
- `C` — The candidate class to check

```python
if cls is MediaLoader:
```

Check if this hook is for MediaLoader (not a subclass of it). Prevents false matches.

```python
attrs = set(dir(C))
```

Get all methods and properties of candidate class C (including inherited ones).

```python
if set(cls.__abstractmethods__) <= attrs:
```

**Set notation:** Check if all abstract methods are in the candidate class's attributes. (`<=` means "is subset of")

```python
return True
```

If all abstract methods exist, the class is a valid subclass.

```python
return NotImplemented
```

If conditions aren't met, return `NotImplemented` to use default subclass detection (did C explicitly inherit from cls?).

---

## Common ABCs in collections Module

| ABC | Required Methods | Example |
|-----|-----------------|---------|
| `Container` | `__contains__` | Check if item is in container |
| `Iterable` | `__iter__` | Can loop through items |
| `Iterator` | `__next__`, `__iter__` | Can iterate with next() |
| `Sized` | `__len__` | Has a length |
| `Sequence` | `__getitem__`, `__len__` | Supports indexing and length |
| `Set` | All set operations | Supports union, intersection, etc. |
| `Mapping` | `__getitem__`, `__iter__`, `__len__` | Dict-like access |

---

## Real-World Example: Plugin System

```python
import abc

class Plugin(metaclass=abc.ABCMeta):
    """Base class for all plugins."""
    
    @abc.abstractmethod
    def load(self):
        """Load plugin data."""
        pass
    
    @abc.abstractmethod
    def run(self):
        """Execute plugin."""
        pass
    
    @abc.abstractproperty
    def name(self):
        """Plugin name."""
        pass

# Third-party plugin (no inheritance needed)
class DataProcessorPlugin:
    name = "DataProcessor"
    
    def load(self):
        print("Loading data processor")
    
    def run(self):
        print("Running data processor")

# Verify it's a valid plugin
>>> isinstance(DataProcessorPlugin(), Plugin)
True

# Use it like any plugin
>>> plugin = DataProcessorPlugin()
>>> plugin.load()
Loading data processor
>>> plugin.run()
Running data processor
```

---

## ABC vs Duck Typing

| Aspect | Duck Typing | ABC |
|--------|------------|-----|
| **Requires inheritance?** | No | No (with `__subclasshook__`) |
| **Enforces interface?** | No | Yes (at instantiation) |
| **Documentation** | Implicit | Explicit |
| **Error checking** | Runtime when method called | Instantiation fails |
| **Third-party plugins** | Works but risky | Recommended |

---

## When to Use ABCs

**Use ABCs when:**
- Creating a plugin system
- Designing a library for third-party use
- Want to enforce a contract on subclasses
- Need explicit documentation of required methods

**Skip ABCs if:**
- Small, internal code
- Duck typing works fine
- Don't need strict validation

---

## Important Notes

1. **Don't need to inherit from ABC** — Implement all abstract methods and `__subclasshook__` recognizes your class

2. **Abstract methods can have implementation** — Subclasses call `super()` to reuse parent implementation

3. **Can still be abstract** — A subclass can implement some abstract methods but remain abstract itself

---

## Complete Plugin System Example

```python
import abc

class AudioPlugin(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def load(self, filename):
        pass
    
    @abc.abstractmethod
    def play(self):
        pass
    
    @abc.abstractproperty
    def format(self):
        pass
    
    @classmethod
    def __subclasshook__(cls, C):
        if cls is AudioPlugin:
            attrs = set(dir(C))
            if set(cls.__abstractmethods__) <= attrs:
                return True
        return NotImplemented

# MP3 Plugin (no inheritance, duck typing)
class MP3Plugin:
    format = "MP3"
    
    def load(self, filename):
        print(f"Loading {filename}")
    
    def play(self):
        print("Playing MP3")

# FLAC Plugin (no inheritance, duck typing)
class FLACPlugin:
    format = "FLAC"
    
    def load(self, filename):
        print(f"Loading {filename}")
    
    def play(self):
        print("Playing FLAC")

# Test
>>> mp3 = MP3Plugin()
>>> isinstance(mp3, AudioPlugin)
True
>>> issubclass(MP3Plugin, AudioPlugin)
True

def play_audio(plugin):
    """Works with any AudioPlugin."""
    plugin.load("song.mp3")
    plugin.play()

play_audio(MP3Plugin())  # Works!
play_audio(FLACPlugin()) # Works!
```

---

## Key Rules

✓ ABCs define required methods and properties  
✓ Classes must implement all abstract methods to instantiate  
✓ `@abc.abstractmethod` marks required methods  
✓ `@abc.abstractproperty` marks required properties  
✓ `__subclasshook__` allows duck-typed classes to be recognized  
✓ No inheritance needed if `__subclasshook__` is implemented  
✓ Use ABCs for plugin systems and third-party code  
✓ ABCs provide documentation and validation  
✓ Python recognizes duck-typed ABC implementations automatically