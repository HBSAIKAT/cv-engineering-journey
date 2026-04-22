# Hiding Details and Creating the Public Interface - Notes

## The Public Interface

**Public Interface:** The collection of attributes and methods that other objects can access to interact with an object.

Key principle: Other objects don't need to know (or are not allowed to know) the internal workings.

### Real-World Example: Television

- **What we interact with:** Remote control (the interface)
- **What we don't care about:** Whether the signal comes from antenna, cable, or satellite
- **What we don't access:** Internal circuitry (voiding the warranty)

The TV works the same way regardless of internal implementation—that's the power of a well-designed interface.

---

## Information Hiding vs. Encapsulation

These terms are often used interchangeably, but there's a subtle distinction:

### **Encapsulation**
- Creating a "capsule" that bundles data and behavior together
- Like a time capsule: everything is contained in one package
- **Encapsulated data doesn't have to be hidden**

### **Information Hiding**
- Hiding the implementation details from the outside world
- Restricting access to internal workings
- **Hides what's inside the capsule**

### The Relationship
Time capsule (unlocked, clear plastic):
→ Encapsulated (everything bundled together)
→ NOT information hiding (we can see inside)

Time capsule (locked, buried):
→ Encapsulated (everything bundled together)
→ Information hiding (we can't see or access inside)


**For Python programmers:** Python doesn't enforce true information hiding, so we use the broader definition: encapsulation = bundling data and behavior together with a controlled public interface.

---

## Why the Public Interface Matters

### Hard to Change Later
- Once other objects depend on your interface, changing it breaks their code
- Renaming a public attribute? Every client object needs updating
- Changing method parameters? All callers need modification

### Easy to Improve Internally
- Keep the interface the same
- Change how it works internally (more efficient, access network data, etc.)
- Client objects don't need to know or change

**The contract:** Objects promise to maintain their public interface, but reserve the right to change internals.

### Design Principle: Keep It Simple
- Design interfaces based on **how easy they are to use**, not how hard they are to code
- This applies to user interfaces too
- A slightly harder implementation is worth a much better interface

---

## Abstraction: Dealing with Appropriate Detail Levels

**Abstraction** = dealing with the level of detail appropriate to the task.

It's the process of:
1. Extracting a public interface from inner details
2. Focusing on what matters for the current purpose
3. Ignoring irrelevant complexity

### Real-World Example: A Car

**Driver's abstraction level:**
Car (Driver's view)
+steer()
+change_gears()
+apply_brake()


The driver cares about:
- Steering
- Gear changes
- Braking

The driver doesn't care about:
- Motor workings
- Drive train mechanics
- Brake system details

**Mechanic's abstraction level:**
Car (Mechanic's view)
+disc_brakes
+fuel_injected_engine
+automatic_transmission
+adjust_brake()
+change_oil()


The mechanic cares about:
- Engine tuning
- Oil changes
- Brake adjustments

**Same object, two different interfaces at two different abstraction levels.**

### Models Are Abstractions

Remember: Your program objects are **models**, not real objects.

A model car:
- Looks like a 1956 Thunderbird
- Doesn't actually run
- Driveshaft doesn't turn
- These details were irrelevant at the time you built it

**The power of modeling:** You can ignore irrelevant details and focus on what matters for your purpose.

---

## Putting It All Together: Encapsulation + Information Hiding + Abstraction

**In one sentence:** Encapsulation is bundling data and behavior, information hiding restricts access, and abstraction determines what details are relevant.

**Practical definition for OOP:** Design separate **public** and **private** interfaces. Make the public interface simple, clean, and appropriate for the task. Keep internal details hidden and changeable.

---

## Naming Guidelines for Clear Interfaces

When designing objects, use natural language cues:

| What It Is | Part of Speech | Example |
|-----------|----------------|---------|
| Class/Object | Noun | Orange, Basket, Customer |
| Method/Behavior | Verb | pick(), squeeze(), sell(), discard() |
| Attribute/Property | Adjective (or noun if reference) | weight, color, size, location |

**Why this matters:** Code becomes self-documenting. You can read `orange.squeeze()` and immediately understand what's happening.

---

## Best Practices for Designing Public Interfaces

### 1. **Model Only What You Need**
- Don't add "future-proofing" features you don't need yet
- Model exactly what the current system requires
- The design will naturally reach appropriate abstraction

### 2. **Think About Future Requirements**
- Design interfaces to be open-ended
- Make them flexible enough for future changes
- But don't over-engineer for hypothetical scenarios

### 3. **Use the Privacy Principle**
Think of your object as having strong privacy preferences:

> Don't let other objects access your data unless it's in your best interest.  
> Don't give them methods to force you to do things unless you're certain they should be able to.

**In practice:** Ask yourself:
- Does this attribute really need to be public?
- Should other objects be able to call this method?
- What's the minimum interface needed for other objects to use this object?

### 4. **Consistency and Clarity**
- Use sensible, consistent names
- Make methods do one thing
- Keep interfaces simple and intuitive

---

## The Big Picture: Why This Matters

**Good interface design enables:**
- ✓ Easy collaboration (objects interact predictably)
- ✓ Maintainability (you can change internals without breaking other code)
- ✓ Reusability (clear interfaces make objects useful in different contexts)
- ✓ Testing (you know exactly what to test from the outside)
- ✓ Understanding (others can use your object without reading internals)

**Bad interface design causes:**
- ✗ Tight coupling (changes ripple everywhere)
- ✗ Hard to maintain (touching internals breaks unpredictable things)
- ✗ Confusing APIs (unclear what methods do or what they need)
- ✗ Difficult testing (can't isolate what's being tested)

---

## Key Takeaway

The public interface is the contract between an object and the outside world. Design it carefully, keep it simple, and hide implementation details. This separation of concerns is one of object-oriented programming's greatest strengths—it lets you build complex systems from simple, understandable pieces.