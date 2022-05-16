'''Capítulo 5: 5_Cadenas
Ejercicio 1:
° Hacer un programa donde se deberá imprimir por la consola la palabra
con más caracteres de dos palabras dadas. En el caso de que ambas palabras tengan
la misma cantidd de caracteres, deberás mostrar el mensaje "Son iguales"'''

cadena1=input("Digite una cadena: ")
cadena2=input("Digite una segunda cadena: ")

if len(cadena1)>len(cadena2):
    print(f"La cadena más larga es: {cadena1}")
elif len(cadena2)>len(cadena1):
    print(f"La cadena más larga es: {cadena2}")
elif len(cadena1)==len(cadena2):
    print("Son iguales")
