class Person:

    def __init__(self):
        self.NIK = ""
        self.Name = ""
        self.gender = ""
        self.TimeSleep = ""

    def setPerson(self, nik, name, gender, sleep):
        self.NIK = nik
        self.Name = name
        self.gender = gender
        self.TimeSleep = sleep

    def setNIK(self, nik):
        self.NIK = nik

    def getNIK(self):
        return self.NIK

    def setName(self, name):
        self.Name = name

    def getName(self):
        return self.Name

    def setgender(self, gender):
        self.gender = gender

    def getgender(self):
        return self.gender

    def setTimeSleep(self, time):
        self.TimeSleep = time

    def getTimeSleep(self):
        return self.TimeSleep

    def sleep(self):
        print(">>> SLEEP <<<")
        print("Name Person : " + self.getName())
        print("Time Sleep (hour) : " + self.getTimeSleep())

    def printPerson(self):
        print("NIK : " + self.getNIK())
        print("Gender : " + self.getgender())
