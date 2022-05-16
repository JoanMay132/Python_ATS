'''Capítulo 4: 4_Bucles
Ejercicio 4:

°Hacer un programa para sumar números pares dentro de un rango

Ejemplo:
 Suma de números pares del 2 al 30
 Suma= 240'''

a= int(input("Digite de donde va a comenzar a sumar: "))
b= int(input("Digite hasta donde quiere llegar a sumar: "))
suma=0
for i in range(a,b+1): #se le pone b+1 porque b siempre llega hasta un número anterior
    if i%2==0: #Si el numero es par
        suma+=i
print(f"\nLa suma de numeros pares dentro del rango es: {suma}")

