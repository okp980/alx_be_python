class Engine:
    def __init__(self, power):
        self.power = power
        
    def start(self):
        print(f"Engine started with {self.power} power")
        
class Car:
    def __init__(self, brand, model, engine):
        self.brand = brand
        self.model = model
        self.engine = engine
        
    def start(self):
        self.engine.start()
        print(f"Car {self.brand} {self.model} started")
        
def main():
    engine = Engine(100)
    car = Car("Toyota", "Corolla", engine)
    car.start()
    
if __name__ == "__main__":
    main()