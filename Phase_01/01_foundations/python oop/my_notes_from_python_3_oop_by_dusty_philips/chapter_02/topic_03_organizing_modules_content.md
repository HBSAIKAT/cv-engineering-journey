# Organizing Module Contents

## Module-Level Variables

We can define variables at the module level to store global state without namespace conflicts.

**Example:** Instead of instantiating a `Database` class in each module, create one globally in the database module:

```python
class Database:
    # the database implementation
    pass

database = Database()
```

Then import and use it:

```python
from ecommerce.database import database
```

---

## Problem: Immediate Execution

Module-level code is executed **immediately when the module is imported**, not when functions are called.

**Issue:** Database connection might take time at startup, or connection info might not be available yet.

**Solution:** Use a function to delay creation:

```python
class Database:
    # the database implementation
    pass

database = None

def initialize_database():
    global database
    database = Database()
```

### The `global` Keyword

```python
def initialize_database():
    global database
    database = Database()
```

The `global` keyword tells Python that `database` inside the function refers to the module-level variable, not a new local variable.

**Without `global`:** Python creates a new local variable that is discarded when the function exits.

---

## Important Distinction

| Code Location | When Executed |
|---------------|---------------|
| Module level (outside functions) | Immediately on import |
| Inside a function | Only when the function is called |

**Example:**

```python
print("This runs on import")  # Runs immediately

def my_function():
    print("This runs on call")  # Only when called

my_function()  # Now the print statement runs
```

---

## The `if __name__ == "__main__":` Guard

**Problem:** If we write a module with startup code and later want to import a function from it in another script, the startup code runs automatically. This can cause unwanted side effects.

**Solution:** Wrap startup code in a `main()` function and only call it when the module is run directly:

```python
class UsefulClass:
    '''This class might be useful to other modules.'''
    pass

def main():
    '''Creates a useful class and does something with it.'''
    useful = UsefulClass()
    print(useful)

if __name__ == "__main__":
    main()
```

### How It Works

- `__name__` is a special variable in every module
- When a module is **executed directly** with `python module.py`: `__name__ == "__main__"`
- When a module is **imported**: `__name__` is the module's name (not `"__main__"`)

**Example:**

```python
# Run directly
python my_module.py
# __name__ is "__main__" → if block executes → main() runs

# Import in another file
from my_module import UsefulClass
# __name__ is "my_module" → if block does NOT execute
```

**Best practice:** Always use this guard in scripts, just in case we want to import from them later.

---

## Classes Defined Inside Functions

Classes can be defined anywhere, including inside functions:

```python
def format_string(string, formatter=None):
    '''Format a string using the formatter object.'''
    
    class DefaultFormatter:
        '''Format a string in title case.'''
        def format(self, string):
            return str(string).title()
    
    if not formatter:
        formatter = DefaultFormatter()
    return formatter.format(string)

hello_string = "hello world, how are you today?"
print("input: " + hello_string)
print("output: " + format_string(hello_string))
```

**Output:**
```
input: hello world, how are you today?
output: Hello World, How Are You Today?
```

### Scope

- The inner class `DefaultFormatter` is **local to the function**
- It **cannot be accessed** from outside the function
- It **only exists when the function is called**

---

## Inner Functions

Functions can also be defined inside other functions:

```python
def outer():
    def inner():
        print("I'm inside a function")
    inner()  # Call it here

outer()  # Call the outer function
```

---

## When to Use Inner Classes and Functions

**Use inner classes/functions for:**
- One-off items that don't need module-level scope
- Logic that only makes sense inside a single function
- Encapsulation (hiding implementation details)

**Note:** This technique is occasionally useful but not commonly seen in typical Python code.

---

## Code Organization Hierarchy

In order from smallest to largest scope:

```
Function/Method
    ↓
Class (typically at module level)
    ↓
Module (Python file)
    ↓
Package (folder with __init__.py)
```

---

## Quick Summary

| Concept | Where | When Executed |
|---------|-------|---------------|
| Module-level code | Outside functions | On import |
| Function code | Inside function `def:` | When called |
| `__name__ == "__main__"` | Module guard | Only when run directly |
| Inner classes | Inside functions | Only when function is called |
| `global` keyword | In functions | Refers to module-level variable |

---

## Key Rules

✓ Put startup code in a `main()` function  
✓ Use `if __name__ == "__main__":` to guard startup code  
✓ Use `global` keyword to modify module-level variables in functions  
✓ Inner classes/functions are scoped to their container  
✓ Module-level code runs on import; function code only on call