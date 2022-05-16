#cadena de caracteres (parte 2)

cadena= "hola mundo".startswith('h') #retorna valor booleano del caracter o palabra con el que empieza
print(cadena)

cadena= "hola mundo".endswith('o') #devuelve valor booleano del caracter o palabra con la que termina
print(cadena)

cadena="hola-mundo".split('-') #retorna una lista con los elementos que tenga dentro de la cadena , separa x espacios
print(cadena)

cadena=",".join("alejandro") #separa cada uno de los elementos con lo que se indique en el string
print(cadena)

cadena= "--hola--".strip('-') #elimina espacios innecesarios o también se le puede indicar el caracter a eliminar
print(cadena)

cadena= "hola mundo".replace('o','0') #te reemplaza un caracter por el que indiques, también pueden ser palabras
print(cadena)