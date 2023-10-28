class Mammal:
    def walk(self):
        print("walk")

class dog(Mammal):
    def bark(self):
        print("bark")
class cat(Mammal):
    def annoying(self):
        print("annoying")

dog1 = dog()
dog1.bark()

