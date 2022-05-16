'''Ejercicio 1:

Desarrollar un programa que pueda calcular el valor del tipo
de cambio de moneda (de tu moneda-hacia el dólar y viceversa)'''
def cambio_Pesos_Dolares(Pesos):
    return Pesos*0.050
def cambio_dolares_pesos(dolares):
    return dolares/0.05
while True:
    print("""\t.:MENU:.
1.- Convertir Pesos a Dólares
2.- Convertir de Dólares a Pesos
3.- Salir""")
    opcion=int(input("Digite una opción: "))
    print()

    if opcion==1:
        Pesos=int(input("Digite la cantidad de Pesos: "))
        print(f"Dolares -> ${cambio_Pesos_Dolares(Pesos):.2f}")
    elif opcion==2:
        dolares=int(input("Digite la cantidad de dólares: "))
        print(f"Pesos--> ${cambio_dolares_pesos(dolares):.2f}")
    elif opcion==3:
         break
    else:
        print("Se equivocó de opción de Menú")
print()