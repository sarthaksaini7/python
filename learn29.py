class Animal:
    def walk(self):
        print("Walk")


class Dog(Animal):
    def bark(self):
        print("Bark")


class Cat(Animal):
    def meow(self):
        print("Meow")


billi = Cat()
billi.walk()
print(billi)
bhauk = Dog()
bhauk.bark()
print(bhauk)
