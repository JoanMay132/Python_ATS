'''Capítulo 6: Funciones
Ejercicio 4:

Desarrollar un programa para calcular el factorial de un
número con ayuda de una función recursiva.'''

def factorial(num):
    if num>0:
        resultado= num* factorial(num-1)
    else:
        resultado=1
    return resultado

valor=factorial(0)
print(valor)