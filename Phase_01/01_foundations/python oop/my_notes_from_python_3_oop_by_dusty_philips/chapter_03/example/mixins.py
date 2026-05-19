"""Multiple inheritance examples for the image toolkit.

This module defines mixins that modify filter behavior using multiple inheritance.
The examples show how method resolution order (MRO) and super() combine behaviors.
"""

from image_toolkit.filters import BlurFilter, ResizeFilter, EnhanceFilter


class FilterLoggingMixin:
    """Mixin that logs filter execution before delegating."""

    def apply(self, image_handler):
        print(f"[LoggingMixin] Running {self.__class__.__name__}")
        return super().apply(image_handler)


class FilterValidationMixin:
    """Mixin that validates the image before applying the filter."""

    def apply(self, image_handler):
        if image_handler.get_data() is None:
            print(f"[ValidationMixin] Skipping {self.__class__.__name__}: image not loaded")
            return False
        width, height = image_handler.get_dimensions()
        if width == 0 or height == 0:
            print(f"[ValidationMixin] Skipping {self.__class__.__name__}: invalid dimensions")
            return False
        return super().apply(image_handler)


class VerboseBlurFilter(FilterLoggingMixin, BlurFilter):
    """Combined filter showing logging + blur behavior."""
    pass


class ValidatedResizeFilter(FilterValidationMixin, ResizeFilter):
    """Combined filter showing validation + resize behavior."""
    pass


class VerboseValidatedEnhanceFilter(FilterLoggingMixin, FilterValidationMixin, EnhanceFilter):
    """Combined filter with logging, validation, and enhancement."""
    pass
