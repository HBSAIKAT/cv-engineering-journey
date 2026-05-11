# When Objects Are Alike: Inheritance

## Every Class Inherits from object

All Python classes automatically inherit from the built-in `object` class, even if you don't explicitly state it.

```python
# These are equivalent:
class MyClass:
    pass

class MyClass(object):
    pass
```

**Terminology:**
- **Superclass (Parent class)** — The class being inherited from
- **Subclass (Child class)** — The class that inherits from a superclass
- **Derived/Extends** — When a subclass derives from or extends a parent

---

## Basic Inheritance Syntax

Include the parent class name in parentheses after the class name:

```python
class Contact:
    def __init__(self, name, email):
        self.name = name
        self.email = email

class Supplier(Contact):
    def order(self, order):
        print(f"Send '{order}' order to '{self.name}'")
```

The `Supplier` subclass inherits everything from `Contact` and adds its own `order()` method.

---

## Class Variables vs Instance Variables

### Class Variables

Defined at the class level, **shared by all instances**:

```python
class Contact:
    all_contacts = []  # Class variable—one list for all instances
    
    def __init__(self, name, email):
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)
```

Access class variables two ways:
- `Contact.all_contacts` (on the class)
- `self.all_contacts` (on an instance)

Both refer to the same list.

### ⚠️ Common Pitfall

If you **assign** to a class variable using `self`, you create a new **instance variable**:

```python
self.all_contacts = []  # Creates instance variable, NOT class variable
```

Now only that object has its own `all_contacts` list; the class variable is unchanged.

**Fix:** Always use the class name to assign to class variables:
```python
Contact.all_contacts = []  # Use class name
```

---

## Example: Contact and Supplier Classes

```python
class Contact:
    all_contacts = []
    
    def __init__(self, name, email):
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)

class Supplier(Contact):
    def order(self, order):
        print(f"If this were a real system we would send "
              f"'{order}' order to '{self.name}'")
```

### Testing

```python
>>> c = Contact("Some Body", "somebody@example.net")
>>> s = Supplier("Sup Plier", "supplier@example.net")

>>> c.name, s.name
('Some Body', 'Sup Plier')

>>> len(Contact.all_contacts)
2  # Both contact and supplier are in the list

>>> c.order("I need pliers")
AttributeError: 'Contact' object has no attribute 'order'

>>> s.order("I need pliers")
If this were a real system we would send 'I need pliers' order to 'Sup Plier'
```

**Key point:** `Supplier` inherits the `__init__` method and `all_contacts` class variable from `Contact`, and adds its own `order()` method.

---

## Extending Built-in Classes

You can inherit from built-in types like `list`, `dict`, `str`, `set`, `int`, and `float`.

### Example 1: Extending list

```python
class ContactList(list):
    def search(self, name):
        '''Return all contacts containing the search value in their name.'''
        matching_contacts = []
        for contact in self:
            if name in contact.name:
                matching_contacts.append(contact)
        return matching_contacts

class Contact:
    all_contacts = ContactList()  # Use custom list instead of regular list
    
    def __init__(self, name, email):
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)
```

### Testing

```python
>>> c1 = Contact("John A", "johna@example.net")
>>> c2 = Contact("John B", "johnb@example.net")
>>> c3 = Contact("Jenna C", "jennac@example.net")

>>> [c.name for c in Contact.all_contacts.search('John')]
['John A', 'John B']
```

### Why This Works

`[]` syntax is shorthand for `list()`:
```python
[] == list()  # True
```

So `list` is a class you can inherit from.

### Example 2: Extending dict

```python
class LongNameDict(dict):
    def longest_key(self):
        longest = None
        for key in self:
            if not longest or len(key) > len(longest):
                longest = key
        return longest
```

### Testing

```python
>>> longkeys = LongNameDict()
>>> longkeys['hello'] = 1
>>> longkeys['longest yet'] = 5
>>> longkeys['hello2'] = 'world'

>>> longkeys.longest_key()
'longest yet'
```

---

## Overriding Methods

**Overriding** means replacing a parent method with a new method in the subclass.

No special syntax needed—just define a method with the same name:

```python
class Contact:
    def __init__(self, name, email):
        self.name = name
        self.email = email

class Friend(Contact):
    def __init__(self, name, email, phone):  # Override __init__
        self.name = name
        self.email = email
        self.phone = phone
```

**Any method can be overridden**, not just `__init__`.

---

## The super() Function

### Problem with Overriding

When you override a method, you might duplicate code:

```python
class Friend(Contact):
    def __init__(self, name, email, phone):
        self.name = name         # Duplicated from Contact
        self.email = email       # Duplicated from Contact
        self.phone = phone       # New code
```

**Also:** Friend doesn't add itself to `all_contacts` list!

### Solution: Use super()

`super()` returns the parent class, allowing you to call the parent's method:

```python
class Friend(Contact):
    def __init__(self, name, email, phone):
        super().__init__(name, email)  # Call parent's __init__
        self.phone = phone
```

This:
- Calls `Contact.__init__(name, email)`
- Adds friend to `all_contacts` automatically
- Avoids code duplication

### Using super() in Any Method

`super()` can be called in any method, not just `__init__`:

```python
class Friend(Contact):
    def contact_info(self):
        parent_info = super().contact_info()  # Call parent method
        return parent_info + f"\nPhone: {self.phone}"
```

### Calling super() at Any Point

You don't have to call `super()` as the first line:

```python
class Friend(Contact):
    def __init__(self, name, email, phone):
        # Validate phone first
        if not phone.startswith('+'):
            phone = '+1' + phone
        
        # Then call parent
        super().__init__(name, email)
        self.phone = phone
```

---

## Python 2 vs Python 3 super()

### Python 3 (Simple)

```python
super().__init__(name, email)
```

### Python 2 (Verbose)

```python
super(Friend, self).__init__(name, email)
```

**Note:** In Python 2, the first argument is the **child class name**, not the parent. Python 3's simplified syntax is cleaner.

---

## Complete Example

```python
class Contact:
    all_contacts = []
    
    def __init__(self, name, email):
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)

class Friend(Contact):
    def __init__(self, name, email, phone):
        super().__init__(name, email)  # Reuse Contact's init
        self.phone = phone

class Supplier(Contact):
    def __init__(self, name, email, order_code):
        super().__init__(name, email)  # Reuse Contact's init
        self.order_code = order_code
    
    def order(self, order):
        print(f"Send '{order}' to {self.name}")
```

### Testing

```python
>>> f = Friend("Jane Doe", "jane@example.net", "555-1234")
>>> s = Supplier("Acme Corp", "acme@example.net", "ACME123")

>>> Contact.all_contacts
[<Friend object>, <Supplier object>]

>>> f.phone
'555-1234'

>>> s.order("Widget")
Send 'Widget' to Acme Corp
```

---

## Key Rules

✓ All classes inherit from `object` (explicitly or implicitly)  
✓ Use parent class name in parentheses to inherit: `class Child(Parent):`  
✓ Class variables (defined in class body) are shared by all instances  
✓ Don't assign to class variables using `self`—use the class name  
✓ Override methods by redefining them in the subclass  
✓ Use `super()` to call parent methods and avoid code duplication  
✓ `super()` works in any method, not just `__init__`  
✓ You can inherit from built-in types: `list`, `dict`, `str`, `int`, `float`, `set`  
✓ Check for code duplication—it's a sign you need `super()`

---

## Built-in Types You Can Extend

| Type | Syntax | Use Case |
|------|--------|----------|
| `object` | Implicit (all classes) | Base of all classes |
| `list` | `class MyList(list):` | Add list methods |
| `dict` | `class MyDict(dict):` | Add dict methods |
| `str` | `class MyString(str):` | Add string methods |
| `set` | `class MySet(set):` | Add set methods |
| `int` | `class MyInt(int):` | Add integer methods |
| `float` | `class MyFloat(float):` | Add float methods |