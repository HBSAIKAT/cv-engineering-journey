# Composition Notes

## What is Composition?
Composition is collecting multiple objects together to create a new object. It's useful when one object is **part of** another object.

**Key insight:** Composition creates levels of abstraction — different interfaces can be exposed at different depths.

---

## Why Composition Matters
- **Physical examples** (cars, engines) are intuitive but don't transfer well to software
- **Computer objects** often represent abstract ideas (calls, titles, accounts, appointments) rather than physical things
- The challenge: identifying what should be composed in abstract systems

---

## Chess Game Example
A chess set is composed of:
- **1 Board** (which itself is composed of 64 positions)
- **32 Pieces** (which can potentially exist independently)

This decomposition helps us understand the system at different levels:
- High level: Two players interact with a chess set
- Mid level: Chess set contains board + pieces
- Deeper level: Board contains 64 individual positions

---

## Composition vs. Aggregation

| Aspect | Composition | Aggregation |
|--------|-------------|-------------|
| **Independence** | Parts cannot exist independently | Parts can exist independently |
| **Lifespan** | Parent controls creation/destruction of children | Children can outlive the parent |
| **Example** | Board **has** 64 positions | Chess set **has** 32 pieces |
| **UML** | Solid diamond | Hollow diamond |

**Important:** In practice, the distinction often doesn't matter during implementation — both behave similarly. The difference is useful for **team discussion and design clarity**.

---

## Key Takeaway
Composition (and its looser cousin aggregation) is one of two fundamental OOP principles for creating levels of abstraction. It's simpler than inheritance, so it's the natural starting point for object-oriented design.

The real skill: **recognizing what objects should be composed together** in abstract systems.