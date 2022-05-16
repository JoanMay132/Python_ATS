#Tuplas
#Las tuplas no se pueden modificar(añadir elementos)
tupla= (4,"Hola",6.7,[1,2,3],4) #transforma tupla a lista
lista= list(tupla)
lista= [4,"Hola",6.7,[1,2,3],4] #transforma lista a tupla
tupla=tuple(lista)
print(tupla)
print(lista)
print(tupla[1:-1])
print(4 in tupla)
print(tupla.index("Hola"))
print(tupla.count(4))
print(len(tupla))
#todo tipo de busqueda está permitido

tupla=(3,1,2,"Hola,")
print(type(tupla))