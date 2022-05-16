#Funciones Recursivas

def cuenta_regresiva(num):
    if num>0:
        print(num)
        cuenta_regresiva(num - 1)
    else:
        print("BOOOOOM!!!")

cuenta_regresiva(3**2)