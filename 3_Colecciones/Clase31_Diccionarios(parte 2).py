#Diccionarios parte 2
equipo= {10:"Paulo Dybala",11:"Douglas Costa",7:"Cristiano Ronaldo",17:"Mario"}

print(equipo.get(10,"No existe un jugador con ese dorsal"))
#Se le pasa la clave no el indice
#Con el .get, te deja imprimir un mensaje
print(10 in equipo) #se puede comprobar si está el dorsal
print(equipo.keys()) #enseña las claves que hay dentro del diccionario
print(equipo.values())
print(equipo.items()) #items me pone en tuplas los elementos del diccionario
print(len(equipo))
equipo.clear()
print(equipo)