'''Capitulo 3: Colecciones
Ejercicio 1:
*Escriba un programa donde tenga una lista y que, a continuación, elimine los elementos repetidos,
por último mostrar la lista.'''
lista=[1,2,3,3,3,4,4,5]
conjunto= set(lista) #Se convierte a conjunto
lista=list(conjunto) #Luego se convierte a lista nuevamente y se imprime
print(lista)

lista=[1,3,4,5,2,4,1,2]
lista= list(set(lista))
print(lista)