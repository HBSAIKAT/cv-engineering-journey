# Specifying Attributes and Behaviors - Notes

## What is an Object Instance?

An **object instance** is a specific object with its own set of data and behaviors.
- Example: The three oranges on your table are three separate instances of the "Orange" class
- Each instance has its own data values (weights, origins, etc.)
- All instances share the same class blueprint and available behaviors

---

## Attributes: The Data

**Attributes** (also called **members** or **properties**) describe the individual characteristics of an object.

### How Attributes Work

- **Class defines attributes:** "All Oranges have a weight"
- **Each instance has values:** Orange #1 weighs 150g, Orange #2 weighs 160g
- **Attributes can be shared:** Two different customers might both have the same first name

### Attributes in Our Fruit Example

| Class  | Attributes |
|--------|-----------|
| Orange | Weight, Orchard, Date_Picked |
| Apple  | Color, Weight |
| Basket | Location, Oranges (list of oranges in it) |
| Barrel | Size, Apples (list of apples in it) |

### Specifying Attribute Types

Attributes can have types (optional at the design stage):
Orange
+Weight: float
+Orchard: string
+Date_Picked: date
+basket: Basket


**Common types:**
- **Primitives:** int, float, string, boolean, byte
- **Data structures:** list, tree, graph
- **Other classes:** basket: Basket (an orange contains a reference to a Basket)

### A Design Note

Implementation-specific types (ArrayList vs. LinkedList, list vs. tuple) are chosen during programming, not design. At the design stage, just say "list"—let the programmer pick the specific implementation for their language.

### Implicit Attributes from Associations

Associations can be represented as attributes:
- An Orange "goes in" a Basket → the Orange has an implicit `basket` attribute
- A Basket "contains" Oranges → the Basket has an implicit `oranges: list` attribute

---

## Behaviors: The Actions

**Behaviors** are actions that can occur on an object. In code, behaviors are called **methods**.

### Methods vs. Functions

- **Functions (structured programming):** Stand-alone code that does something
- **Methods (object-oriented):** Functions that live in a class and have automatic access to all the object's data

### Method Structure

A method has three parts:
1. **Name:** What it does
2. **Parameters:** Data passed in (from the calling object) to use
3. **Return value:** The result of the method

### Methods in Our Fruit Example

#### Orange Methods
- **`pick(basket: Basket)`**
  - Takes a basket as a parameter
  - Updates the orange's `basket` attribute
  - Adds the orange to the basket's `oranges` list

- **`squeeze()`**
  - Returns the amount of juice extracted
  - Removes the orange from its basket

#### Basket Methods
- **`sell(customer: Customer)`**
  - Takes a customer as a parameter
  - Updates accounting/inventory records

- **`discard()`**
  - Removes the basket from inventory (goes bad)

#### Apple Methods
- (Not specified yet—but could include `pick()`, `peel()`, `store()`, etc.)

#### Barrel Methods
- (Not specified yet—but could include `fill()`, `ship()`, `discard()`, etc.)

---

## How It All Comes Together: The UML Class Diagram
Orange Basket
+Weight: float +location: string
+oranges: list
+Orchard: string +sell(customer: Customer)
+Date_Picked: date +discard()
+basket: Basket
+pick(basket: Basket)
+squeeze(): amount_of_juice

Basket
+location: string
+oranges: list
+sell(customer: Customer)
+discard()

    goes in
    *  ————→  1
    
    (Many oranges go in one basket)


---

## Object-Oriented Systems: How It Works

**The Big Picture:**
1. **Objects interact with each other** by calling methods and sharing data
2. **Each object is an instance of a class** that defines its structure and behavior
3. **Shared state:** Objects of the same class have the same attributes and methods, but different data values
4. **Different reactions:** Two oranges might respond differently to `squeeze()` depending on their ripeness

**Example of interaction:**
Orange instance #1 calls: pick(basket_A)
↓
Basket_A is updated to contain Orange #1
Orange #1's basket attribute now points to Basket_A
↓
System is now in a consistent state with interconnected objects


---

## Key Takeaway

- **Attributes** define what data an object holds (can specify types)
- **Methods** define what actions an object can perform (with parameters and return values)
- **Together** they create a system of interacting objects, each with its own state
- **The design challenge:** Figure out what objects you need and how they should interact

Object-oriented analysis and design is fundamentally about identifying these objects and designing clean, intuitive interactions between them.