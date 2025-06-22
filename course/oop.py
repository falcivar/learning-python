class Person:
    def __init__(self, name, age, nationality="uk"):
        self.name = name
        self.age = age
        self.nationality = nationality

    def introduce_self(self):
        print(f"Hey man! Name's {self.name}, from {self.nationality}!")

    def lie_about_age(self):
        print(f"I'm {self.age - 5} years old. Really.") 

    def emigrate(self, new_country):
        self.nationality = new_country

    def think_random_thought(self):
        return "Why is London called London?"


stranger = Person("Josiah", 20, "malaysia")

stranger.emigrate("uk")
stranger.introduce_self()
stranger.lie_about_age()

thought = stranger.think_random_thought()
print(thought)

class Vector: 
    def __init__(self, x, y): 
        self.x = x 
        self.y = y

    def __add__(self, other): 
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self): 
        return f"Vector({self.x}, {self.y})"

v1 = Vector(1, 2) 
v2 = Vector(5, 7) 
v3 = v1 + v2
print(v3)