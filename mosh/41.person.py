class Person:
    def __init__(self,name):
        self.name = name
    def talk(self):
        print(f"hi,I am {self.name}")

lake = Person("lake smith")
lake.talk()
bob = Person("bob smith")
bob.talk()