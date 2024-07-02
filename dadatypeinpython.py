from typing import Dict

class Car:
    # Class Variable
    vehicle: str = 'Car'  # Type hint for class variable
    all_cars: Dict[str, 'Car'] = {}  # Dictionary to store all instances with type hint
    
    def __init__(self, name: str, model: str, price: int):
        # Instance Variables with type hints
        self.name: str = name
        self.model: str = model
        self.price: int = price
        Car.all_cars[self.name] = self  # Store instance in dictionary using name as key  
    
# Objects of class
Audi = Car("Audi", "R8", 100000)
BMW = Car("BMW", "I8", 10000000)
Maruti = Car("Maruti", "MUV", 700000)

print('Audi details:')
print('Audi is a', Audi.vehicle)
print('Model: ', Audi.model)
print('Price: ', Audi.price)

print('\nBMW details:')
print('BMW is a', BMW.vehicle)
print('Model: ', BMW.model)
print('Price: ', BMW.price)

print('\nMaruti details:')
print('Maruti is a', Maruti.vehicle)
print('Model: ', Maruti.model)
print('Price: ', Maruti.price)


print("\nAccessing class variable using class name")
print('Class vehicle:', Car.vehicle)
car_name = "BMW"
if car_name in Car.all_cars:
    car_instance = Car.all_cars[car_name]
    print(f'{car_name} details:')
    print(f'{car_name} is a {car_instance.vehicle}')
    print(f'Model: {car_instance.model}')
    print(f'Price: {car_instance.price}')
else:
    print(f'Car with name "{car_name}" not found.')
print("\nPrinting all cars:")
for name, car in Car.all_cars.items():
    print(f"Name: {name}, Model: {car.model}, Price: {car.price}")
