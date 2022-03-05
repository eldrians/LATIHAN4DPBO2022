class Vehicle:

    # contructor
    def __init__(self):
        self.Brand = ""
        self.FuelType = ""
        self.MaxPassengers = ""
        self.MaxSpeed = ""

    def setVehicle(self, brand, fueltype, passenger, speed):
        self.Brand = brand
        self.FuelType = fueltype
        self.MaxPassengers = passenger
        self.MaxSpeed = speed

    def setBrand(self, brand):
        self.Brand = brand

    def getBrand(self):
        return self.Brand

    def setFuelType(self, fuel):
        self.FuelType = fuel

    def getFuelType(self):
        return self.FuelType

    def setMaxPassengers(self, passengers):
        self.MaxPassengers = passengers

    def getMaxPassengers(self):
        return self.MaxPassengers

    def setMaxSpeed(self, speed):
        self.MaxSpeed = speed

    def getMaxSpeed(self):
        return self.MaxSpeed

    def Move(self):
        print(">>> MOVE <<<")
        print("Brand : " + self.getBrand())
        print("Max Speed : " + self.getMaxSpeed() + " Km/h")

    def DataPrint(self):
        print("Fuel Type : " + self.getFuelType())
        print("Max Passengers  : " + self.getMaxPassengers() + " People")
