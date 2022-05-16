'''Capítulo 6: Funciones

Ejercicio 5:

Desarrollar un programa que permita sumar los dígitos de un número con ayuda de una función recursiva'''

def sumardigitos(num):
    if num==0: #CASO BASE
        resultado=0
    else: #CASO RECURSIVO
        resultado=sumardigitos(int(num/10)) + (num%10)
    return resultado
valor=sumardigitos(165)
print(valor)
