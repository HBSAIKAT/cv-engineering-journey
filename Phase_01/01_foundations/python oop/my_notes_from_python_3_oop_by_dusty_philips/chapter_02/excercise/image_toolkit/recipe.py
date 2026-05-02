"""
Recipe module - Contains RecipeManager for saving and loading filter configurations.
Chapter 2 Concepts: File I/O, JSON handling, classes with __init__ and methods.
"""

import json
from .filters import BlurFilter, GrayscaleFilter, ResizeFilter, EnhanceFilter

class RecipeManager:
    """
    Manages saving and loading filter pipeline recipes as JSON.
    Attributes:
        recipe_path: Directory path for storing recipes
    """
    
    def __init__(self, recipe_path="./recipes"):
        """
        Initialize RecipeManager.
        Args:
            recipe_path (str): Directory path for recipe storage
        """
        self.recipe_path = recipe_path
    
    def save(self, pipeline, recipe_name):
        """
        Save a filter pipeline as a JSON recipe.
        Args:
            pipeline (FilterPipeline): Pipeline to save
            recipe_name (str): Name for the recipe (without .json)
            
        Returns:
            bool: Success status
        """
        filters = pipeline.get_filters()
        recipe_data = []
        
        for filter_obj in filters:
            filter_info = {
                'type': filter_obj.__class__.__name__,
                'config': filter_obj.config
            }
            recipe_data.append(filter_info)
        
        recipe_dict = {
            'name': recipe_name,
            'filters': recipe_data
        }
        
        try:
            file_path = f"{self.recipe_path}/{recipe_name}.json"
            with open(file_path, 'w') as f:
                json.dump(recipe_dict, f, indent=2)
            print(f"Recipe saved: {file_path}")
            return True
        except Exception as e:
            print(f"Error saving recipe: {e}")
            return False
    
    def load(self, recipe_name):
        """
        Load a filter pipeline from a JSON recipe.  
        Args:
            recipe_name (str): Name of recipe to load (without .json)
        Returns:
            FilterPipeline: Loaded pipeline or None if failed
        """
        try:
            file_path = f"{self.recipe_path}/{recipe_name}.json"
            with open(file_path, 'r') as f:
                recipe_dict = json.load(f)
            
            # Import pipeline here to avoid circular imports
            from .pipeline import FilterPipeline
            
            pipeline = FilterPipeline()
            
            for filter_info in recipe_dict.get('filters', []):
                filter_type = filter_info['type']
                config = filter_info['config']
                
                # Reconstruct filter based on type
                if filter_type == 'BlurFilter':
                    filter_obj = BlurFilter(radius=config.get('radius', 5))
                elif filter_type == 'GrayscaleFilter':
                    filter_obj = GrayscaleFilter()
                elif filter_type == 'ResizeFilter':
                    filter_obj = ResizeFilter(
                        width=config.get('width'),
                        height=config.get('height')
                    )
                elif filter_type == 'EnhanceFilter':
                    filter_obj = EnhanceFilter(level=config.get('level', 1.0))
                else:
                    print(f"Unknown filter type: {filter_type}")
                    continue
                
                pipeline.add_filter(filter_obj)
            
            print(f"Recipe loaded: {file_path}")
            return pipeline
            
        except Exception as e:
            print(f"Error loading recipe: {e}")
            return None
