#5_Cadenas de caracteres

cadena="hola mundo".upper() #convierte toda la cadena a mayuscula
print(cadena)

cadena="hola mundo"
print(cadena.upper()) #Igual este metodo sirve para convertir a mayúscula

cadena= "HOLA MUNDO"
print(cadena.lower())

cadena="hola mundo".capitalize() #Pone en mayuscula la primera letra que encuentre
print(cadena)

cadena= "hola mundo".title() #se convierten a mayuscula la primera letra de cada palabra
print(cadena)

cadena= "hola mundo".count('o') #cuenta las palabras o letras que aparecen dentro de la cadena
print(cadena)

cadena= "hola mundo mundo" .find('mundo') #te dice en que indice está el caracter o palabra que busques (la primera que encuentre)
print(cadena)

cadena= "hola mundo mundo".rfind('mundo') #te muestra la última coincidencia que encuentre (al contrario)
print(cadena)

cadena="1000".isdigit() #te menciona si solo tiene valores númericos (entrega resultado booleano)
print(cadena)

cadena="Adstw".isalpha() #te menciona si todos los caracteres son alfabeticos (devuelve booleano)
print(cadena)
cadena="ahdda22".isalnum() #te menciona si tiene caracteres alfanumericos
print(cadena)

cadena="hola mundo".islower() #te dice si toda la cadena está en minuscula (devuelve booleano)
print(cadena)

cadena="HOLA MUNDO".isupper() #te dice si toda la cadena está en mayúscula (devuelve booleano)
print(cadena)

cadena="Hola Mundo".istitle() #te dice si la primera letra de cada palabra está en mayuscula (devuelve booleano)
print(cadena)

cadena= "     ".isspace() # te dice si la cadena está completa de espacios (devuelve booleano)
print(cadena)