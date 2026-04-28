# Third-Party Libraries

## What are Third-Party Libraries?

Python ships with a **standard library** of packages and modules available on every Python installation. When we need something not in the standard library, we have two options:

1. Write our own package
2. Use somebody else's code (third-party libraries)

---

## Python Package Index (PyPI)

**PyPI** (Python Package Index) is a repository of third-party Python libraries.

**Website:** http://pypi.python.org/

we can search for and find almost any library we need there.

---

## Installing Packages with pip

### Install pip

`pip` is a tool for installing third-party libraries. It doesn't come with Python, but Python 3.4+ includes `ensurepip` to install it:

```bash
python -m ensurepip
```

**On Linux, Mac, or Unix (if permission denied):**
```bash
sudo python -m ensurepip
```

**For Python < 3.4:**
Download and install pip manually from http://pip.readthedocs.org/

### Install a Package

Once pip is installed, use it to install packages:

```bash
pip install requests
```

---

## The Problem with Global Installation

Installing directly with `pip install package_name` might:

- Install to our **system Python directory** (bad practice)
- Require **administrator/root permissions**
- Conflict with system-installed packages
- Affect all our Python projects globally

**Common consensus:** Only use system installers for system Python packages. Don't use `pip` to install globally.

---

## Virtual Environments with venv

### What is a Virtual Environment?

A **virtual environment** is a mini Python installation in our project directory. It isolates each project's dependencies.

### Create a Virtual Environment

Python 3.4+ includes the `venv` tool:

```bash
cd project_directory
python -m venv env
```

This creates a folder named `env` containing a mini Python installation.

### Activate the Virtual Environment

**On Linux or macOS:**
```bash
source env/bin/activate
```

**On Windows:**
```bash
env\Scripts\activate.bat
```

Once activated, Python and pip commands work on the **project directory**, not the system directory.

### Deactivate the Virtual Environment

When we're done working:

```bash
deactivate
```

---

## How Virtual Environments Work

When a virtual environment is **activated:**

- `python` command runs the mini Python (not system Python)
- `pip` installs packages to the virtual environment (not system)
- All Python dependencies are isolated to this project

**Result:** Our project is completely independent from other projects and the system.

---

## Best Practices

### Use a Virtual Environment for Each Project

```bash
# Project 1
cd project1
python -m venv env
source env/bin/activate
pip install django==1.5

# Project 2
cd project2
python -m venv env
source env/bin/activate
pip install django==1.8

# Both can run simultaneously without conflicts
deactivate  # When done with project
```

### Why This Matters

**Problem:** Different projects need different library versions.
- Old website uses Django 1.5
- New website uses Django 1.8

**Solution:** Virtual environments keep them separate.

### Prevent Version Conflicts

Virtual environments prevent conflicts between:
- Different projects with different dependency versions
- System-installed packages and pip-installed packages
- Multiple versions of the same library

---

## Virtual Environment Directory Structure

```
project_directory/
    env/
        bin/
            python
            pip
            activate
        lib/
            python3.x/
                site-packages/  (installed packages go here)
    src/
        my_code.py
    README.md
```

---

## Typical Workflow

```bash
# 1. Navigate to project directory
cd my_project

# 2. Create virtual environment (first time only)
python -m venv env

# 3. Activate it (every time we work on the project)
source env/bin/activate  # Linux/Mac
# or
env\Scripts\activate.bat  # Windows

# 4. Install packages
pip install requests
pip install flask

# 5. Do our work
python my_code.py

# 6. Deactivate when done
deactivate
```

---

## Quick Reference

| Task | Command |
|------|---------|
| Install pip | `python -m ensurepip` |
| Create venv | `python -m venv env` |
| Activate (Linux/Mac) | `source env/bin/activate` |
| Activate (Windows) | `env\Scripts\activate.bat` |
| Install package | `pip install package_name` |
| Deactivate venv | `deactivate` |
| List installed packages | `pip list` |

---

## Key Rules

✓ Create a virtual environment for each project  
✓ Activate it before installing packages or running code  
✓ Never use `pip install` in global/system Python  
✓ Keep virtual environments in our project directory  
✓ Deactivate when our done working  
✓ Use virtual environments to avoid version conflicts  
✓ Always activate before running `pip` or `python`