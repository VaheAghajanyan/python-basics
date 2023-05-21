class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def speak(self):
        print("Dog barks")

dog = Dog("Buddy", "Labrador")
print(dog.name)  # Output: Buddy
dog.speak()  # Output: Dog barks

class Parent:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, {self.name}!")

class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

    def greet(self):
        super().greet()
        print(f"You are {self.age} years old.")

child = Child("Alice", 10)
child.greet()