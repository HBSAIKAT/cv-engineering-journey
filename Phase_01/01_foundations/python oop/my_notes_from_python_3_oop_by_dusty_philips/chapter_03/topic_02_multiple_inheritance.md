# Multiple Inheritance and the Diamond Problem

## Basic Multiple Inheritance

A class can inherit from **multiple parent classes**:

```python
class Contact:
    def __init__(self, name, email):
        self.name = name
        self.email = email

class AddressHolder:
    def __init__(self, street, city, state, code):
        self.street = street
        self.city = city
        self.state = state
        self.code = code

class Friend(Contact, AddressHolder):
    def __init__(self, name, email, phone, street, city, state, code):
        Contact.__init__(self, name, email)
        AddressHolder.__init__(self, street, city, state, code)
        self.phone = phone
```

**Syntax:** List parent classes in parentheses, separated by commas.

---

## The Diamond Problem

Multiple inheritance creates a problem when the hierarchy forms a **diamond shape**:

```
       BaseClass
       /        \
LeftSubclass  RightSubclass
       \        /
       Subclass
```

### The Problem: Double Initialization

When both parents inherit from the same grandparent, that grandparent gets initialized twice:

```python
class Friend(Contact, AddressHolder):
    def __init__(self, ...):
        Contact.__init__(self, ...)        # Calls object.__init__
        AddressHolder.__init__(self, ...)  # Calls object.__init__ AGAIN
```

**Result:** Dangerous when base class does real work (database connection, payment, etc.).

---

## Diamond Problem Example

```python
class BaseClass:
    num_base_calls = 0
    def call_me(self):
        print("Calling method on Base Class")
        self.num_base_calls += 1

class LeftSubclass(BaseClass):
    num_left_calls = 0
    def call_me(self):
        BaseClass.call_me(self)
        print("Calling method on Left Subclass")
        self.num_left_calls += 1

class RightSubclass(BaseClass):
    num_right_calls = 0
    def call_me(self):
        BaseClass.call_me(self)
        print("Calling method on Right Subclass")
        self.num_right_calls += 1

class Subclass(LeftSubclass, RightSubclass):
    num_sub_calls = 0
    def call_me(self):
        LeftSubclass.call_me(self)
        RightSubclass.call_me(self)
        print("Calling method on Subclass")
        self.num_sub_calls += 1
```

### Output (Naive Approach)

```python
>>> s = Subclass()
>>> s.call_me()
Calling method on Base Class
Calling method on Left Subclass
Calling method on Base Class      # CALLED TWICE!
Calling method on Right Subclass
Calling method on Subclass

>>> s.num_base_calls
2  # Problem!
```

---

## Solution: Use super()

Replace direct parent calls with `super()`:

```python
class BaseClass:
    num_base_calls = 0
    def call_me(self):
        print("Calling method on Base Class")
        self.num_base_calls += 1

class LeftSubclass(BaseClass):
    num_left_calls = 0
    def call_me(self):
        super().call_me()
        print("Calling method on Left Subclass")
        self.num_left_calls += 1

class RightSubclass(BaseClass):
    num_right_calls = 0
    def call_me(self):
        super().call_me()
        print("Calling method on Right Subclass")
        self.num_right_calls += 1

class Subclass(LeftSubclass, RightSubclass):
    num_sub_calls = 0
    def call_me(self):
        super().call_me()  # Call super ONCE
        print("Calling method on Subclass")
        self.num_sub_calls += 1
```

### Output (With super())

```python
>>> s = Subclass()
>>> s.call_me()
Calling method on Base Class
Calling method on Right Subclass
Calling method on Left Subclass
Calling method on Subclass

>>> s.num_base_calls
1  # Solved!
```

---

## How super() Works in Multiple Inheritance

`super()` calls the **next method in the inheritance order**, not the direct parent.

**Trace for Subclass().call_me():**

1. `Subclass.call_me()` → calls `super().call_me()`
2. `super()` → `LeftSubclass.call_me()` (next in MRO)
3. `LeftSubclass.call_me()` → calls `super().call_me()`
4. `super()` → `RightSubclass.call_me()` (next, NOT parent!)
5. `RightSubclass.call_me()` → calls `super().call_me()`
6. `super()` → `BaseClass.call_me()` (next)
7. `BaseClass.call_me()` → no `super()` call; unwinds

**Key:** The next method may not be the direct parent!

---

## Multiple Inheritance with Different Arguments

### Problem

Different parents need different `__init__` arguments. How do we pass them with `super()`?

### Solution: **kwargs

Use keyword arguments with defaults and `**kwargs`:

```python
class Contact:
    all_contacts = []
    def __init__(self, name='', email='', **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)

class AddressHolder:
    def __init__(self, street='', city='', state='', code='', **kwargs):
        super().__init__(**kwargs)
        self.street = street
        self.city = city
        self.state = state
        self.code = code

class Friend(Contact, AddressHolder):
    def __init__(self, phone='', **kwargs):
        super().__init__(**kwargs)
        self.phone = phone
```

### How It Works

```python
f = Friend(
    name='John',
    email='john@example.com',
    phone='555-1234',
    street='123 Main St',
    city='Anytown',
    state='CA',
    code='90210'
)
```

1. `Friend.__init__` captures `phone`, passes rest via `super().__init__(**kwargs)`
2. `Contact.__init__` captures `name` and `email`, passes rest via `super().__init__(**kwargs)`
3. `AddressHolder.__init__` captures address fields, passes rest via `super().__init__(**kwargs)`
4. `object.__init__` ignores unused kwargs

---

## **kwargs Syntax

**`**kwargs`** collects keyword arguments into a dictionary:

```python
def method(name, **kwargs):
    print(kwargs)  # Remaining keyword arguments

method(name='John', age=30, city='NYC')
# kwargs = {'age': 30, 'city': 'NYC'}
```

**`**kwargs` unpacking** passes dictionary items as keyword arguments:

```python
kwargs = {'age': 30, 'city': 'NYC'}
method(name='John', **kwargs)
# Expands to: method(name='John', age=30, city='NYC')
```

---

## Ensuring Variables Reach All Parents

When a parameter is explicit, it won't pass to `super()` automatically:

```python
class Friend(Contact, AddressHolder):
    def __init__(self, phone='', **kwargs):
        super().__init__(**kwargs)  # phone is NOT in kwargs!
        self.phone = phone
```

### Solutions

**Option 1:** Explicitly pass in super():

```python
super().__init__(phone=phone, **kwargs)
```

**Option 2:** Add to kwargs before super():

```python
kwargs['phone'] = phone
super().__init__(**kwargs)
```

**Option 3:** Use kwargs.update():

```python
kwargs.update(phone=phone)
super().__init__(**kwargs)
```

---

## When to Avoid Multiple Inheritance

Multiple inheritance becomes complex. **Prefer:**

- **Composition** — Simpler and clearer
- **Design patterns** — Decorator, Strategy, Mixin
- **Single inheritance** — Often sufficient

---

## Complete Working Example

```python
class Contact:
    all_contacts = []
    def __init__(self, name='', email='', **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)

class AddressHolder:
    def __init__(self, street='', city='', state='', code='', **kwargs):
        super().__init__(**kwargs)
        self.street = street
        self.city = city
        self.state = state
        self.code = code

class Friend(Contact, AddressHolder):
    def __init__(self, phone='', **kwargs):
        super().__init__(**kwargs)
        self.phone = phone

# Usage:
f = Friend(
    name='Alice',
    email='alice@example.com',
    phone='555-1234',
    street='123 Main',
    city='Springfield',
    state='IL',
    code='62701'
)

print(f.name)      # Alice
print(f.phone)     # 555-1234
print(f.street)    # 123 Main
```

No double initialization!

---

## Key Rules

✓ Use `super()` instead of direct parent calls  
✓ `super()` calls the NEXT method, not necessarily the parent  
✓ All `__init__` methods need `**kwargs`  
✓ Give parameters default values  
✓ Call `super()` only once per method  
✓ Document expected arguments clearly  
✓ Consider composition before multiple inheritance  
✓ Test thoroughly—bugs are hard to debug