# ----------------------------------------
# Assignment 1: Design Your Own Class 🏗️
# ----------------------------------------

# Base class
class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def info(self):
        return f"{self.brand} {self.model}"

# Derived class (Smartphone inherits from Device)
class Smartphone(Device):
    def __init__(self, brand, model, storage, battery_life):
        super().__init__(brand, model)  # Call parent constructor
        self.storage = storage
        self.battery_life = battery_life
        self.__secret_code = "1234"  # encapsulated (private) attribute
    
    def call(self, number):
        print(f"📱 Calling {number} from {self.info()}...")

    def charge(self):
        print(f"🔋 {self.info()} is charging. Battery life: {self.battery_life} hours.")
    
    # Encapsulation example (controlled access to private attribute)
    def unlock(self, code):
        if code == self.__secret_code:
            print(f"🔓 {self.info()} unlocked ✅")
        else:
            print(f"❌ Incorrect code for {self.info()}")

# Create Smartphone objects
phone1 = Smartphone("Apple", "iPhone 15", "256GB", 24)
phone2 = Smartphone("Samsung", "Galaxy S23", "512GB", 30)

# Use Smartphone methods
print("\n--- Smartphone Demo ---")
phone1.call("0722000000")
phone2.charge()
phone1.unlock("1234")
phone2.unlock("9999")


# ----------------------------------------
# Activity 2: Polymorphism Challenge 🎭
# ----------------------------------------

class Vehicle:
    def move(self):
        pass  # abstract method (to be overridden by subclasses)

class Car(Vehicle):
    def move(self):
        print("🚗 Driving on the road...")

class Plane(Vehicle):
    def move(self):
        print("✈️ Flying in the sky...")

class Boat(Vehicle):
    def move(self):
        print("🚤 Sailing across the water...")

# Polymorphism in action
print("\n--- Vehicle Polymorphism Demo ---")
vehicles = [Car(), Plane(), Boat()]

for v in vehicles:
    v.move()
