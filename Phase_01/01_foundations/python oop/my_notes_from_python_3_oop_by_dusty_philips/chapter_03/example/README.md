# Chapter 3 Image Toolkit Examples

This folder contains learning examples that apply Chapter 3 OOP concepts to the Image Toolkit project.

## Concepts Demonstrated

- **Basic inheritance**: `MetadataImageHandler` extends the Chapter 2 `ImageHandler` class.
- **Method overriding and `super()`**: `MetadataImageHandler` overrides `load()` and `save()` while reusing base logic.
- **Multiple inheritance and mixins**: `FilterLoggingMixin` and `FilterValidationMixin` combine with existing filter classes.
- **Polymorphism**: `FilterProcessor` uses a single processing interface for different filter objects.
- **Abstract base classes**: `ImageFilterInterface` defines a filter contract and recognizes duck-typed filters.

## Files

- `image_handler_ext.py` - inheritance example with metadata-enabled image handler.
- `mixins.py` - multiple inheritance examples with filter mixins.
- `abc_filters.py` - abstract base class and duck typing example.
- `processor.py` - a polymorphic filter processor.
- `run_example.py` - demo script showing how all examples work together.

## Run the example

From this folder:

```bash
python run_example.py
```

The script is intentionally lightweight and uses the existing Chapter 2 `image_toolkit` package as the foundation. It is designed for learning, not a production image pipeline.
