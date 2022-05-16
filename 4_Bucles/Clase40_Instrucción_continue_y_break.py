#Instrucción continue y break

for i in range(10):
    #continue va a obviar lo que sigue después
    #break va a terminar en cuanto llegue a la interación
    if i==5:
        break #se detiene en cuanto llega al elemento 5
    print(i)
print("programa finalizado")

for i in range(10):
    if i==5:
        continue # Obvia lo que hay después de lo que se definió en if
    print(i)