# Creating Python Classes

## The Simplest Class

```python
class MyFirstClass:
    pass
```

That's it! A working class. Now you can create objects from it:

```python
a = MyFirstClass()  # Create object 'a'
b = MyFirstClass()  # Create object 'b'
print(a)  # <__main__.MyFirstClass object at 0xb7b7faec>
```

Each object is **distinct**—different memory addresses, different instances.

---

## Naming Classes

Follow these rules:
- Start with a **capital letter** (CamelCase)
- Use letters, numbers, and underscores only
- Example: `MyClass`, `Point`, `BankAccount` ✓

---

## Adding Attributes

Assign data to objects using **dot notation**:

```python
class Point:
    pass

p1 = Point()
p1.x = 5    # Add attribute x
p1.y = 4    # Add attribute y

p2 = Point()
p2.x = 3
p2.y = 6

print(p1.x, p1.y)  # Output: 5 4
print(p2.x, p2.y)  # Output: 3 6
```

We can assign **any** value: numbers, strings, other objects, even functions.

---

## Adding Methods (Behaviors)

Methods are functions inside a class. They let objects **do things**.

```python
class Point:
    def reset(self):
        self.x = 0
        self.y = 0

p = Point()
p.reset()
print(p.x, p.y)  # Output: 0 0
```

### The `self` Parameter

**Every method must have `self` as the first parameter.**

- `self` = a reference to the object the method is called on
- Python automatically passes it—we don't include it when calling the method
- it—we can call it anything, but `self` is the universal convention

```python
p = Point()

# These do the same thing:
p.reset()           # Normal way (self passed automatically)
Point.reset(p)      # Explicit way (pass object as self)
```

**Forget `self`? Python will complain:**
```
TypeError: reset() takes no arguments (1 given)
```

---

## Methods with Arguments

Pass extra parameters after `self`:

```python
import math

class Point:
    def move(self, x, y):
        """Move point to coordinates x, y"""
        self.x = x
        self.y = y
    
    def reset(self):
        """Reset to origin (0, 0)"""
        self.move(0, 0)  # Reuse move() method
    
    def calculate_distance(self, other_point):
        """Calculate distance to another point"""
        return math.sqrt(
            (self.x - other_point.x)**2 + 
            (self.y - other_point.y)**2
        )

# Usage:
p1 = Point()
p2 = Point()
p1.move(3, 4)
p2.move(0, 0)
print(p1.calculate_distance(p2))  # Output: 5.0
```

Call methods with arguments using dot notation: `object.method(arg1, arg2)`

---

## Initialization with `__init__`

**Problem:** Objects need initial data. If you forget to set `x` or `y`, you get errors.

**Solution:** Use `__init__()` (initialization method) to set up data when the object is created.

```python
class Point:
    def __init__(self, x, y):
        self.move(x, y)
    
    def move(self, x, y):
        self.x = x
        self.y = y

point = Point(3, 5)  # Must provide x and y
print(point.x, point.y)  # Output: 3 5
```

`__init__` runs automatically when you create an object with `ClassName(...)`.

---

## Default Arguments

Make arguments optional with defaults:

```python
class Point:
    def __init__(self, x=0, y=0):  # Default to origin
        self.move(x, y)

p1 = Point()        # Uses defaults: x=0, y=0
p2 = Point(5)       # x=5, y=0 (default)
p3 = Point(3, 4)    # x=3, y=4
```

---

## Docstrings (Documentation)

Add documentation right in your code using docstrings. Put a string right after the definition line:

```python
class Point:
    'Represents a point in 2D space'
    
    def __init__(self, x=0, y=0):
        '''Initialize a point. x and y default to 0 (origin).'''
        self.move(x, y)
    
    def move(self, x, y):
        "Move the point to new coordinates."
        self.x = x
        self.y = y
    
    def calculate_distance(self, other_point):
        """Calculate distance to another point using Pythagorean theorem.
        
        Args:
            other_point: Another Point object
        
        Returns:
            float: Distance between the two points
        """
        return math.sqrt(
            (self.x - other_point.x)**2 + 
            (self.y - other_point.y)**2
        )
```

Use `help(ClassName)` in Python to see docstrings:
```python
help(Point)  # Shows all docstrings
```

---

## Complete Example

```python
import math

class Point:
    'Represents a point in 2D space'
    
    def __init__(self, x=0, y=0):
        '''Initialize a point (defaults to origin).'''
        self.move(x, y)
    
    def move(self, x, y):
        "Move to new coordinates."
        self.x = x
        self.y = y
    
    def reset(self):
        'Reset to origin (0, 0)'
        self.move(0, 0)
    
    def calculate_distance(self, other_point):
        """Distance to another point (Pythagorean theorem)."""
        return math.sqrt(
            (self.x - other_point.x)**2 + 
            (self.y - other_point.y)**2
        )

# Usage:
p1 = Point(3, 4)
p2 = Point(0, 0)
print(p1.calculate_distance(p2))  # Output: 5.0
```

---

## Quick Summary

| Concept | What It Is |
|---------|-----------|
| **Class** | Blueprint for objects |
| **Object** | Instance of a class |
| **Attribute** | Data on an object (`object.x = 5`) |
| **Method** | Function inside a class (`def method(self):`) |
| **self** | Reference to the object (required in all methods) |
| **__init__** | Constructor—runs when object is created |
| **Docstring** | Documentation string inside code |

---

## Key Rules

✓ Always include `self` as first parameter in methods  
✓ Use `self.attribute` to access/set object data  
✓ Initialize objects with `__init__`  
✓ Write docstrings to document your classes  
✓ Use CamelCase for class names  
✓ Python passes `self` automatically—don't include it when calling methods