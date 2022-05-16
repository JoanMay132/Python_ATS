#Listas
lista= [5,4,3,6,8,1]
print(len(lista)) #funcion len sirve para contar los elementos de la lista
lista.append(2) #lista.append() agrega elementos al final de la lista
lista.append("Joan")
print(lista)

lista= [2,3,4,5,6]
lista.extend([2,3,4]) #lista.extend([]) agrega varios elementos en la lista
print(lista)

lista=[2,3,5,1]
lista.insert(0,"ola") #lista.insert() agrega elementos en la posición de la lista que se indique
print(lista)

lista1=[1,30,59]
lista2=[2,212,49]
lista3=lista1+lista2
print(lista3)

lista=[2,3,4,5,0]
print(3 in lista) #print(in) sirve para saber si el valor está dentro de la lista

lista=[1,2,3,4,5,"Joan"]
print(lista.index("Joan")) #print(lista.index()) retorna el indice donde está el elemento que se busca

lista=[1,2,3,4,5,"Joan",1,2,3,1,"Joan",1]
print(lista.count(1)) #print(lista.count(numero)) imprime la cantidad de veces que aparece un elemento

lista=[1,2,3,4,5,"Joan",1,2,3,1,"Joan",1]
lista.pop(0) #lista.pop(indice) elimina el indice que se coloque
print(lista)

lista=[1,2,3,4,5,"Joan"]
lista.remove("Joan") #lista.remove(numero o elemento) elimina el elemento que se coloque
print(lista)

lista=[1,2,3,4,5,"Alejandro"]
lista.clear() #lista.clear elimina toda la lista (queda vacía)
print(lista)

lista=[1,2,3,4,5,"Joan"]
lista.reverse() #lista.reverse() da la vuelta a la lista
print(lista)

lista=[1,2,3,4,5,"Joan"]*2 # se pueden multiplicar las listas y poner en el mismo orden
print(lista)

lista=[5,4,-8,9,0,1,3]
lista.sort() #lista.sort() ordena los elementos enteros
print(lista)

lista=[5,4,-8,9,0,1,3]
lista.sort(reverse=True) #lista.sort(reverse=True) se ordenan los elementos de mayor a menor
print(lista)



