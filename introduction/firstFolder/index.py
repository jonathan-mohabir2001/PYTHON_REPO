# just some general writing after reading this initial chapter


import random as rnd


def printRandomMath():
    print(rnd.randint(1, 10))


printRandomMath()


myName = "jonathan Mohabir"
myAge = 21
print(f"Here is a dude named {myName} and his age is {myAge}")


class makeAPerson:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def printName(self):
        print(f"You are {self.name} and you are {self.age} years old")


person = makeAPerson("Jonathan Mohabir", 21)

person.printName()
