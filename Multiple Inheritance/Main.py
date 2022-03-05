from Person import Person
from Job import Job
from Driver import Driver

D = Driver()

print("     +++++++++++++++++++++++")
print("     + D r i v e r - J o b +")
print("     +++++++++++++++++++++++")
print("")

D.set_Driver_Job("123456789", "Google", "Manager", "4asd4a", "2025", "Sedan")
D.printDriverJob()

for i in range(20):
    print("-", end="")

print("")
print("\n")

D.set_Driver_Job("689313834", "Microsoft", "Staff", "r4THgs4", "2024", "SUV")
D.printDriverJob()

for i in range(20):
    print("-", end="")

print("")
print("\n")

D.set_Driver_Job("484646468", "Tokopedia", "Directur",
                 "adnoeoa4", "2025", "Coupe")
D.printDriverJob()

for i in range(20):
    print("-", end="")

print("")
print("\n")

D.set_Driver_Job("315033105", "Shopee", "Vice President",
                 "8e61651da", "2027", "SUV")
D.printDriverJob()

for i in range(20):
    print("-", end="")

print("")
print("\n")

D.set_Driver_Job("549843351", "Samsung", "Manager",
                 "5ad53a2", "2030", "Hatchback")
D.printDriverJob()

for i in range(20):
    print("-", end="")

print("")
print("\n")

print("     +++++++++++++++++++++++++++++")
print("     + D r i v e r - P e r s o n +")
print("     +++++++++++++++++++++++++++++")
print("")

D.set_Driver_Person("187546825365", "Axel Eldrian", "Male",
                    "8", "awkd5a4", "2024", "Of Road")
D.printDriverPerson()

for i in range(20):
    print("-", end="")

print("")
print("\n")

D.set_Driver_Person("116135351843", "Ella Ismalina",
                    "Female", "9", "4ada54sd3", "2030", "Sedan")
D.printDriverPerson()

for i in range(20):
    print("-", end="")

print("")
print("\n")

D.set_Driver_Person("95845685624", "Aldrin Hadiwibowo",
                    "Male", "5", "6a5sd56", "2023", "Hactback")
D.printDriverPerson()

for i in range(20):
    print("-", end="")

print("")
print("\n")

D.set_Driver_Person("5645314831", "Edi Gunadi",
                    "Male", "10", "315asd61", "2027", "SUV")
D.printDriverPerson()

for i in range(20):
    print("-", end="")

print("")
print("\n")

D.set_Driver_Person("564526831", "Edi Masaid",
                    "Male", "3", "244sr", "2025", "Sedan")
D.printDriverPerson()

for i in range(20):
    print("-", end="")

print("")
print("\n")