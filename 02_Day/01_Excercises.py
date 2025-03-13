#Day 2: 30 Days of python programming
import math

def circleArea(radio):
    area = math.pi*(radio**2)
    print(f"EL area es de {area}")
    return area

def circleCircunference(radio):
    circunf = 2*math.pi*radio
    print(f"La circunferencia es de {circunf}")
    return circunf

firstName = "Angie"
lastName = "Palos"
fullName = "Angie Palos"
country = "México"
city = "Aguascalientes"
age = 18
year = 2006
isMarried = False
isTrue = True
isLight = False
a, b, c = "a", 1, True

print(type(firstName), " ", len(firstName))
print(type(lastName), " ", len(lastName))
print(type(fullName))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(isMarried))
print(type(isTrue))
print(type(isLight))
print(type(a))
print(type(b))
print(type(c))

n1 = 5
n2 = 4

suma = n1 +n2
diff = n2 - n1
prod = n2 * n1
div = n1 / n2
remainder = n2 % n1
exp = n1 ** n2
floorDivision = n1 // n2


r = 30
area_of_circle = circleArea(r)
circum_of_circle = circleCircunference(r)

r = float(input("Dame el radio del circulo: "))
area_of_circle = circleArea(r)
circum_of_circle = circleCircunference(r)

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
pais = input("Ingrese su país: ")
edad = input("Ingrese su edad: ")