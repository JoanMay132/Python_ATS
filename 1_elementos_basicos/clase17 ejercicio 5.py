#Ejercicio 5
'''una tienda ofrece un descuento del 15% sobre el total de la
compra y un cliente desea saber cuánto deberá pagar
finalmente por su compra'''

precio= float(input("Digite el precio: "))
descuento=precio*0.15
precio_final=precio-descuento
print(f"El valor de su compra con descuento es ${precio_final:.2f}")