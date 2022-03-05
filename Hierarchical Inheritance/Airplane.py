from Vehicle import Vehicle

class Airplane(Vehicle):

    def __init__(self):
        super().__init__()
        self.Type = ""
        self.Age = ""
        self.WingsLength = ""

    def setAirplane(self, brand, fueltype, passenger, speed, type, age, wings):
        self.setVehicle(brand, fueltype, passenger, speed)
        self.Type = type
        self.Age = age
        self.WingsLength = wings

    def setType(self, type):
        self.Type = type

    def getType(self):
        return self.Type

    def setAge(self, age):
        self.Age = age

    def getAge(self):
        return self.Age

    def setWingsLength(self, wings):
        self.WingsLength = wings

    def getWingsLength(self):
        return self.WingsLength

    def printAirplane(self):
        print(">>> SPECIFICATION <<<")
        print("Type : " + self.getType())
        print("Age : " + self.getAge())
        print("Wings Length : " + self.getWingsLength() + " m")
        self.DataPrint()
        print("")
        self.Move()