from cars import Car, Celta

class CarFactory(Car):
	def create_car(sefl):
		pass

class ChevroletFabric(CarFactory):
	def __init__(self):
		self.car = Celta()

	def create_car(self):
		return Celta()