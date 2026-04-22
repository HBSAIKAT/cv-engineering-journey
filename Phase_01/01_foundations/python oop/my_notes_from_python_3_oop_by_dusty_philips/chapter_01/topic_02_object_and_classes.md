# Objects and Classes - Notes

## Objects vs. Classes

**Object:** A specific instance of something—like one particular apple or orange.

**Class:** A blueprint or template that describes a *kind* of object.
- All objects of the same class share the same attributes and behaviors
- Example: You have 3 oranges on a table. Each is a distinct object, but all belong to the class "Orange"

**Analogy:** A class is like an architectural blueprint; an object is like an actual building built from that blueprint.
---
## Example: Fruit Farm Inventory
Imagine an inventory system for a fruit farm:
- **Apples** (class) → go in **Barrels** (class)
- **Oranges** (class) → go in **Baskets** (class)
This gives us 4 classes of objects to model.
---
## Relationships Between Classes: UML

**UML** = Unified Modeling Language (yes, it's a three-letter acronym)

### What is UML?
- A standard way to visually represent classes and their relationships
- Uses simple boxes and lines—intuitive to draw and understand
- Good for communication between programmers, designers, and managers
- Useful in brainstorming sessions and team discussions

### The Debate: Is UML Worth It?

**Pro:**
- Easy communication with non-programmers
- Quick and intuitive diagramming
- Useful for remembering *why* you made design decisions later
- Even anti-UML teams use informal versions in meetings

**Con:**
- In iterative development, diagrams become outdated quickly
- Maintaining formal specs can feel like wasted effort

**Reality:** Even if you don't maintain formal UML documents, sketching diagrams during design sessions is incredibly valuable.

---

## Association: The Basic Relationship

An **association** is the most basic way two classes relate to each other.

### Simple Association
Orange ——— Basket
Apple ——— Barrel


This shows: Oranges are associated with Baskets, Apples are associated with Barrels.

### Enhanced Association with Multiplicity
Orange ———— Basket
1

Apple ———— Barrel
1


**Multiplicity** (or **cardinality**) describes *how many* objects can be involved in a relationship:
- **\* (asterisk)** = many (zero or more)
- **1** = exactly one
- **0..1** = zero or one
- **2..5** = between 2 and 5, etc.

### How to Read Multiplicity

**The multiplicity nearest to a class tells you how many of that class can associate with one object on the other side.**

For the orange-basket relationship:
- **Reading left to right:** Many Oranges can go in exactly one Basket
- **Reading right to left:** One Basket holds many Oranges

For the apple-barrel relationship:
- **Reading left to right:** Many Apples can go in exactly one Barrel
- **Reading right to left:** One Barrel holds many Apples

### Direction and Arrows

UML diagrams often show arrows indicating the direction of the association:
Orange ——→ Basket (oranges GO IN baskets)
Apple ——→ Barrel (apples GO IN barrels)
This clarifies the relationship beyond just "somehow associated."
---

## UML Design Philosophy

**Everything in UML is optional.** You only specify as much detail as makes sense for your situation:
- **Quick whiteboard sketch?** Just draw boxes and lines
- **Formal design document?** Add multiplicity, directions, and labels
- **The key:** Use what helps your team communicate

---

## Key Takeaway

Classes are blueprints; objects are instances. UML class diagrams are a simple, visual way to show how classes relate to each other. Multiplicity tells you the constraints of those relationships. Even if you never create a formal UML document, sketching relationships helps clarify your design and communicates ideas to others.