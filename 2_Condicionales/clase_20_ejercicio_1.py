'''ejercicio 1
Hacer un programa que pida 2 números y se de cuenta cual de 
ellos es par o si ambos lo son'''

num1= int(input("Digite un número: "))
num2= int(input("Digite otro número: "))

if num1%2==0 and num2%2==0:
    print("Ambos números son pares")
elif num1%2==0 and num2%2!=0:
    print(f"{num1} es par")
elif num1%2!=0 and num2%2==0:
    print(f"{num2} es par")
else:
    print("Ambos números son impares")













