# 91. Simple Class (Person): Create a class Person with attributes like name and age.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# 92. Class Methods: Add methods to the Person class (e.g., introduce()).
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."

# 93. Constructor: Use a constructor to initialize object attributes.
# (Already demonstrated in 91 and 92)

# 94. Inheritance: Create a subclass Student inheriting from Person.
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def introduce(self):
        return f"Hello, my name is {self.name}, I am {self.age} years old, and my student ID is {self.student_id}."

# 95. Polymorphism: Demonstrate polymorphism.
class Animal:
    def speak(self):
        return "Animal sound"

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

# Example Usage:
person1 = Person("Alice", 30)
print(person1.introduce())

student1 = Student("Bob", 20, "12345")
print(student1.introduce())

def animal_sound(animal):
  print(animal.speak())

animal = Animal()
dog = Dog()
cat = Cat()

animal_sound(animal)
animal_sound(dog)
animal_sound(cat)