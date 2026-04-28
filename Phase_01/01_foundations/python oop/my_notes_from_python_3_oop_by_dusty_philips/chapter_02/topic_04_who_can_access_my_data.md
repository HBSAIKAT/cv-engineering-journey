# Who Can Access My Data?

## Access Control in Other Languages

Most object-oriented languages enforce access control:

- **Private** — Only the object itself can access
- **Protected** — Only the class and its subclasses can access
- **Public** — Any object can access

---

## Python's Philosophy

Python **doesn't enforce** access control. Instead, it provides **unenforced guidelines** based on naming conventions.

**Why?** Python trusts programmers and believes restrictions might get in our way. If someone needs to access "private" data, maybe they have a good reason.

---

## Single Underscore `_` (Soft Privacy)

Prefix attributes or methods with a single underscore to suggest they're for internal use only:

```python
class MyClass:
    def __init__(self):
        self._internal_value = 42  # Internal use only
    
    def _internal_method(self):
        """Internal method—don't call this directly."""
        return self._internal_value
```

**What it means:**
- Python programmers will see `_` and think: "This is internal. Think three times before accessing it."
- Nothing stops them from accessing it if they have a good reason
- Documented in docstrings as internal

**When to use:** For attributes/methods not meant for public API, but might be useful to subclasses or in special cases.

---

## Double Underscore `__` (Hard Privacy via Name Mangling)

Prefix attributes with a double underscore to apply **name mangling**:

```python
class SecretString:
    '''A not-at-all secure way to store a secret string.'''
    
    def __init__(self, plain_string, pass_phrase):
        self.__plain_string = plain_string
        self.__pass_phrase = pass_phrase
    
    def decrypt(self, pass_phrase):
        '''Only show the string if the pass_phrase is correct.'''
        if pass_phrase == self.__pass_phrase:
            return self.__plain_string
        else:
            return ''
```

### How Name Mangling Works

**From inside the class (works normally):**
```python
def decrypt(self, pass_phrase):
    return self.__plain_string  # Works fine
```

**From outside the class (normal access fails):**
```python
secret = SecretString("ACME: Top Secret", "antwerp")
print(secret.__plain_string)
# AttributeError: 'SecretString' object has no attribute '__plain_string'
```

**Name mangling is applied automatically inside the class**, so it just works.

### Breaking Name Mangling (Still Possible)

Name mangling is **not true privacy**. It's easy to circumvent:

```python
secret = SecretString("ACME: Top Secret", "antwerp")
print(secret._SecretString__plain_string)
# Output: ACME: Top Secret
```

When we use `__`, Python renames the attribute to `_<classname><attribute>`. we can access it if we know this pattern.

---

## Name Mangling Details

- **Internal access:** Automatically unmangled by Python
- **External access:** Requires manual name mangling pattern: `_ClassName__attribute`
- **Subclasses:** Must also do manual mangling to access parent's double-underscore attributes

---

## Single vs. Double Underscore

| Prefix | Level | Enforcement | Use Case |
|--------|-------|-------------|----------|
| `_single` | Soft privacy | Convention only | Internal but might be useful |
| `__double` | Name mangling | Easy to break | Strongly discourage access |
| No prefix | Public | None | Public API |

---

## Best Practice Recommendation

**Use single underscore `_` instead of double underscore `__`:**

1. **Single underscore is respected** — Most Python programmers won't touch it without a good reason
2. **Easier for subclasses** — They can use the attribute without manual mangling
3. **Less grief** — Double underscore can cause problems in inheritance

**Why avoid double underscore?**
- Subclasses can't easily access parent's double-underscore attributes
- Name mangling isn't real privacy anyway
- Single underscore is sufficient for 99% of cases

---

## Example: Single Underscore

```python
class BankAccount:
    def __init__(self, balance):
        self._balance = balance  # Internal, but accessible if needed
    
    def deposit(self, amount):
        '''Public method for depositing money.'''
        self._balance += amount
    
    def get_balance(self):
        '''Public method for checking balance.'''
        return self._balance
```

**Usage:**
```python
account = BankAccount(1000)
account.deposit(500)
print(account.get_balance())  # 1500

# Someone with a good reason can access _balance:
print(account._balance)  # 1500 (works, but understood to be internal)
```

---

## Philosophy Summary

Python says:
- **"We're all consenting adults here"** — Don't use access control to prevent misuse
- **Document our intentions** — Use docstrings to explain what's public vs. internal
- **Use naming conventions** — Single underscore for "internal," no underscore for "public"
- **Trust developers** — If they need to access "private" data, they probably have a reason

---

## Key Rules

✓ Use single underscore `_` for internal attributes/methods  
✓ Document internals clearly in docstrings  
✓ Don't use double underscore `__` (except in rare cases)  
✓ Remember: nothing is truly private in Python—it's all convention  
✓ Trust other programmers to use internal APIs responsibly