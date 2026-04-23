Library Catalog — OOP Design Notes
Chapter 1 Case Study | Object-Oriented Analysis & Design

1. Classes and Their Structure

LibraryItem (Abstract / Parent Class)
- title: Name of the book / media
- subject: Subject
- upc: Universal Product Code
- locate(): Returns where it is located (abstract)
- getInfo(): Returns general information

Book — extends LibraryItem
- isbn: Unique ID of the book
- ddsNumber: Dewey Decimal System number
- contributors: List<ContributorWithType>
- locate(): "Shelf " + ddsNumber

DVD — extends LibraryItem
- genre: Genre
- runtime: Length in minutes
- contributors: List<ContributorWithType>
- locate(): "Section " + genre

Magazine — extends LibraryItem
- volume: Volume number
- issue: Issue number
- publisher: Publisher
- locate(): "Vol." + volume + " #" + issue

Catalog (Manager Class)
- items: List<LibraryItem>
- searchByTitle(t)
- searchByAuthor(a)
- searchBySubject(s)
- addItem(item)

Important: Catalog only knows LibraryItem — not Book or DVD. This is Polymorphism.

Contributor
- name: Person's name
- bio: Short biography

ContributorWithType (Composition)
- contributor: Contributor object
- type: "Author" / "Actor" / "Director" / "Artist"

2. Inheritance Hierarchy

LibraryItem
 ├── Book
 ├── DVD
 ├── Magazine
 └── CD

3. Sequence Flow

User → Catalog → Items → locate() → return location → User

4. Refactoring

Bad Design:
Inheritance for roles (Author, Actor, etc.)

Good Design:
Composition using ContributorWithType

5. Key Takeaways

- Objects are tools, not rules
- Inheritance can create complexity if misused
- Composition is more flexible
- Polymorphism enables uniform interaction
