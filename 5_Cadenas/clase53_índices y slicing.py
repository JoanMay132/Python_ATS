#cadena de caracteres
cadena= "Alejandro"
#se quiere mostrar específico de la cadena

print(cadena[0]) #Se indica el indice y se imprime el caracter en donde se encuentre

#En cadenas se puede hacer slicing
print(cadena[1:4]) #SLICING (subcadena que se muestra)
'''Las cadenas son inmutables'''

# cadena[0]= 'a' # No se puede modificar directamente (error)

cadena= 'a' + cadena [1:]
print(cadena)
print(len(cadena)) #Cuenta los caracteres que hay dentro de una cadena