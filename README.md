Python OOP & Polymorphism

This project demonstrates fundamental Object-Oriented Programming (OOP) concepts in Python through two assignments:

1. Design Your Own Class (Smartphone Example)
2. Polymorphism Challenge (Vehicles Example)

---

🏗️ Assignment 1: Smartphone Class

We create a Smartphone class that inherits from a base class Device.
It demonstrates constructors, attributes, methods, encapsulation, and inheritance.

Key Features

* Attributes: brand, model, storage, battery life
* Encapsulation: private attribute \_\_secret\_code
* Methods:

  * info() → returns brand and model
  * call(number) → simulates making a call
  * charge() → simulates charging
  * unlock(code) → validates input against a private code

Example Usage

```python
phone1 = Smartphone("Apple", "iPhone 15", "256GB", 24)
phone1.call("0722000000")
phone1.charge()
phone1.unlock("1234")
```

Output

```
📱 Calling 0722000000 from Apple iPhone 15...
🔋 Apple iPhone 15 is charging. Battery life: 24 hours.
🔓 Apple iPhone 15 unlocked ✅
```

---

🎭 Assignment 2: Polymorphism with Vehicles

We create a Vehicle base class and override the move() method in subclasses:

* Car → "Driving 🚗"
* Plane → "Flying ✈️"
* Boat → "Sailing 🚤"

This demonstrates polymorphism where the same method name behaves differently depending on the object.

Example Usage

```python
vehicles = [Car(), Plane(), Boat()]
for v in vehicles:
    v.move()
```

Output

```
🚗 Driving on the road...
✈️ Flying in the sky...
🚤 Sailing across the water...
```

---

⚙️ How to Run

1. Ensure you have Python 3.x installed.
2. Save the script as assignment.py.
3. Run the script in your terminal:


python assignment.py




📚 Concepts Demonstrated

* Classes & Objects – Core building blocks of OOP
* Constructors (**init**) – Initializing objects with unique values
* Encapsulation – Protecting data with private attributes
* Inheritance – Smartphone inherits from Device
* Polymorphism – Different move() behaviors across Car, Plane, and Boat



🚀 Extensions (Optional)

* Make the script interactive (user inputs phone details or chooses a vehicle)
* Add more subclasses (e.g., Train.move() → "Chugging 🚂")
* Connect the Smartphone class with a simple contact list feature



✍️ Author: Geoffrey Ndungi Kimani


