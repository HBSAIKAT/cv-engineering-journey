"""Chapter 3 Image Toolkit Example Package

This package contains learning examples for Chapter 3 OOP concepts:
- inheritance
- method overriding and super()
- multiple inheritance and mixins
- polymorphism
- abstract base classes with duck-typed recognition

The examples use the Chapter 2 image toolkit code as a foundation.
"""

from .image_handler_ext import MetadataImageHandler
from .mixins import (
    VerboseBlurFilter,
    ValidatedResizeFilter,
    VerboseValidatedEnhanceFilter
)
from .abc_filters import ImageFilterInterface, DuckTypedFilter
from .processor import FilterProcessor

__all__ = [
    'MetadataImageHandler',
    'VerboseBlurFilter',
    'ValidatedResizeFilter',
    'VerboseValidatedEnhanceFilter',
    'ImageFilterInterface',
    'DuckTypedFilter',
    'FilterProcessor'
]
