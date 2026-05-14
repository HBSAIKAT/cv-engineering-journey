# Case Study: Real Estate Application

## Project Overview

A real estate agent management system to:
- Manage properties available for purchase or rent
- Handle two property types: apartments and houses
- Allow agents to enter property details
- List all available properties
- Mark properties as sold or rented

**Key design principle:** Focus on OOP, not GUI/web overhead. The skills learned apply to GUI and web frameworks.

---

## Class Hierarchy Design

The system uses inheritance and multiple inheritance to share behavior:

```
Agent
├── Property (base class)
│   ├── House
│   │   ├── HouseRental (Rental + House)
│   │   └── HousePurchase (Purchase + House)
│   └── Apartment
│       ├── ApartmentRental (Rental + Apartment)
│       └── ApartmentPurchase (Purchase + Apartment)
├── Rental (mixin-like)
└── Purchase (mixin-like)
```

### Design Decision: Inheritance Over Composition

**Problem:** Need to represent Rental and Purchase behaviors combined with House and Apartment.

**Options:**
1. Composition — Create Rental and Purchase objects inside properties (cleaner but more complex)
2. Multiple inheritance — Create combined classes like HouseRental, HousePurchase (our choice)

We chose multiple inheritance to explore inheritance patterns, though composition might be better in production.

---

## Property Class (Base)

```python
class Property:
    def __init__(self, square_feet='', bedrooms='',
                 bathrooms='', **kwargs):
        super().__init__(**kwargs)
        self.square_feet = square_feet
        self.bedrooms = bedrooms
        self.bathrooms = bathrooms
    
    def display(self):
        print("PROPERTY DETAILS")
        print("================")
        print("square footage: {}".format(self.square_feet))
        print("bedrooms: {}".format(self.bedrooms))
        print("bathrooms: {}".format(self.bathrooms))
    
    def prompt_init():
        return dict(
            square_feet=input("Enter the square feet: "),
            bedrooms=input("Enter number of bedrooms: "),
            bathrooms=input("Enter number of baths: "))
    
    prompt_init = staticmethod(prompt_init)
```

**Key features:**
- Base attributes: square footage, bedrooms, bathrooms
- `display()` method for showing property details
- Static `prompt_init()` method to get user input without needing an instance

---

## Apartment Class

```python
class Apartment(Property):
    valid_laundries = ("coin", "ensuite", "none")
    valid_balconies = ("yes", "no")
    
    def __init__(self, balcony='', laundry='', **kwargs):
        super().__init__(**kwargs)
        self.balcony = balcony
        self.laundry = laundry
    
    def display(self):
        super().display()
        print("APARTMENT DETAILS")
        print("laundry: {}".format(self.laundry))
        print("has balcony: {}".format(self.balcony))
    
    def prompt_init():
        parent_init = Property.prompt_init()
        laundry = get_valid_input(
            "What laundry facilities does the property have? ",
            Apartment.valid_laundries)
        balcony = get_valid_input(
            "Does the property have a balcony? ",
            Apartment.valid_balconies)
        parent_init.update({
            "laundry": laundry,
            "balcony": balcony
        })
        return parent_init
    
    prompt_init = staticmethod(prompt_init)
```

**Key features:**
- Extends Property with apartment-specific attributes
- `prompt_init()` calls parent's prompt, then adds apartment-specific prompts
- Uses `dict.update()` to merge dictionaries

---

## Validation Helper Function

Instead of using inheritance for validation, use a module-level function. This avoids unnecessary class overhead:

```python
def get_valid_input(input_string, valid_options):
    input_string += " ({}) ".format(", ".join(valid_options))
    response = input(input_string)
    while response.lower() not in valid_options:
        response = input(input_string)
    return response
```

**Why not inheritance?** Validation doesn't need instance state, so it doesn't belong in a class. A simple function is cleaner and more reusable.

### Testing the Function

```python
>>> get_valid_input("what laundry?", ("coin", "ensuite", "none"))
what laundry? (coin, ensuite, none) hi
what laundry? (coin, ensuite, none) COIN
'COIN'
```

---

## House Class

```python
class House(Property):
    valid_garage = ("attached", "detached", "none")
    valid_fenced = ("yes", "no")
    
    def __init__(self, num_stories='', garage='',
                 fenced='', **kwargs):
        super().__init__(**kwargs)
        self.num_stories = num_stories
        self.garage = garage
        self.fenced = fenced
    
    def display(self):
        super().display()
        print("HOUSE DETAILS")
        print("# of stories: {}".format(self.num_stories))
        print("garage: {}".format(self.garage))
        print("fenced yard: {}".format(self.fenced))
    
    def prompt_init():
        parent_init = Property.prompt_init()
        fenced = get_valid_input(
            "Is the yard fenced? ",
            House.valid_fenced)
        garage = get_valid_input(
            "Is there a garage? ",
            House.valid_garage)
        num_stories = input("How many stories? ")
        parent_init.update({
            "fenced": fenced,
            "garage": garage,
            "num_stories": num_stories
        })
        return parent_init
    
    prompt_init = staticmethod(prompt_init)
```

---

## Rental Class (Mixin)

```python
class Rental:
    def __init__(self, furnished='', utilities='',
                 rent='', **kwargs):
        super().__init__(**kwargs)
        self.furnished = furnished
        self.rent = rent
        self.utilities = utilities
    
    def display(self):
        super().display()
        print("RENTAL DETAILS")
        print("rent: {}".format(self.rent))
        print("estimated utilities: {}".format(self.utilities))
        print("furnished: {}".format(self.furnished))
    
    def prompt_init():
        return dict(
            rent=input("What is the monthly rent? "),
            utilities=input("What are the estimated utilities? "),
            furnished=get_valid_input(
                "Is the property furnished? ",
                ("yes", "no")))
    
    prompt_init = staticmethod(prompt_init)
```

**Note:** Doesn't inherit from Property, but calls `super().__init__(**kwargs)` because it will be combined with Property via multiple inheritance.

---

## Purchase Class (Mixin)

```python
class Purchase:
    def __init__(self, price='', taxes='', **kwargs):
        super().__init__(**kwargs)
        self.price = price
        self.taxes = taxes
    
    def display(self):
        super().display()
        print("PURCHASE DETAILS")
        print("selling price: {}".format(self.price))
        print("estimated taxes: {}".format(self.taxes))
    
    def prompt_init():
        return dict(
            price=input("What is the selling price? "),
            taxes=input("What are the estimated taxes? "))
    
    prompt_init = staticmethod(prompt_init)
```

---

## Combined Classes (Multiple Inheritance)

### HouseRental

```python
class HouseRental(Rental, House):
    def prompt_init():
        init = House.prompt_init()
        init.update(Rental.prompt_init())
        return init
    
    prompt_init = staticmethod(prompt_init)
```

**Magic:** No `__init__` or `display()` method needed! Both parent classes call `super()`, so the methods chain correctly.

### Testing HouseRental

```python
>>> init = HouseRental.prompt_init()
Enter the square feet: 1
Enter number of bedrooms: 2
Enter number of baths: 3
Is the yard fenced? (yes, no) no
Is there a garage? (attached, detached, none) none
How many stories? 4
What is the monthly rent? 5
What are the estimated utilities? 6
Is the property furnished? (yes, no) no

>>> house = HouseRental(**init)
>>> house.display()
PROPERTY DETAILS
================
square footage: 1
bedrooms: 2
bathrooms: 3
HOUSE DETAILS
# of stories: 4
garage: none
fenced yard: no
RENTAL DETAILS
rent: 5
estimated utilities: 6
furnished: no
```

### Inheritance Order Matters!

**Wrong order:** `class HouseRental(House, Rental)`

```python
house.display()
# Calls House.display() → calls super() → Property.display()
# Property.display() does NOT call super()
# Result: Rental.display() NEVER CALLED!
```

**Correct order:** `class HouseRental(Rental, House)`

```python
house.display()
# Calls Rental.display() → calls super() → House.display()
# → calls super() → Property.display()
# Result: All three display methods called!
```

**Lesson:** Order classes so the one with `super()` calls comes first.

---

## Other Combined Classes

```python
class ApartmentRental(Rental, Apartment):
    def prompt_init():
        init = Apartment.prompt_init()
        init.update(Rental.prompt_init())
        return init
    prompt_init = staticmethod(prompt_init)

class ApartmentPurchase(Purchase, Apartment):
    def prompt_init():
        init = Apartment.prompt_init()
        init.update(Purchase.prompt_init())
        return init
    prompt_init = staticmethod(prompt_init)

class HousePurchase(Purchase, House):
    def prompt_init():
        init = House.prompt_init()
        init.update(Purchase.prompt_init())
        return init
    prompt_init = staticmethod(prompt_init)
```

All follow the same pattern: call parent's `prompt_init()`, update with own values.

---

## Agent Class

### Type Mapping

```python
class Agent:
    type_map = {
        ("house", "rental"): HouseRental,
        ("house", "purchase"): HousePurchase,
        ("apartment", "rental"): ApartmentRental,
        ("apartment", "purchase"): ApartmentPurchase
    }
```

**Clever design:** Dictionary maps (property_type, payment_type) tuples to class objects. Classes can be stored and passed around like normal objects!

### Display Properties

```python
def __init__(self):
    self.property_list = []

def display_properties(self):
    for property in self.property_list:
        property.display()
```

Polymorphism in action: Each property's `display()` method runs without Agent knowing the specific type.

### Add Property

```python
def add_property(self):
    property_type = get_valid_input(
        "What type of property? ",
        ("house", "apartment")).lower()
    payment_type = get_valid_input(
        "What payment type? ",
        ("purchase", "rental")).lower()
    PropertyClass = self.type_map[
        (property_type, payment_type)]
    init_args = PropertyClass.prompt_init()
    self.property_list.append(PropertyClass(**init_args))
```

**Process:**
1. Get property type and payment type from user
2. Look up correct class in `type_map`
3. Call `prompt_init()` on that class to get user input
4. Use `**dict` syntax to convert dict to keyword arguments
5. Instantiate the correct class and add to list

---

## Demo Session

```python
>>> agent = Agent()
>>> agent.add_property()
What type of property? (house, apartment) house
What payment type? (purchase, rental) rental
Enter the square feet: 900
Enter number of bedrooms: 2
Enter number of baths: one and a half
Is the yard fenced? (yes, no) yes
Is there a garage? (attached, detached, none) detached
How many stories? 1
What is the monthly rent? 1200
What are the estimated utilities? included
Is the property furnished? (yes, no) no

>>> agent.add_property()
What type of property? (house, apartment) apartment
What payment type? (purchase, rental) purchase
Enter the square feet: 800
Enter number of bedrooms: 3
Enter number of baths: 2
What laundry facilities does the property have? (coin, ensuite, one) ensuite
Does the property have a balcony? (yes, no, solarium) yes
What is the selling price? $200,000
What are the estimated taxes? 1500

>>> agent.display_properties()
PROPERTY DETAILS
================
square footage: 900
bedrooms: 2
bathrooms: one and a half
HOUSE DETAILS
# of stories: 1
garage: detached
fenced yard: yes
RENTAL DETAILS
rent: 1200
estimated utilities: included
furnished: no
PROPERTY DETAILS
================
square footage: 800
bedrooms: 3
bathrooms: 2
APARTMENT DETAILS
laundry: ensuite
has balcony: yes
PURCHASE DETAILS
selling price: $200,000
estimated taxes: 1500
```

---

## Design Patterns Used

1. **Inheritance** — Property → House, Apartment
2. **Multiple inheritance** — Rental/Purchase + House/Apartment
3. **Static methods** — `prompt_init()` for user input without instances
4. **Polymorphism** — `display()` works on any property type
5. **Type mapping** — Dictionary maps tuples to classes
6. **Dictionary unpacking** — `**kwargs` for flexible initialization
7. **Helper functions** — `get_valid_input()` for validation

---

## Key OOP Principles Demonstrated

✓ **Inheritance** — Share common behavior (Property base class)  
✓ **Method overriding** — Each class customizes `display()` and `prompt_init()`  
✓ **Super()** — Call parent methods to build behavior chain  
✓ **Polymorphism** — Agent doesn't care what property type; just calls methods  
✓ **Static methods** — Input gathering without instance state  
✓ **Multiple inheritance** — Combine rental/purchase with house/apartment  
✓ **Encapsulation** — Property details hidden; Agent uses simple interface  
✓ **DRY (Don't Repeat Yourself)** — `get_valid_input()` avoids code duplication  

---

## Extensibility

To add new features:

- **Condo class** — Inherit from Property, add condo-specific attributes
- **Lease option** — Add LeasePurchase mixin
- **Commercial property** — Create new property type
- **Property editing** — Add `update_property()` method to Agent
- **Persistence** — Save/load properties from database

The design is flexible enough to accommodate these without major changes!