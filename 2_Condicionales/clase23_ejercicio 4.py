#Ejercicio 4
'''Construir un programa que simule el funcionamiento de una
calculadora que pueda realizar las cuatro operaciones aritméticas
básicas (suma, resta, multiplicación y división). El usuario debe espe-
cificar la operación con el primer carácter del nombre de la operación
S, s- suma
R, r- resta
P, p, M, m- Multiplicación
D, d - división'''
num1=float(input("Digite un número: "))
num2=float(input("Digite otro número: "))
operacion=input("\nElija la operación a realizar: ").lower()

if operacion=='s':
    suma=num1+num2
    print(f"\nLa suma es {suma} ")
elif operacion=='r':
    resta=num1-num2
    print(f"\nLa resta es {resta}")
elif operacion=='p' or operacion=='m':
     multiplicacion=num1*num2
     print(f"\nLa multiplicación es {multiplicacion}")
elif operacion=='d':
    division=num1/num2
    print(f"\nLa división es {division:.3f}")
else:
    print("Se equivocó de carácter")
