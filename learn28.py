class Person:
    def __init__(self, name):
        super().__init__()
        self.name = name
        print(f'{name}')

    def talk(self):
        print(f"My name is {name}")


name = input("Enter your name > ")
greeting = Person("Vijay Saini")
greeting.talk()

bob = Person("Bob Smith")
bob.talk()
