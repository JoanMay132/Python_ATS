'''Ejercicio 3:
Hacer un programa para intercambiar
el valor de 2 variables'''

a= input("a - >")
b= input("b - >")

a,b = b,a
print(f"El nuevo valor de a es: {a}")
print(f"El nuevo valor de a es: {b}")