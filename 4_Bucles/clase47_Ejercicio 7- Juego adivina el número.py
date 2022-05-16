'''Capítulo 4: 4_Bucles
Ejercicio 7:
°Realizar un juego para adivinar un número. Par ello generar un número aleatorio
entre 0-100, y luego ir pidiendo números indicando "es mayor" o "es menor"
según sea mayor o menor con respecto a N. El proceso termina cuando el usuario
acierta y mostrar el número de intentos.'''

#Ejercicio 7- Juego adivina el número

import random
aleatorio=random.randint(0,100) #Se genera un número aleatorio
print("\t .:Juego adivina el número:.")
contador=0
while True: #Bucle infinito?
    numero=int(input("Digite un número: "))
    contador+=1
    if numero>aleatorio:
        print("\tNo es el número, digita un número menor")
    elif numero<aleatorio:
        print("\tNo es el número, digita un número mayor")
    else:
        print(f"\t FELICIDADES, Acabas de adivinar el número {aleatorio}")
        break
print(f"\n Número de intentos: {contador}")