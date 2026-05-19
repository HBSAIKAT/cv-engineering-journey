"""Inheritance example for the image toolkit.

This module extends the Chapter 2 ImageHandler class to demonstrate:
- basic inheritance
- method overriding
- use of super()
- adding a custom public interface on a subclass
"""

from image_toolkit.image_handler import ImageHandler


class MetadataImageHandler(ImageHandler):
    """ImageHandler subclass that stores extra image metadata."""

    def __init__(self, file_path, author=None):
        super().__init__(file_path)
        self.author = author
        self.metadata = {}

    def load(self):
        """Load image data and capture metadata."""
        loaded = super().load()
        if loaded:
            self.metadata = {
                'source': self.file_path,
                'author': self.author or 'unknown',
                'format': 'simulated',
                'dimensions': self.get_dimensions()
            }
        return loaded

    def save(self, output_path):
        """Save image with metadata info."""
        print(f"MetadataImageHandler: saving metadata for {self.file_path}")
        if self.metadata:
            print(f"  metadata: {self.metadata}")
        return super().save(output_path)

    def display_metadata(self):
        """Show metadata stored on this image."""
        print("Image Metadata")
        print("--------------")
        for key, value in self.metadata.items():
            print(f"{key}: {value}")
