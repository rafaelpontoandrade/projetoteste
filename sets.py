# Conjuntos são coleções não ordenadas e não indexadas. Eles são úteis quando você precisa de uma coleção que não permita elementos duplicados e a ordem dos elementos não é importante. Conjuntos também oferecem operações matemáticas de conjuntos, como união, interseção, diferença, etc.

 # Exemplo

numeros =[2,3,4,5,5,6,6]
set_numeros = set(numeros)
print(set_numeros)

#Como o set nao premite itens duplicados, ele removeu os duplicados
# Com set eu posso usar as configurações de conjuntos matematicos: uniao, interseção, diferenca.

#Exemplo

numeros2 = [1,4,5,6,11,23]
set_numeros2 = set(numeros2)
print(set_numeros2)
print('--------------------------')

#Aqui eu imprimo apenas os numeros que aparecem uma única vez quando combinados os dois set's
print(set_numeros.symmetric_difference(set_numeros2))

#Aqui eu imprimo a interseção, ou seja, os números que aparecem em ambos casos
print(set_numeros.intersection(set_numeros2))

#Aqui eu imprimo a uniao, removendo os duplicados
print(set_numeros.union(set_numeros2))





