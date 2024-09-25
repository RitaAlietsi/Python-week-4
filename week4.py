#Create a Python class named Person.

#The Person class should have the following attributes: name: representing the person's name. age: representing the person's age. gender: representing the person's gender.

#Implement a method called introduce that prints a message introducing the person with their name, age, and gender.

#Create an instance of the Person class and call the introduce method to display the person's information.

class Person:
    def __init__(self, name, age, gender):
        self.name = name      # Attribute representing the person's name
        self.age = age        # Attribute representing the person's age
        self.gender = gender  # Attribute representing the person's gender

    def introduce(self):
        # Method to introduce the person
        print(f"Hello, my name is {self.name}. I am {self.age} years old and my gender is {self.gender}.")

# Creating an instance of the Person class
person1 = Person("Kasike", 29, "Female")

# Calling the introduce method to display the person's information
person1.introduce()