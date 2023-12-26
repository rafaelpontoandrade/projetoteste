pessoa = ['Carol', 18, 1.60]
print(pessoa)

#Porem, dessa forma, eu não sei o que significa o valor 18, 1.60
#Poderia criar essa lista da seguinte maneira:

dicionario_pessoa = {'nome': 'Carol', 'idade': 18, 'altura': 1.60}
print(dicionario_pessoa)

#acessar um elemento
print(dicionario_pessoa['idade'])

#Imprimir todas as chaves existentes
print(dicionario_pessoa.keys())

#Imprimir todos os valores
print(dicionario_pessoa.values())

#Imprimir tanto as chaves, quanto os valores
print(dicionario_pessoa.items())

print('-----------------------------------------')

#Iterar sobre um dicionário
for item in dicionario_pessoa.items():
    print(item[0]) #corresponde a chave
    print(item[1]) #correponde ao valor


#Aqui vou criar uma lista de dicionarios, para armazenar varias pessoas
pessoas = [{'nome': 'Rafael', 'idade': 30, 'altura': 1.68}, {'nome': 'Carol', 'idade': 18, 'altura': 1.60}, {'nome': 'Juca', 'idade': 58, 'altura': 1.99}]
print(pessoas)
print('-----------------------')

for x in pessoas:
    print(x)
    print(x['nome'], x['idade'])
    print('----------')

# Ordenar lista de dicionario
# Para ordenar essa lista eu preciso usar uma biblioteca extra.
from operator import itemgetter

pessoas.sort(key=itemgetter('nome'))
print('-----------ordenar-------------')
print(pessoas)
print('----------fimordenar-----------')

#Em alguns casos, eu posso ter uma colecao sem uma chave

produtos = [('Celular', 750), ('TV', 1750), ('Carro', 7350)]
print(produtos)

# Para ordenar esse tipo de colecao, eu posso passar ao invés da chave, o indice
# Ex:
produtos.sort(key=itemgetter(0))
print('-----------------------')
print(produtos)
print('-----------------------')

#Da mesma forma eu posso usar para ordenar matriz

matriz = [[5,10],[88,56],[3,14]]
print(matriz)
matriz.sort(key=itemgetter(0))
print('---------Ordenar_Matriz------------------')
print(matriz)
print('---------Fim_Ordenar_Matriz--------------')

#Outro exemplo
#Ordenar em ordem decrescente pelo indice 1

equipamentos = [('Tripe', 300), ('Camera', 14000), ('Flash', 900), ('Bolsa', 200)]
print(equipamentos)

equipamentos.sort(key=itemgetter(1), reverse=True)
print(equipamentos)













