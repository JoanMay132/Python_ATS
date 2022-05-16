'''Capítulo 4: 4_Bucles
Ejercicio 1:
°Llenar una lista con los números del 1 al 50, luego mostrar la lista con
un bucle for, los elementos deben mostrarse de la siguiente forma:

1-2-3-4-5-..-50'''
#Agregamos a la lista los elementos del 1 al 50(Primera manera)
lista= list(range(1,51))
for i in lista:
    print(f"{i}",end="-")
print("\n")
#Otra manera
lista=[]
#Agregamos a la lista los elementos del 1 al 50
i=1
while i<=50:
    lista.append(i)
    i+=1
#Imprimiendo los elementos de la lista
for i in lista:
    print(i,end="-")