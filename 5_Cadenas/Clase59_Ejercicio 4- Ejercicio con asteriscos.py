'''Capítulo 5: 5_Cadenas
Ejercicio 4:
°Hacer un programa donde se reemplacen todos los espacios de una cadena
por asteriscos y además cada palabra comience por mayúsculas'''

cadena= input("Digite una cadena: ")
# Primero, reemplazamos los " " por "*"
cadena=cadena.replace(" ",'*')
#Segundo, convertir a Titulo con método .title()
cadena=cadena.title()
print(cadena)