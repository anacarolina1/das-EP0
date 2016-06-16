from car_factory import ChevroletFactory, WolksFactory, FordFactory, FiatFactory
from facade import facadeAdditional

if __name__ == '__main__':

	car_factory = ChevroletFactory()
	print "#########################"
	car = car_factory.create_car()
	car.show_info()

	car_factory = WolksFactory()
	print "-------------------------"
	car = car_factory.create_car()
	car.show_info()

	car_factory = FiatFactory()
	print "-------------------------"
	car = car_factory.create_car()
	car.show_info()

	car_factory = FordFactory()
	print "-------------------------"
	car = car_factory.create_car()
	car.show_info()
	print "#########################"


	#Facade Method
	print "\n\n*******ADICIONA ITENS AOS CARROS*********"
	facade = facadeAdditional()
	facade.addItems()
