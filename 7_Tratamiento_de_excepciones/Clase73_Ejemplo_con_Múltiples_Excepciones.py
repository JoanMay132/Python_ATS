#Excepciones

'''¿Cómo capturar multiples excepciones?'''


def dividir():
    while True:
        try:
            num1=float(input("Digite un número: "))
            num2=float(input("Digite otro número: "))
            resultado= num1/num2
            print(f"El resultado de la división es {resultado:.2f}")
        except ValueError:
            print("Error -> Digite correctamente los valores númericos")
        except ZeroDivisionError:
            print("Error -> No se puede dividir entre 0")

        else:
            break

dividir()