# Bucle For
'''El bucle for se utiliza con colecciones
se tendrá un iterador que va a recorrer los elementos de una determinada colección'''
#for i in [1,2,3,4,5]:   #se repite el bucle 5 veces por la cantidad de elementos
   # print("Hola mundo") #la variable iteradora está recorriendo la colección elemento por elemento

#coleccion= {"Alejandro":22,"Maria":23,"José":45,"Luis":12}
#for i in coleccion:
    #print(f"Elemento: {i}") #Imprime la clave
    #print(f"{coleccion[i]}")
    #print(f"{i} -> {coleccion[i]}") #imprime clave y elemento
#for clave,valor in coleccion.items():
   #print(f"{clave} -> {valor}")

coleccion= "Alejandro"
for i in coleccion:
    print(f"{i}",end=".") # end deja un espacio entre carácter
