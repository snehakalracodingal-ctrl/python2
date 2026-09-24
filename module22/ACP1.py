class student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
o1 = student("Penguin", 15)
o2 = student("Parrot", 10)
o1.display()
o2.display()