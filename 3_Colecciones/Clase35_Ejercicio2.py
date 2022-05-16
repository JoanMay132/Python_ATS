'''Capítulo 3: Colecciones
Ejercicio 2:
*Escriba un programa que tenga dos listas y que, a continuación, cree las siguientes
 listas (en las que no debede haber repeticiones):
°Lista de palabras que aparecen en las dos listas
°lista de palabras que aparecen en la primera lista, pero no en la segunda.
°Lista de palabras que aparecen en la segunda lista, pero no en la primera
°Lista de palabras que aparecen en ambas listas.'''

lista1=[1,2,3,4,5,4,3,2,1,5]
lista2=[4,5,6,7,8,4,5,6,7,8]
#Elimine los elementos repetidos de ambas listas
a=set(lista1)
b=set(lista2) #se crean dos conjuntos

union= list(a|b)
soloA=list(a-b)
soloB=list(b-a)
interseccion=list(a&b)
print(f"Lista de palabras que aparecen en las dos listas: {union}")
print(f"lista de palabras que aparecen en la primera lista, pero no en la segunda: {soloA}")
print(f"Lista de palabras que aparecen en la segunda lista, pero no en la primera: {soloB}")
print(f"Lista de palabras que aparecen en ambas listas: {interseccion}")