"""Run Chapter 3 image toolkit examples.

This script demonstrates:
- basic inheritance and method overriding
- multiple inheritance and mixins
- polymorphism via a single processor
- abstract base class recognition with duck typing

Run from the example folder:
    python run_example.py
"""

import os
import sys

HERE = os.path.abspath(os.path.dirname(__file__))
IMAGE_TOOLKIT_PATH = os.path.abspath(os.path.join(HERE, '..', 'chapter_02', 'excercise'))
if IMAGE_TOOLKIT_PATH not in sys.path:
    sys.path.insert(0, IMAGE_TOOLKIT_PATH)

from image_toolkit import BlurFilter, GrayscaleFilter, ResizeFilter, EnhanceFilter

from image_handler_ext import MetadataImageHandler
from mixins import VerboseBlurFilter, ValidatedResizeFilter, VerboseValidatedEnhanceFilter
from abc_filters import ImageFilterInterface, DuckTypedFilter
from processor import FilterProcessor


def main():
    print('=== Chapter 3 Image Toolkit Example ===')

    # Basic inheritance example
    handler = MetadataImageHandler('input.jpg', author='Habib')
    handler.load()
    handler.display_metadata()

    # Multiple inheritance and mixin examples
    filters = [
        BlurFilter(radius=3),
        VerboseBlurFilter(radius=2),
        ValidatedResizeFilter(width=320, height=240),
        VerboseValidatedEnhanceFilter(level=1.5),
        GrayscaleFilter()
    ]

    processor = FilterProcessor()
    results = processor.run_pipeline(handler, filters)
    print('\nFilter results:')
    for filt_name, success in results:
        print(f'  - {filt_name}: {success}')

    # Polymorphism with a duck-typed filter
    duck_filter = DuckTypedFilter()
    print('\nDuck-typed filter recognition:')
    print('  is subclass of ImageFilterInterface?', issubclass(DuckTypedFilter, ImageFilterInterface))
    print('  isinstance(direct filter, ImageFilterInterface)?', isinstance(duck_filter, ImageFilterInterface))
    processor.process(handler, duck_filter)

    # Save output using the inherited save method
    handler.save('output.jpg')

    print('\n=== Example complete ===')


if __name__ == '__main__':
    main()
