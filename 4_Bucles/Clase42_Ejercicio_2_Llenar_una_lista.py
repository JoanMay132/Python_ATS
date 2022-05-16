'''Capítulo 4: 4_Bucles
Ejercicio 2:

°llenar un lista con los números del 1 al 10, luego modificar los elementos de
una lista multiplicándolos por un valor que el usuario digite.'''
#Forma Joan May
lista= list(range(1,11))
print(lista)
multiplicar= int(input("Digite un número a multiplicar: "))
print("Lista final con el valor multiplicado: ")
for i in lista:
    print(f"{i*multiplicar}",end='-')

#Primera forma ATS
lista=list(range(1,11))
print("\nLa lista original: ")
for i in lista:
    print(i,end="-")
valor=int(input("\nDigite un valor a multiplicar: "))
#Multiplicar todos los elementos de la lista
indice=0
for i in lista:
    lista[indice]*=valor
    indice+=1
print(f"\n Lista final con los elementos multiplicados por {valor} ")
for i in lista:
    print(i,end="-")
print("\n")

# Segunda forma
lista=list(range(1,11))
print("\nLa lista original: ")
for i in lista:
    print(i,end="-")
valor=int(input("\nDigite un valor a multiplicar: "))
# Multiplicar todos los elementos de la lista
for indice,i in enumerate (lista):
    lista[indice]*=valor

print(f"\n Lista final con los elementos multiplicados por {valor}")
for i in lista:
    print(i,end="-")