#Listas
#Colecoes em Python: Listas, Tuplas, Conjuntos e Dicionários

precos = [10,20,100, 5, 2, 11, 1, 12]

print (precos[0])
print(precos.index(100)) #estou procurando o valor 100 na lista e retornando o índice

#Listas em Python são dinâmicas (aceitam qualquer tipo de dados)
itens = [1, 3, 6, 'Olá', True, 10.6]

#Maneiras diferentes de gerar uma lista

#Multiplicação de valores
lista_de_noves = [9] * 10 #estou gerando uma lista com dez números 9.
lista_de_teste = ['teste'] * 10
print(lista_de_noves)
print(lista_de_teste)

#Usando um gerador Range

#Ex: 0 até 29
faixa_de_numeros = list(range(30))
print(faixa_de_numeros)

#Gerar a partir de strings
letras_da_frase = list('Bem-Vindo')
print(letras_da_frase)

#Matriz em Python
matriz_ = [['Rafael', 30], ['Carol', 19]]
print(matriz_[0][0], matriz_[0][1])

# Adicionar elementos
valores = [1, 2, 3]
anos = [2020,2021]

#Adicionar ao final da lista
valores.append(4)
print(valores)

#Adicionar em uma posicao específica
valores.insert(0,2033)
print(valores)

#Unir listas
valores.extend(anos)
print(valores)

#Extrair um elemento com base no indice
valor0 = valores.pop(0) #como ele retorna o valor que foi removido,eu posso atribuir ele em alguma variável, por exemplo.
print(valores)
print(valor0)

#Remover item da lista com base no valor
valores.remove(2021)
print(valores)

#Remover item da lista com base no índice
del valores[0]
print(valores)

#Remover uma faixa de valores com base no índice
del valores[2:6]
print(valores)

#Contanto quantas vezes tem a ocorrência de algum valor
print (valores.count(2))

#Resetar lista
valores.clear()


print(precos)


#Inverter ordem dos elementos
precos.reverse()
print(precos)

#Ordenar lista
precos.sort() 
print(precos)

precos.sort(reverse=True)
print(precos)


#Trabalhar com multiplas listas usando o ZIP

a_lista = ['A','B','C','D','E']
b_lista = [1,2,3,4,5]

for a,b in zip(a_lista,b_lista):
    print(a)
    print(b)

#porem caso eu precisa interar com multiplas listas, e elas tem tamanhos diferentes, eu posso usar
#a biblioteca from itertools import zip_longest
    
from itertools import zip_longest

a_lista = ['A','B','C','D','E']
b_lista = [1,2,]

for a,b in zip_longest(a_lista, b_lista):
    print(f'lista A: {a} lista B: {b}')











