from Person import Person
from Job import Job

class Driver(Person, Job):

    def __init__(self):
        super().__init__()
        self.licenseID = ""
        self.activeUntil = ""
        self.vehicleType = ""

    def set_Driver_Person(self, nik, name, gender, sleep, license, active, type):
        self.setPerson(nik, name, gender, sleep)
        self.licenseID = license
        self.activeUntil = active
        self.vehicleType = type

    def set_Driver_Job(self, nip, company, position, license, active, type):
        self.setJob(nip, company, position)
        self.licenseID = license
        self.activeUntil = active
        self.vehicleType = type

    def setlicenseID(self, license):
        self.licenseID = license

    def getlicenseId(self):
        return self.licenseID

    def setactiveUntil(self, active):
        self.activeUntil = active
    
    def getactiveUntil(self):
        return self.activeUntil

    def setvehicleType(self, type):
        self.vehicleType = type

    def getvehicleType(self):
        return self.vehicleType

    def printDriverPerson(self):
        self.printPerson()
        print("License ID : " + self.getlicenseId())
        print("Active : " + self.getactiveUntil())
        print("Vehicle Type : " + self.getvehicleType())
        self.sleep()

    def printDriverJob(self):
        self.printJob()
        print("License ID : " + self.getlicenseId())
        print("Active : " + self.getactiveUntil())
        print("Vehicle Type : " + self.getvehicleType())
        
        
        