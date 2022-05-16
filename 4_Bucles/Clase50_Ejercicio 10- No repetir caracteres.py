''' Capítulo 4: 4_Bucles
Ejercicio 10:
° Hacer un programa que pida una cadena por teclado, luego meta los
caracteres en una lista sin repetir caracteres
'''
cadena= input("Digite una cadena: ")

lista=[]
for i in cadena:
    if i not in lista: #Si el caracter aun no está en la lista
        lista.append(i) #Lo agregamos
print(lista)
#Código extra para juntar caracteres
lista2=""
for i in lista:
    if i!=" ":
        lista2+=i
lista=lista2
print(lista)
