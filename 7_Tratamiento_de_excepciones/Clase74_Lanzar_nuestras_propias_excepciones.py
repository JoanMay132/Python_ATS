# Lanzar nuestras propias excepciones

def verificandoedad(edad):
    if edad<0: #La edad es negativa
        raise ValueError ("La edad no puede ser negativa")#Lanzar mi propia excepción
    elif edad<18:
        print("Eres muy joven")
    elif edad<30:
        print("Eres joven")
    elif edad<50:
        print("Eres maduro")

edad=int(input("Digite su edad: "))
try:
    verificandoedad(edad)
except ValueError as Edadnegativa:
    print(Edadnegativa)
print("Programa terminado")