nome = input('Qual seu nome: ')
print(f'O seu nome é {nome}')


frase = 'Ola,bem vindo a este treinamento'
print(type(frase))
print(frase.split(','))
print(type(frase))


# Manipulando datas
# Descobrindo quanto tempo falta para meu próximo aniversário

from datetime import datetime

data_atual = datetime.now()
data_aniversario = datetime.strptime (input('Data de aniversario: '), '%d/%m/%Y')
proximo_aniversario = data_aniversario - data_atual

print(f'Próximo aniversário: {proximo_aniversario.days} dias')

import random
cores = ['verde', 'azul', 'preto']
print(random.choices(cores))

#Valor aleatório em um intervalo (float)
print(random.uniform(4,10))

#Valor aleatório em um intervalo (int)
print(random.randint(4,10))

#Valor aleatório do conteúdo de uma lista
cores = ['verde', 'azul', 'preto']
print(random.choices(cores))

#Posso pedir mais de um valor aleatório usando uma variavel k
cores = ['verde', 'azul', 'preto']
print(random.choices(cores, k=2))

#embaralhar
cartas = ['carta1','carta2','carta3','carta4']
random.shuffle(cartas)
print(cartas)


#Atalhos

# ctrl + k > c = identar linha
# ctrl + k > u = desidentar linha12

""" shift + alt + a comenta bloco de código """

cartas = ['carta1','carta2','carta3','carta4']
















