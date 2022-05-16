"""
Ejercicio 8
Hacer un programa que simule un cajero automático con un saldo
inicial de $1000 y tendrá el siguiente menú de opciones:
    1. Ingresar dinero en la cuenta
    2. Retirar dinero de la cuenta
    3. Mostrar dinero disponible
    4. Salir
"""
saldo=1000
while True:
    print("\t .:MENU:.")
    print("1.- Ingresar dinero en la cuenta")
    print("2. Retirar dinero de la cuenta")
    print("3. Mostrar dinero disponible")
    print("4. Salir")
    opcion=int(input("Digite un número del menu: "))
    print()
    if opcion==1:
        ingresar= int(input("¿Cuánto dinero desea ingresar? "))
        saldo+=ingresar
        print(f"Su saldo es de ${saldo} ")
    elif opcion==2:
        retirar=int(input("¿Cuánto dinero desea retirar? "))
        if retirar>saldo:
            print("No cuenta con ese saldo")
        else:
            saldo-=retirar
            print(f"Su nuevo saldo es ${saldo}")
    elif opcion==3:
        print(f"Su saldo es ${saldo}")
    elif opcion==4:
        print("Ha salido del cajero")
        break
    else:
        print("Se ha equivocado de número")
    print()