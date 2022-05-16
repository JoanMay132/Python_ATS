#6_Funciones
'''son un bloque de código que están de nuestros programa
y nos sirven para resolver un problema especifico dentro de este
y sirven para reutilizar el código cuantas veces queramos'''
# 6_Funciones sin retorno de valor

#creamos una función
def saludar(nombre): #Deben llevar una identación #Si se quieren usar más parametros se separan x comas
    print(f"Hola {nombre}") #En este punto aún no se puede ejecutar, hay que llamarla

saludar("Joan")  #Llamamos a la función #Funciones te permiten reutilizar código
saludar("Hilda")

def tabla_multiplicar(numero):
    for i in range(1,11):
        print(f"{numero}*{i}= {numero*i}")

tabla_multiplicar(5) #Estas son sin retorno de valor
print()
tabla_multiplicar(3) #Sin retorno de valor