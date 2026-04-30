"""
Pipeline module - Contains FilterPipeline for managing filter sequences.
Chapter 2 Concepts: Classes with list attributes, methods for list manipulation, composition.
"""


class FilterPipeline:
    """
    Manages an ordered sequence of filters to be applied to an image.
    
    Attributes:
        _filters: Internal list of Filter objects (soft privacy)
    """
    
    def __init__(self):
        """Initialize FilterPipeline with empty filter list."""
        self._filters = []
    
    def add_filter(self, filter_obj):
        """
        Add a filter to the pipeline.
        
        Args:
            filter_obj (Filter): Filter object to add
            
        Returns:
            self: For method chaining
        """
        self._filters.append(filter_obj)
        print(f"Added {filter_obj.__class__.__name__} to pipeline")
        return self
    
    def get_filters(self):
        """
        Get list of filters in pipeline.
        
        Returns:
            list: Copy of filters list
        """
        return self._filters.copy()
    
    def execute(self, image_handler):
        """
        Execute all filters in sequence on the image.
        
        Args:
            image_handler: ImageHandler object to process
            
        Returns:
            bool: Success status
        """
        print(f"\nExecuting pipeline with {len(self._filters)} filter(s)...")
        
        for i, filter_obj in enumerate(self._filters, 1):
            print(f"Step {i}: {filter_obj.__class__.__name__}")
            result = filter_obj.apply(image_handler)
            if not result:
                print(f"Error: Filter {filter_obj.__class__.__name__} failed")
                return False
        
        print("Pipeline execution completed successfully\n")
        return True
    
    def clear(self):
        """Remove all filters from pipeline."""
        self._filters.clear()
        print("Pipeline cleared")
    
    def count(self):
        """
        Get the number of filters in pipeline.
        
        Returns:
            int: Number of filters
        """
        return len(self._filters)
