"""Polymorphism example for image toolkit filters.

This module processes filters using a single interface and shows how
objects with the same methods behave polymorphically.
"""

from .abc_filters import ImageFilterInterface


class FilterProcessor:
    """Processes image filters using a common interface."""

    def process(self, image_handler, filter_obj):
        """Apply a filter to the image handler using duck typing."""
        filter_name = getattr(filter_obj, 'name', filter_obj.__class__.__name__)
        print(f"\n[FilterProcessor] Processing with: {filter_name}")

        if isinstance(filter_obj, ImageFilterInterface):
            print(f"[FilterProcessor] Detected ImageFilterInterface: {filter_name}")

        if not hasattr(filter_obj, 'apply'):
            raise TypeError(f"Object {filter_obj} is not a valid filter")

        return filter_obj.apply(image_handler)

    def run_pipeline(self, image_handler, filters):
        """Run a sequence of filters on the image handler."""
        results = []
        for filter_obj in filters:
            result = self.process(image_handler, filter_obj)
            results.append((filter_obj.__class__.__name__, result))
        return results
