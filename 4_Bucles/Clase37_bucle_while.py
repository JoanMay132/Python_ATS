#Bucle While

#Es algo que se repite y repite

'''En python existen dos tipos de bucles while y for'''

import math
numero=int(input("Digite un numero: "))
while numero<0:
    print("Error->Debería de ser un número positivo")
    numero = int(input("Digite un numero: "))
print(f"\n Su raíz cuadrada es: {(math.sqrt(numero)):.2f}")

#Bucle while parte 2
i= 0
while i<10:
    print("Hola mundo")
    i+=1

# Bucle while parte 3
i=1
while i<=10:
    print(i)
    i+=1