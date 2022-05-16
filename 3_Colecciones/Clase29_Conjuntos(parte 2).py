#Conjuntos
a=set() #primero se pone set paraa conjunto vacío

a=({1,2,3}) #frozenset({}) los vuelve inmutables, parecido a una tupla
#pero los conjuntos no acepta duplicados
b= {3,4,5}
#c= a|b # | permite la unión de dos conjuntos
#c= a & b # & permite la intersección entre dos conjuntos
#c= a-b # a-b enseña los elementos que están en a pero no en b
#c=b-a # b-a enseña los elementos en b pero no en a
#c= a ^ b #enseña elementos que no intersectan
c= {1,2,3,4,5}
print(a==b)
print(len(a))
print(c)
# operaciones que se pueden realizar en los conjuntos
print(a.issubset(c)) # .issubset() muestra si los elementos de a están en c (subconjunto)
print(b.issubset(c))
print(c.issuperset(a)) #enseña si están todos los elementos de c en a
print(a.isdisjoint(b)) #enseña si son disconexos (no comparten elementos en común)
