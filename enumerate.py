#Enumerate

#Eu não tenho um indice visível nas interações em lista, como no for em c: que eu tenho uma variavel 'i' que vai sendo incrementada, e a qualquer momento eu sei qual é o valor dela. O enumerate serve para trabalhar com os índices quando necessário.

#Exemplo
#indice é o indice da interacao
#o que vai dentro da funcao enumarate, é o elemento que está sendo iterado

nomes = ['Rafael', 'Cavalo', 'Pedro']

for indice in enumerate(nomes):
    print(indice)
    print('----------------------')

# Posso acessar tanto o indice, quanto o valor naquele indice
for indice in enumerate(nomes):
    print(indice[0])
    print(indice[1])
    print('----------------------')
    
#Aqui eu estou guardando na variavel nome, o valor iterado da lista nomes
for indice, nome in enumerate(nomes):
    print(f'indice: {indice}, valor: {nome}')
    print('----------------------')

#Comparado com o for tradicional
for i in nomes:
    print(i)


