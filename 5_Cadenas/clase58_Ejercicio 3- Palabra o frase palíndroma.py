'''Capítulo 5: 5_Cadenas
Ejercicio 3:
°Hacer un programa que determine si una palabra o frase es palíndroma.
Una cadena palíndroma se lee igual de izquierda a derecha que de derecha
a izquierda.

Ejemplos:
-oso
-reconocer
-anita lava la tina'''

#Ejercicio 3- Palabra o frase palíndroma
cadena= input("Digite una cadena: ")

#Primero, quitamos los espacios en blanco de la cadena
cadena= cadena.replace(" ","") #cada que encuentre un espacio se reemplaza por nada

#Segundo, invertimos la cadena
cadena2= cadena[::-1]  #Se crea otra cadena y adentro se guarda la cadena invertida con [::-1]
print(f"La cadena invertida es: {cadena2}")
if cadena == cadena2:
    print("La cadena es un palíndromo")
else:
    print("La cadena no es un palíndromo")
