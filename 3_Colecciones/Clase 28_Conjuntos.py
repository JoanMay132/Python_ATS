#Conjuntos
'''Son un tipo de colección en donde los elementos
se agregan de forma desordernada.
Su primer carácteristica no pueden existir duplicados'''
conjunto= set()
#Para especificar que es conjunto se escribe set() o set{}
conjunto= {1,2,3,"Hola",4.56,1,2,3}
#se le pueden agregar de todo tipo de datos menos otro tipo de colecciones (listas)
conjunto.add(5) #Los conjuntos no siguen un roden especifico, lo pone donde quiera
conjunto.add("Adiós")
conjunto.add('a')
conjunto.discard(3) #Elimina elemento de un conjunto
#conjunto.clear() #eliminar conjunto (vaciarlo)
print(conjunto) #obvia los duplicados
print(3 not in conjunto)
print(4.5 in conjunto)