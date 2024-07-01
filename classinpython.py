


class Car: 
	
	# Class Variable 
	vehicle = 'Car'		
	def __init__(self, model, price): 
	
		# Instance Variable	 
		self.model = model
		self.price = price		 
	
# Objects of class 
Audi = Car("R8", 100000) 
BMW = Car("I8", 10000000) 
Maruti = Car("MUV", 700000)


print('Audi details:') 
print('Audi is a', Audi.vehicle) 
print('Model: ', Audi.model) 
print('price: ', Audi.price) 

print('\n BMW details:') 
print('BMW is a', BMW.vehicle) 
print('Model: ', BMW.model) 
print('price: ', BMW.price)

print('\n Maruti  details:') 
print('maruti  is a', Maruti.vehicle) 
print('Model: ', Maruti.model) 
print('price: ', Maruti.price)

# Class variables can be
# accessed using class 
# name also 
print("\nAccessing class variable using class name") 
print(Car.vehicle) 
print(Audi.vehicle) 
print(BMW.vehicle)
print(Maruti .vehicle)

















