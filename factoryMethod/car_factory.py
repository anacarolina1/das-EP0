from cars import Car, Celta, Gol, Fiesta, Palio

class CarFactory(Car):
	def create_car(sefl):
		pass

class ChevroletFactory(CarFactory):
	def __init__(self):
		self.car = Celta()

	def create_car(self):
		return Celta()


class WolksFactory(CarFactory):
	def __init__(self):
		self.car = Gol()

	def create_car(self):
		return Gol()

class FordFactory(CarFactory):
	def __init__(self):
		self.car = Fiesta()

	def create_car(self):
		return Fiesta()

class FiatFactory(CarFactory):
	def __init__(self):
		self.car = Palio()

	def create_car(self):
		return Palio()