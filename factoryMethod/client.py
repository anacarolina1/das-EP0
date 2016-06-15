from car_factory import ChevroletFabric

if __name__ == '__main__':

	car_factory = ChevroletFabric()
	car = car_factory.create_car()
	car.show_info()

	