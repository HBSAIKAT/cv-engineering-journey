# Introduction to Object-Oriented Programming - Notes

## What is an Object?

**Real-world analogy:** Objects are like toys a baby plays with—tangible things that do stuff.
- A bell rings (behavior)
- A button presses (behavior)
- A lever pulls (behavior)

**In software:** Objects aren't physical, but they model things that have properties and can perform actions.
- **Formal definition:** A collection of data + associated behaviors

## What Does "Object-Oriented" Mean?

**Oriented** = directed toward  
**Object-oriented** = functionally directed at modeling objects

It's a technique for handling complex systems by describing how objects interact through their data and behaviors.

---

## The OO Development Stages

There are three main phases in object-oriented software development:

### 1. Object-Oriented Analysis (OOA)
- **Focus:** What needs to be done?
- **Task:** Look at a problem and identify objects + their interactions
- **Output:** A set of requirements

*Example:* "I need a website" → requirements like:
- Users can review history
- Users can apply for jobs
- Users can browse and order products

*Note:* It's more like exploration than analysis—we discover what fits where.

### 2. Object-Oriented Design (OOD)
- **Focus:** How should things be done?
- **Task:** Convert requirements into an implementation specification
- **Activities:** Name objects, define behaviors, specify which objects can trigger which behaviors
- **Output:** Classes and interfaces (language-agnostic)

### 3. Object-Oriented Programming (OOP)
- **Focus:** Building the actual working program
- **Task:** Convert the design into code that does exactly what was requested
- **Output:** A functioning application

---

## Reality Check: Iterative Development

In theory, these three stages happen in perfect order.

**In reality?** Not quite.

Most modern software development uses **iterative development:**
- Build a small feature → design it → code it
- Review and test
- Repeat with improvements and new features
- Short development cycles instead of one big waterfall

**What happens in practice:**
- While designing, we find things that need re-analysis
- While coding, we find gaps in the design
- It's messier than textbooks suggest, but more flexible

---

## Key Takeaway

Object-oriented development is about modeling complex systems as collections of interacting objects, each with data and behaviors. The process isn't strictly linear—it's iterative, practical, and evolves as we build.