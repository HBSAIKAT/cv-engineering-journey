# Inheritance in Object-Oriented Programming

## What is Inheritance?

Inheritance is the **"is a" relationship**. It allows one class to inherit attributes and methods from another class—think of it like a family tree where you inherit traits from your parents.

**In object-oriented terms:** Instead of saying "a player *has* artificial intelligence" or "is associated with" a human, we say **"Deep Blue is a player"** or **"Gary Kasparov is a player."**

---

## The Chess Piece Example

A chess set has 32 pieces but only **6 types**: Pawn, Rook, Bishop, Knight, King, and Queen.

Rather than defining each piece class from scratch, they all inherit from a base **`Piece`** class:

- **Base class (`Piece`)** defines shared attributes:
  - `color` (black or white)
  - `chess_set` (which set it belongs to)

- **Subclasses** (Pawn, Rook, etc.) inherit these attributes and each define their own:
  - `shape` (how it looks on the board)
  - `move()` method (how it moves)

This avoids repeating code for color and chess_set 32 times.

---

## Method Overriding

**Subclasses can override parent methods** with their own implementation.

**How it works:**
- The `Piece` class can provide a default `move()` method (e.g., throws an error: "That piece cannot be moved")
- Each subclass—Knight, Rook, Pawn—overrides `move()` with its own logic
- The board doesn't need to know which piece type it's dealing with; it just calls `move()` and the right behavior happens

**Real-world analogy:** A `Player` class has a `calculate_move()` method. A `BeginnerPlayer` subclass might randomly choose a move, while a `DeepBluePlayer` subclass calculates the optimal move. The chess board treats both the same way—it just asks for the move.

---

## Abstract Classes & Abstract Methods

Sometimes it doesn't make sense to provide a default implementation of a method.

**Abstract class:** A template that cannot be instantiated directly.

**Abstract method:** Declares that a method *must* exist in any non-abstract subclass, but provides no implementation.

**Chess example:** The `Piece` class could declare `move()` as abstract, meaning:
- Every subclass (Rook, Bishop, Pawn, etc.) **must** provide a `move()` method
- If you try to create a new piece (like "Wizard") without a `move()` method, the code will fail
- This enforces your design rules

---

## Interfaces

An **interface** is the most abstract type of class:
- It declares what methods must exist
- It provides **zero** implementation
- It's a pure contract: "If you claim to implement this interface, you must have all these methods"

---

## Why Inheritance Matters

Inheritance gives you:
1. **Code reuse** — shared attributes and methods don't need to be repeated
2. **Specialized behavior** — subclasses can implement methods specific to their needs
3. **Flexibility** — add new piece types (like Wizard) without changing existing code
4. **Design enforcement** — abstract classes and interfaces ensure subclasses follow the required pattern

---

## Polymorphism

**Definition:** The ability to treat a class differently depending on which subclass is implemented.

The chess board doesn't need to know whether it's moving a Knight, Pawn, Rook, or Bishop. It just calls `move()` on the piece, and the correct subclass automatically handles it.

Board.move(piece) → calls piece.move()
↙ ↓ ↘
Knight Pawn Rook
(L-shaped) (1 square) (straight)


This is the real power of inheritance: **write once, work with many subclasses.**

---

## Duck Typing (Python's Superpower)

Python takes polymorphism even further. You don't need inheritance at all.

**"If it walks like a duck or swims like a duck, it's a duck."**

A Python board could call `move()` on **anything** with a `move()` method:
- A Bishop (inherits from Piece)
- A Car (completely unrelated class)
- A Duck (from the zoo)

When `move()` is called, each does its own thing:
- Bishop moves diagonally on the board
- Car drives someplace
- Duck swims or flies (depending on mood)

**Why this matters:** Future designers can create completely new behaviors—like a penguin that walks and swims—without needing to inherit from a base class or even thinking about the original design. As long as it has the right method, it works.

---

## Multiple Inheritance

A subclass can inherit from **more than one parent class**.

**Example that works well:**
- A `ScannerFax` class inherits from both `Scanner` and `Faxer`
- Clear, non-overlapping behaviors

**Example that gets messy:**
- A `Motorcycle` class has a `move()` method (drives on land)
- A `Boat` class has a `move()` method (drives on water)
- Now create `AmphibiousVehicle` inheriting from both
- **Problem:** Which `move()` gets called? How do we merge two conflicting behaviors?

**The practical answer:** **Avoid it.** If you find yourself in this situation, step back and redesign. Use composition, aggregation, or other patterns instead. The problem usually means you're thinking about the design wrong.

---

## When NOT to Use Inheritance

⚠️ **The hammer metaphor:** Owning a hammer doesn't turn screws into nails.

Inheritance is powerful and popular, but it's often **overused**.

**Common mistake:** Using inheritance just to share code between unrelated objects.

**Red flag:** "These two classes both need X, so we'll inherit from a common parent"—even though there's no real **"is a"** relationship.

**Better approach:** Ask yourself:
- Is there a clear **"is a"** relationship? (Pawn *is a* Piece ✓)
- Or is it just code reuse? (Class A and Class B both need `log()` — maybe use composition instead)

**Key principle:** Inheritance works best for **obvious** type hierarchies. For everything else, consider:
- Composition ("has a")
- Aggregation ("contains")
- Mixins or other design patterns

---

## Inheritance Provides Abstraction

Inheritance is fundamentally about **abstraction**: hiding unnecessary details and revealing only what matters.

- The Board doesn't care *how* a Pawn moves, only that it can `move()`
- Python's duck typing takes this further: the Board doesn't care *what* the piece is, only that it responds to `move()`
- Abstract classes enforce the contract: "All Pieces must have a `move()` method"

**Bottom line:** Inheritance lets you abstract away the differences between similar objects and treat them uniformly. That's its real power.

---

## Summary

| Concept | What It Is | When to Use |
|---------|-----------|------------|
| **Inheritance** | "is a" relationship | Clear type hierarchies (Pawn is a Piece) |
| **Polymorphism** | Treat subclasses as parent | Reduces code that depends on type |
| **Duck typing** | Any object with the method works | Flexibility; don't need inheritance |
| **Multiple inheritance** | Inherit from 2+ parents | Rarely; usually a design smell |
| **Abstract classes** | Enforce required methods | When subclasses must implement something |

**Remember:** Inheritance is powerful but easy to abuse. When in doubt, ask: "Is there a real *is a* relationship?" If not, consider other design patterns.