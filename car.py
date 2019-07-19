class Vehicle:
    def __init__(self):
        self.__mileage = None
        self.__fuel_left = None
        self.__initial_fuel = None
    def set_mileage(self,mil):
        self.__mileage = mil
    def set_fuel_left(self,le):
        self.__fuel_left = le
    def set_initial_fuel(self,inf):
        self.__initial_fuel = inf

    def get_mileage(self):
        return self.__mileage
    def get_fuel_left(self):
        return self.__fuel_left
    def get_initial_fuel(self):
        return self.__initial_fuel


    def identify_distance_that_can_be_travelled(self):
        if self.__fuel_left <= 5 :
            return 0
        else:
            a = self.__fuel_left - 5
            trav = a * self.__mileage
            return trav

    def identify_distance_travelled(self,initial_fuel):
        total_use_fuel = initial_fuel - self.__fuel_left
        total_travel = total_use_fuel * self.__mileage
        return total_travel

v1 = Vehicle()
v1.set_initial_fuel(50)
v1.set_fuel_left(10)
v1.set_mileage(7.5)

print(v1.identify_distance_that_can_be_travelled())
print(v1.identify_distance_travelled(45))


