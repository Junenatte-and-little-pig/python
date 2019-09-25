# -*- encoding: utf-8 -*-


class Vehicle(object):
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def __str__(self):
        return "name={0},color={1}".format(self.name, self.color)


class Car(Vehicle):
    def __init__(self, name, color, seat):
        super(Car, self).__init__(name, color)
        self.seat = seat

    def __str__(self):
        return "name={0},color={1},seat={2}".format(self.name, self.color,
                                                    self.seat)


class Truck(Vehicle):
    def __init__(self, name, color, load):
        super(Truck, self).__init__(name, color)
        self.load = load

    def __str__(self):
        return "name={0},color={1},load={2}".format(self.name, self.color,
                                                    self.load)


class CarFactory(object):
    @classmethod
    def create_vehicle(cls, name, color, seat, load):
        return Car(name, color, seat)


class TruckFactory(object):
    @classmethod
    def create_vehicle(cls, name, color, seat, load):
        return Truck(name, color, load)


car = CarFactory().create_vehicle('宝马', '红色', 5, 0)
print(car)
