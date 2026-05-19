"""Abstract base class examples for the image toolkit.

This module demonstrates how to define an ABC for image filters and how to use
__subclasshook__ to recognize duck-typed implementations without inheritance.
"""

import abc


class ImageFilterInterface(metaclass=abc.ABCMeta):
    """Abstract interface for image filters."""

    @abc.abstractmethod
    def apply(self, image_handler):
        """Apply the filter to an ImageHandler."""
        pass

    @property
    @abc.abstractmethod
    def name(self):
        """Human-readable filter name."""
        pass

    @classmethod
    def __subclasshook__(cls, C):
        if cls is ImageFilterInterface:
            required = {'apply', 'name'}
            attrs = set(dir(C))
            if required <= attrs:
                return True
        return NotImplemented


class DuckTypedFilter:
    """A filter that does not inherit from ImageFilterInterface.

    It is still recognized as a filter through duck typing and the abstract
    base class subclass hook.
    """

    @property
    def name(self):
        return 'DuckTypedFilter'

    def apply(self, image_handler):
        if image_handler.get_data() is None:
            print('[DuckTypedFilter] Image not loaded')
            return False
        print('[DuckTypedFilter] Applying a standalone duck-typed filter')
        return True
