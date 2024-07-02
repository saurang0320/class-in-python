class Car:
    # Class Variable
    vehicle = 'Car'
    all_cars = []  # Class variable to store all instances
    
    def __init__(self, model, price):
        # Instance Variable
        self.model = model
        self.price = price
        Car.all_cars.append(self)  
    
# Objects of class
Audi = Car("R8", 100000)
BMW = Car("I8", 10000000)
Maruti = Car("MUV", 700000)

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

# Accessing class variable using class name
print("\nAccessing class variable using class name")
print('Class vehicle:', Car.vehicle)
print('Audi vehicle:', Audi.vehicle)
print('BMW vehicle:', BMW.vehicle)
print('Maruti vehicle:', Maruti.vehicle)

# Print all car details from the class variable list
print("\nPrinting all cars:")
for car in Car.all_cars:
    print(f"Model: {car.model}, Price: {car.price}")
