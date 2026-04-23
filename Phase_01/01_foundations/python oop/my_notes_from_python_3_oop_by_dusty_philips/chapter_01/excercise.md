# Object Oriented Analysis(OOA),Object Oriented Design(OOD) and UML Diagram for Image-toolkit project

Image-Toolkit: Full Project Description
---------------------------------------
Image-Toolkit is a command-line Python application that loads image files, applies a configurable pipeline of image filters (blur, grayscale, resize, enhance, etc.), and saves the processed output. It is designed to handle single images and batch folders, support user-defined "filter recipes" saved as JSON, and process large workloads efficiently using multiprocessing.


Part: 01/ Object Oriented Analysis(OOA)
=======================================
## Actors
Actors are external entities that interact with the system:
* **User (CLI User)**: executes commands and provides necessary inputs (image path, recipe, and output location).
* **File System**: acts as the source for raw images and the destination for processed outputs.
* **JSON Recipe Storage**: stores reusable filter configurations and predefined processing logic.
* **OS/CPU Scheduler**: manages and executes the multiprocessing workers responsible for image processing.


## Use Case Analysis

### Use Case 1: Process Single Image
* User provides image path + filters/recipe
* System loads image
* Applies filter pipeline
* Saves output

### Use Case 2: Apply Recipe
* User selects a saved JSON recipe
* System reconstructs pipeline
* Applies filters in defined sequence

### Use Case 3: Batch Processing
* User provides folder path
* System loads all images
* Queues images
* Processes in parallel
* Saves outputs with naming strategy


### Use Case 4: Create / Save Recipe
* User defines filter sequence
* System serializes pipeline -> JSON


### Use Case 5: Load Recipe
* System deserializes JSON -> pipeline