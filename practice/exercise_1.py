class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __del__(self):
        print(f"{self.name} is no longer with us")
        
def main():
    person = Person("John", 30)
    print(person.name)
    print(person.age)
    del person
    
if __name__ == "__main__":
    main()