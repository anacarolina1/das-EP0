from car_factory import ChevroletFactory, WolksFactory, FordFactory, FiatFactory

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