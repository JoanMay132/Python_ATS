'''Capítulo 4: 4_Bucles
Ejercicio 5:
 °Hacer un programa para calcular el factorial de un número positivo'''

numero=int(input("Digite un número: "))
while numero<0: #mientras el número sea negativo
    print("Error ->El número tiene que ser positivo")
    numero = int(input("Digite un número: "))

#Calcular el factorial
factorial=1
for i in range(1,numero+1):
    factorial*=i #Multiplica la variable iteradora

print(f"El factorial de {numero} es {factorial}")