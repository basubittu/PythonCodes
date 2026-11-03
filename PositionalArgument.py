class VoterList:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("My Name is", self.name)
        print("He is", self.age, "years old")


name = input("Enter Your name: ")
age = int(input("Enter Your age: "))

ob = VoterList(name, age)
ob.display()
