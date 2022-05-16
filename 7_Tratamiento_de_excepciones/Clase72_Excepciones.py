# Errores
while True:
    try:
        numero=int(input("Digite un número: "))
        print(f"La suma es: {numero+10}")

    except:
        print("Ha ocurrido un error")
    else:
        print("Programa finalizado correctamente")
        break
    finally: #se ejecuta siempre con el try y except
        print("Iteración finalizada")

print("Programa terminado")


 # Try, except, else son para excepciones