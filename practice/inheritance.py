class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        print("The animal makes a sound")
        

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
        
    def make_sound(self):
        print("Woof Woof")
        
def main():
    dog = Dog("Buddy", "Golden Retriever")
    dog.make_sound()
    print(dog.name)
    print(dog.breed)
        
if __name__ == "__main__":
    main()