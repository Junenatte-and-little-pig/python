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


class VehicleFactory(object):
    @classmethod
    def create_vehicle(cls, type_name, name, color, seat, load):
        ve = None
        if type_name.lower() == "car":
            ve = Car(name, color, seat)
        elif type_name.lower() == "truck":
            ve = Truck(name, color, load)
        return ve


vehicles = [VehicleFactory.create_vehicle('car', '宝马', '红色', 5, 0),
            VehicleFactory.create_vehicle('car', '奥迪', '黑色', 5, 0),
            VehicleFactory.create_vehicle('truck', '解放', '蓝色', 0, 10)]
for v in vehicles:
    print(v, end="\t")
    print(type(v))
