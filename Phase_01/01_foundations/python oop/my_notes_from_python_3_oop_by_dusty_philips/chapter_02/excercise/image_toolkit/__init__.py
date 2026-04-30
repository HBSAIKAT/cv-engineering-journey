"""
Image Toolkit Package
Chapter 2 Learning: Classes, Modules, Packages, and Import Organization

This package provides a modular image processing toolkit built with core OOP concepts.

Main components:
    - image_handler: ImageHandler class for image operations
    - filters: Filter base class and concrete filter implementations
    - pipeline: FilterPipeline class for managing filter sequences
    - recipe: RecipeManager class for saving/loading configurations
"""

from .image_handler import ImageHandler
from .filters import Filter, BlurFilter, GrayscaleFilter, ResizeFilter, EnhanceFilter
from .pipeline import FilterPipeline
from .recipe import RecipeManager

__all__ = [
    'ImageHandler',
    'Filter',
    'BlurFilter',
    'GrayscaleFilter',
    'ResizeFilter',
    'EnhanceFilter',
    'FilterPipeline',
    'RecipeManager'
]
