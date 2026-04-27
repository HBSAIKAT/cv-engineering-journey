# Modules and Packages

## What is a Module?

A **module** is a Python file. That's it.

- One file = one module
- Multiple files = multiple modules
- Files in the same folder can import from each other

**Example:** `database.py` and `products.py` are two separate modules in the same folder.

---

## The `import` Statement

### Import entire module

```python
import database
db = database.Database()
```

This imports the `database` module into our namespace. Access classes/functions using `database.<something>`.

### Import specific class

```python
from database import Database
db = Database()
```

This imports only the `Database` class. we access it directly by name.

### Rename imports to avoid conflicts

```python
from database import Database as DB
db = DB()
```

Useful if our module already has a class with the same name.

### Import multiple items

```python
from database import Database, Query
```

---

## ⚠️ Never Use `import *`

```python
# DON'T DO THIS:
from database import *
```

**Why it's bad:**

1. **Hard to find classes** — we see `db = Database()` 400 lines later, but where did `Database` come from? we have to hunt for the import.

2. **Breaks editor tools** — Code completion, jump-to-definition, and inline documentation don't work reliably.

3. **Imports everything** — It imports not just what's defined in the module, but also anything that module imported. Unexpected names appear in our namespace.

4. **"Magic variables"** — Names appear to come from nowhere. Every name should have a clear, specified origin.

**Instead, be explicit:**
```python
from database import Database
```

Now we can immediately see where `Database` came from.

---

## Packages

A **package** is a folder containing modules. To make a folder a package, add an empty file named `__init__.py` in it.

**Without `__init__.py`**, Python won't recognize it as a package.

### Example folder structure

```
parent_directory/
    main.py
    ecommerce/
        __init__.py
        database.py
        products.py
        payments/
            __init__.py
            square.py
            stripe.py
```

- `ecommerce/` is a package
- `payments/` is a subpackage inside `ecommerce/`
- `database.py` and `products.py` are modules inside the `ecommerce` package
- `square.py` and `stripe.py` are modules inside the `ecommerce.payments` package

---

## Absolute Imports

**Absolute imports** specify the complete path to what we want to import. They work from any module.

### Option 1: Import the module, access the class

```python
import ecommerce.products
product = ecommerce.products.Product()
```

### Option 2: Import the class directly

```python
from ecommerce.products import Product
product = Product()
```

### Option 3: Import the module by name

```python
from ecommerce import products
product = products.Product()
```

Use periods to separate packages and modules.

### Which syntax to choose?

- If importing many classes from a module: `from ecommerce import products` then use `products.Product`
- If importing only one or two classes: `from ecommerce.products import Product`
- If we have name conflicts between modules: `import ecommerce.products`

---

## Relative Imports

**Relative imports** specify a module's position relative to the current module. Useful when modules are in the same package.

### One level up (same package)

In `products.py`, import from `database.py`:

```python
from .database import Database
```

The `.` means "look in the current package."

### Two levels up (parent package)

In `ecommerce/payments/paypal.py`, import from `ecommerce/database.py`:

```python
from ..database import Database
```

The `..` means "go up to the parent package."

### Going up then back down

Import from a sibling package:

```python
from ..contact.email import send_mail
```

- `..` = go to parent package
- `contact.email` = go into contact package, then email module

---

## Using `__init__.py`

The `__init__.py` file can contain variable and class declarations. These become part of the package.

**Example:** If `ecommerce/database.py` has a `db` variable:

**Without `__init__.py` code:**
```python
from ecommerce.database import db
```

**With code in `ecommerce/__init__.py`:**
```python
from .database import db
```

**Now we can import directly from the package:**
```python
from ecommerce import db
```

This makes the package the main point of contact for other modules.

### Note

Don't put all our code in `__init__.py`. Programmers don't expect logic there—they'll look elsewhere for class definitions and get confused if the code is hidden in `__init__.py`.

---

## Quick Reference

| Task | Code |
|------|------|
| Import entire module | `import database` |
| Import specific class | `from database import Database` |
| Rename on import | `from database import Database as DB` |
| Import multiple items | `from database import Database, Query` |
| Absolute import (nested) | `from ecommerce.products import Product` |
| Relative import (same package) | `from .database import Database` |
| Relative import (parent package) | `from ..database import Database` |
| Never use | `from database import *` |

---

## Key Rules

✓ Use explicit imports (name the class we want)  
✓ Never use `import *`  
✓ Create `__init__.py` to make a folder a package  
✓ Use absolute imports or relative imports consistently  
✓ Keep logic out of `__init__.py`