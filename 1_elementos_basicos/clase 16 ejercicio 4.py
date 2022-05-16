'''Ejercicio 4
Ingresar el radio de un circulo y se reporte su
área y la longitud de la circunferencia'''
import math

radio = float(input("Ponga el valor del radio: "))
area = math.pi *radio**2
longitud= 2*math.pi*radio
print(f"El area es: {area:.2f}")
print(f"La longitud de la circunferencia es: {longitud:.2f}")

