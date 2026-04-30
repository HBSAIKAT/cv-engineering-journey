"""
Demo module - Demonstrates Image Toolkit functionality.
Chapter 2 Concepts: Package imports, __name__ guard, module execution.
"""

from image_toolkit import (
    ImageHandler,
    BlurFilter,
    GrayscaleFilter,
    ResizeFilter,
    EnhanceFilter,
    FilterPipeline,
    RecipeManager
)


def main():
    """
    Main demo function showcasing Image Toolkit capabilities.
    Demonstrates:
        - Creating an ImageHandler
        - Building a filter pipeline
        - Executing filters
        - Saving and loading recipes
    """
    print("=" * 60)
    print("Image Toolkit - Chapter 2 Demo")
    print("=" * 60)
    print()
    
    # 1. Create an ImageHandler
    print("1. Creating ImageHandler...")
    image = ImageHandler("sample.jpg")
    print()
    
    # 2. Load the image
    print("2. Loading image...")
    image.load()
    print(f"   Image dimensions: {image.get_dimensions()}")
    print()
    
    # 3. Create a FilterPipeline and add filters
    print("3. Building filter pipeline...")
    pipeline = FilterPipeline()
    
    # Add individual filters using method chaining
    pipeline.add_filter(BlurFilter(radius=3)) \
            .add_filter(GrayscaleFilter()) \
            .add_filter(ResizeFilter(800, 600)) \
            .add_filter(EnhanceFilter(level=1.2))
    
    print(f"   Total filters in pipeline: {pipeline.count()}")
    print()
    
    # 4. Execute the pipeline
    print("4. Executing pipeline...")
    pipeline.execute(image)
    
    # 5. Save processed image
    print("5. Saving processed image...")
    image.save("output.jpg")
    print()
    
    # 6. Save pipeline as recipe
    print("6. Saving pipeline as recipe...")
    recipe_manager = RecipeManager(recipe_path="./recipes")
    recipe_manager.save(pipeline, "my_first_recipe")
    print()
    
    # 7. Demo: Load and use saved recipe
    print("7. Loading recipe and applying to new image...")
    new_image = ImageHandler("another_image.jpg")
    new_image.load()
    
    loaded_pipeline = recipe_manager.load("my_first_recipe")
    if loaded_pipeline:
        print(f"   Loaded pipeline with {loaded_pipeline.count()} filters")
        loaded_pipeline.execute(new_image)
    print()
    
    print("=" * 60)
    print("Demo completed!")
    print("=" * 60)


if __name__ == "__main__":
    main()
