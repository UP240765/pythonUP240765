import math

age = int(18)       
height = float(1.70)
numComplex = 7 + 9j

base = float(input("Enter the base:"))
height = float(input("Enter the height:"))
areaTriangle = (base*height)/2
print(f"The area of your triangle is {areaTriangle}")

sideA = float(input("Enter sideA:"))
sideB = float(input("Enter sideB:"))
sideC = float(input("Enter sideC:"))
perimeterTriangle = sideA + sideB + sideC
print(f"The perimeter of your triangle is {perimeterTriangle}")

lenght = float(input("Enter lenght: ")) 
width = float(input("Enter width: ")) 
areaRectangle = lenght*width
perimeterRectangle = 2*(lenght+width)
print(f"Rectangle area: {areaRectangle}, Perimeter {perimeterRectangle}")

radius = float(input("Enter radius: ")) 
areaCircle = math.pi*(radius**2)
circunCircle = 2*math.pi*radius
print(f"Circle Area: {areaCircle}, Circunference: {circunCircle}")

#y = 2x - 2
m = 2
b = -2
interceptX = -b/m
interceptY = b
print(f"Intersección con el eje X: ({interceptX}, 0)")
print(f"Intersección con el eje Y: (0, {interceptY})")

x1, y1 = 2,2
x2, y2 = 6,10
slope = (y2-y1)/(x2-x1)
print(f"The slope is {slope}")

if m > slope:
    print(f"La pendiente {m} es mayor que la pendiente {slope}.")
elif m < slope:
    print(f"La pendiente {m} es menor que la pendiente {slope}.")
else:
    print(f"Las pendientes {m} y {slope} son iguales.")

y = 5**2 + 6*5 + 9
print(f"y value if x is equals to 5")

discriminante = 6**2 - 4*5*9
if discriminante > 0:
    x1 = (-b + math.sqrt(discriminante)) / (2 * 5)
    x2 = (-b - math.sqrt(discriminante)) / (2 * 5)
    print(f"Las soluciones son x1 = {x1} y x2 = {x2}")
elif discriminante == 0:
    x = -6 / (2 * 5)
    print(f"Hay una única solución: x = {x}")
else:
    print("No hay soluciones reales (las soluciones son complejas).")

pyLen = len("python")
drLen = len("dragon")

if pyLen != drLen:
    print("False Statement")

if ("on" in "python") and ("on" in "dragon" ):
    print("on is on both words")

pyLen = float(pyLen)
print(f"float python len: {pyLen}")
pyLen = str(pyLen)
print(f"String python len: {pyLen}")

sentence = "I hope this course is not full of jargon"

if "jargon" in sentence:
    print(f"Jargon is on {sentence}")

num = int(input("Ingresa un numero entero: "))
if num % 2 == 0:
    print("The number is even")
else:
    print("the number is not even")

print("7//3 == int(2.7)")
if 7//3 == int(2.7):
    print("They are equal")
else:
    print("They aren't equal")

print("type('10') == type(10)")
if type('10') == type(10):
    print("They are equal")
else:
    print("They aren't equal")

print("int(9.8) == 10")
if int(9.8) == 10:
    print("They are equal")
else:
    print("They aren't equal")

hour = float(input("Enter hours "))
hourRate = float(input("Enter rate per hours "))
print(f"Your weekly earning is {hour*hourRate}")

year = int(input("Enter number of years you have lived: "))
days = 365 * year
hour = days * 24
second = hour * 3600
print(f"You have lived {second} seconds")

for i in range(1, 6):
    print(i, 1, i, i**2, i**3)