class Vehicle:
    def __init__(self):
        self.__vehicle_id = 0
        self.__vehicle_type = ""
        self.__vehicle_cost = 0
        self.__premium_amount = 0

    def set_vehicle_id(self,vehicle_id):
        self.__vehicle_id = vehicle_id
    def set_vehicle_type(self,vehicle_type):
        self.__vehicle_type = vehicle_type
    def set_vehicle_cost(self,vehicle_cost):
        self.__vehicle_cost = vehicle_cost
    def get_vehicle_id(self):
        return self.__vehicle_id
    def get_vehicle_type(self):
        return self.__vehicle_type
    def get_vehicle_cost(self):
        return self.__vehicle_cost

    def calculate_premium(self):
        if self.__vehicle_type == "Two Wheeler":
            self.__premium_amount = self.__vehicle_cost*0.02
        elif self.__vehicle_type == "Four Wheeler":
            self.__premium_amount = self.__vehicle_cost*0.06
        else:
            return False

    def display_vehicle_details(self):
        print(self.__vehicle_id,"is type of",self.__vehicle_type,"have amount ",self.__vehicle_cost,"and premium of ",self.__premium_amount)

v1 = Vehicle()
v1.set_vehicle_id(1)
v1.set_vehicle_cost(500000)
v1.set_vehicle_type("Four Wheeler")

print(v1.get_vehicle_id())
print(v1.get_vehicle_cost())
v1.calculate_premium()
v1.display_vehicle_details()