from Vehicle import Vehicle
from Airplane import Airplane
from Ship import Ship

V = Vehicle()
A = Airplane()
S = Ship()
print("     +++++++++++++++++++")
print("     + A I R P L A N E +")
print("     +++++++++++++++++++")
print("") 
# AIRPLANE
A.setAirplane("Bombardier Aerospace", "Avtur", "13", "982", "Bombardier Global 8000", "12", "24")
A.printAirplane()

for i in range(20):
    print("-", end="")

print("")
print("\n")
A.setAirplane("Bombardier Aerospace", "Avtur", "19", "981", "Bombardier Global 7500", "10", "24")
A.printAirplane()

for i in range(20):
    print("-", end="")

print("")
print("\n")
A.setAirplane("Gulfstrem", "Avtur", "19", "904", "Gulfstream G650ER", "7", "21")
A.printAirplane()

for i in range(20):
    print("-", end="")

print("")
print("\n")
A.setAirplane("Dassault", "Avtur", "19", "965", "Dassault Falcon 8X", "7", "17")
A.printAirplane()

for i in range(20):
    print("-", end="")

print("")
print("\n")
A.setAirplane("Gulfstream", "Avtur", "19", "849", "Gulfstream G550", "10", "24")
A.printAirplane()

for i in range(20):
    print("-", end="")

print("")
print("\n")
A.setAirplane("Gulfstream", "Avtur", "19", "925", "Gulfstream G600", "10", "24")
A.printAirplane()

for i in range(20):
    print("-", end="")

print("")
print("\n")
A.setAirplane("Bombardier Aerospace", "Avtur", "17", "944", "Bombardier Global 6000", "10", "21")
A.printAirplane()

#SHIP
print("     +++++++++++")
print("     + S H I P +")
print("     +++++++++++")
print("")
S.setShip("Beneteau", "MFO", "16", "15", "2", "beneteau oceanis yacht 62", "France")
S.printShip()

for i in range(20):
    print("-", end="")

print("")
print("\n")

S.setShip("Simpson Marine", "MFO", "12", "30", "1", "Lagoon 42", "France")
S.printShip()

for i in range(20):
    print("-", end="")

print("")
print("\n")

S.setShip("Lagoon Yachting", "MFO", "12", "65", "4", " Princess 49", "Singapure")
S.printShip()

for i in range(20):
    print("-", end="")

print("")
print("\n")

S.setShip("Hong Seh Marine", "MFO", "5", "64", "1", " Crachi Z35", "Singapure")
S.printShip()

for i in range(20):
    print("-", end="")

print("")
print("\n")

S.setShip("Azimut Yachts", "MFO", "10", "52", "1", "Azimut 95RPH", "Italia")
S.printShip()