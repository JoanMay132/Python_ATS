#Funciones con retorno de valor

def multiplicar(num1,num2):
    mult= num1*num2
    return mult
mult=multiplicar(3,4) #te retorna un valor
print(mult)
print(multiplicar(6,8))
print(multiplicar(3,9))

def prueba():
    return "hola",45,[1,2,3]
print(prueba()) #retorna una tupla

c,n,l=prueba()
print(c)
print(n)
print(l)