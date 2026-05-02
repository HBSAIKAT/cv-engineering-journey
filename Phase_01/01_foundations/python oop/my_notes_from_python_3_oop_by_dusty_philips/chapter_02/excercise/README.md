# Image Toolkit - Chapter 2 Implementation

## Overview
This is the Image Toolkit project built using **Chapter 2 OOP concepts** from Python 3 OOP by Dusty Phillips.

## Chapter 2 Concepts Applied

### 1. Creating Python Classes (Topic 1)
- **Basic class structure**: Each component (ImageHandler, Filter, Pipeline) is defined as a class
- **`__init__` method**: Initialization methods for all classes
- **Attributes**: Objects store data using attributes (e.g., `file_path`, `_data`, `_filters`)
- **Methods**: Classes implement behaviors through methods (e.g., `load()`, `apply()`, `execute()`)
- **`self` parameter**: All methods use `self` to reference the object instance

**Example:**
```python
class ImageHandler:
    def __init__(self, file_path):
        self.file_path = file_path
        self._data = None
    
    def load(self):
        # Method implementation
```

### 2. Modules and Packages (Topic 2)
- **Module structure**: Each component is in its own module:
  - `image_handler.py`
  - `filters.py`
  - `pipeline.py`
  - `recipe.py`
- **Import statements**: Explicit imports (no `import *`)
- **Package creation**: `image_toolkit/` folder with `__init__.py`
- **Absolute imports**: Using full paths to import from the package

**Example:**
```python
from image_toolkit import ImageHandler, FilterPipeline
```

### 3. Organizing Module Contents (Topic 3)
- **Module-level docstrings**: Each module includes documentation
- **`__init__.py` organization**: Package exports main classes via `__all__`
- **`__name__ == "__main__"` guard**: Demo module only runs when executed directly
- **Logical grouping**: Related classes in the same module

**Example:**
```python
if __name__ == "__main__":
    main()
```

### 4. Who Can Access My Data? (Topic 4)
- **Single underscore (`_`)**: Internal attributes marked for soft privacy
  - `_data`, `_width`, `_height` in ImageHandler
  - `_filters` in FilterPipeline
  - Suggests "internal use only" to other programmers
- **Public interface**: Methods like `get_data()` and `get_dimensions()` provide controlled access

**Example:**
```python
class ImageHandler:
    def __init__(self):
        self._data = None  # Soft privacy - internal use
    
    def get_data(self):   # Public interface
        return self._data
```

### 5. Third-Party Libraries (Topic 5)
- **JSON module**: Used in RecipeManager for serialization
- **Import from standard library**: `import json`
- **Integration patterns**: Using standard library responsibly

**Example:**
```python
import json
with open(file_path, 'w') as f:
    json.dump(recipe_dict, f, indent=2)
```

## Project Structure

```
chapter_02/excercise/
├── image_toolkit/              # Package
│   ├── __init__.py            # Package initialization and exports
│   ├── image_handler.py       # ImageHandler class
│   ├── filters.py             # Filter base class and implementations
│   ├── pipeline.py            # FilterPipeline class
│   └── recipe.py              # RecipeManager class
├── demo.py                    # Demo script using __name__ guard
└── recipes/                   # Directory for saving recipes (created at runtime)
```

## Usage

### Run the demo:
```bash
cd chapter_02/excercise
python demo.py
```

### Use in your own scripts:
```python
from image_toolkit import ImageHandler, FilterPipeline, BlurFilter

# Create image handler
image = ImageHandler("input.jpg")
image.load()

# Build pipeline
pipeline = FilterPipeline()
pipeline.add_filter(BlurFilter(radius=5))

# Execute
pipeline.execute(image)
image.save("output.jpg")
```

## Key Learning Points

1. **Classes are blueprints** for creating objects with specific structure and behavior
2. **Modules organize code** by putting related classes in separate files
3. **Packages group modules** using `__init__.py` for convenient importing
4. **Access control conventions** (underscore naming) guide proper API usage
5. **Standard library modules** (like `json`) extend functionality

## Alignment with Chapter 1 Architecture

This implementation respects the design from Chapter 1:
- **ImageHandler**: Represents a single image
- **Filter classes**: Individual transformations (BlurFilter, GrayscaleFilter, etc.)
- **FilterPipeline**: Manages ordered sequence of filters
- **RecipeManager**: Saves/loads filter configurations

The Chapter 2 implementation provides a **minimal, working foundation** that will be enhanced with more advanced OOP concepts in subsequent chapters.
