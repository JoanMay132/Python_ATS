''' Capítulo 4: 4_Bucles
Ejercicio 9:
° Hacer un programa donde el usuario ingrese una frase, se le devolverá
la misma frase pero sin espacios en blanco y además un contador de cuántos
caracteres tiene la frase (sin contar los espacios en blanco).

Ejemplo:
 Frase: Hola que tal?
 Frase final: Holaquetal?
 N° de caracteres: 11'''
frase= input("Digite una frase: ")
frase2= ""
for i in frase:
    if i!=" ":
        frase2+=i
frase=frase2
print(f"La frase es: \n{frase}")
print(f"El número de caracteres es: \n{len(frase)}")
