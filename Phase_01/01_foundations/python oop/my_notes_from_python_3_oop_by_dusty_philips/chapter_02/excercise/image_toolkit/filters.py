"""
Filters module - Contains filter base class and concrete filter implementations.
Chapter 2 Concepts: Abstract base classes, __init__, methods, and inheritance basics.
"""


class Filter:
    """
    Abstract base class for all filters.
    
    Defines the interface that all concrete filters must implement.
    
    Attributes:
        config: Configuration dictionary for the filter
    """
    
    def __init__(self, config=None):
        """
        Initialize filter with configuration.
        
        Args:
            config (dict): Filter configuration parameters
        """
        self.config = config or {}
    
    def apply(self, image_handler):
        """
        Apply filter to an image.
        
        Args:
            image_handler: ImageHandler object to apply filter on
            
        Returns:
            bool: Success status
        """
        raise NotImplementedError("Subclasses must implement apply() method")


class BlurFilter(Filter):
    """
    Applies blur effect to image.
    
    Attributes:
        config: Must contain 'radius' key for blur radius
    """
    
    def __init__(self, radius=5):
        """
        Initialize BlurFilter.
        
        Args:
            radius (int): Blur radius in pixels
        """
        super().__init__({'radius': radius})
    
    def apply(self, image_handler):
        """
        Apply blur filter to image.
        
        Args:
            image_handler: ImageHandler object
            
        Returns:
            bool: Success status
        """
        if image_handler.get_data() is None:
            print("Error: Image not loaded")
            return False
        
        radius = self.config.get('radius', 5)
        print(f"Applying BlurFilter with radius={radius}")
        return True


class GrayscaleFilter(Filter):
    """
    Converts image to grayscale.
    """
    
    def __init__(self):
        """Initialize GrayscaleFilter."""
        super().__init__({})
    
    def apply(self, image_handler):
        """
        Apply grayscale filter to image.
        
        Args:
            image_handler: ImageHandler object
            
        Returns:
            bool: Success status
        """
        if image_handler.get_data() is None:
            print("Error: Image not loaded")
            return False
        
        print("Applying GrayscaleFilter")
        return True


class ResizeFilter(Filter):
    """
    Resizes image to specified dimensions.
    
    Attributes:
        config: Must contain 'width' and 'height' keys
    """
    
    def __init__(self, width, height):
        """
        Initialize ResizeFilter.
        
        Args:
            width (int): Target width in pixels
            height (int): Target height in pixels
        """
        super().__init__({'width': width, 'height': height})
    
    def apply(self, image_handler):
        """
        Apply resize filter to image.
        
        Args:
            image_handler: ImageHandler object
            
        Returns:
            bool: Success status
        """
        if image_handler.get_data() is None:
            print("Error: Image not loaded")
            return False
        
        width = self.config.get('width')
        height = self.config.get('height')
        print(f"Applying ResizeFilter to {width}x{height}")
        return True


class EnhanceFilter(Filter):
    """
    Enhances image brightness/contrast.
    
    Attributes:
        config: Must contain 'level' key for enhancement level
    """
    
    def __init__(self, level=1.0):
        """
        Initialize EnhanceFilter.
        
        Args:
            level (float): Enhancement level (1.0 = no change)
        """
        super().__init__({'level': level})
    
    def apply(self, image_handler):
        """
        Apply enhance filter to image.
        
        Args:
            image_handler: ImageHandler object
            
        Returns:
            bool: Success status
        """
        if image_handler.get_data() is None:
            print("Error: Image not loaded")
            return False
        
        level = self.config.get('level', 1.0)
        print(f"Applying EnhanceFilter with level={level}")
        return True
