#Ejercicio 5
'''Hacer un programa que simule un cajero automático con un
saldo inicial de $1000 y tendrá el siguiente menú de opciones
1. Ingresar dinero a la cuenta
2. Retirar dinero de la cuenta
3. Mostrar dinero disponible
4. Salir'''
saldo= 1000
print("\t.:MENU:.")
print("1. Ingresar dinero a la cuenta: ")
print("2. Retirar dinero de la cuenta")
print("3. Mostrar dinero disponible")
print("4. Salir")
opcion=int(input("Digite una opción del menu: "))
if opcion==1:
    extra=float(input("\n¿Cuánto dinero desea ingresar? "))
    saldo+=extra
    saldo=print(f"\nSu nuevo saldo es de {saldo}")
elif opcion==2:
    retirar=float(input(f"\n¿Cuánto dinero desea retirar? "))
    if retirar>saldo:
        print("No cuenta con esa cantidad")
    else:
         saldo-=retirar
         print(f"\nSu saldo es de {saldo}")
elif opcion==3:
    print(f"\nSu saldo es de {saldo}")
elif opcion==4:
    print("\nGracias por usar el cajero")
else:
    print("\n Error, Se equivocó de opción!!!")