from datetime import datetime
import random

# nome = input('Informe seu nome: ')
# data_aniversario = datetime.strptime (input('Data de nascimento: '), '%d/%m/%Y')
nome ='Rafael de Andrade'
data_aniversario = datetime.strptime('12/05/1987', '%d/%m/%Y')
data_cadastro = datetime.now()
idade = data_cadastro - data_aniversario
cartoes = ['R$50,00','R$120,00','R$250,00']
cartao = random.choice(cartoes)

print(f'Olá {nome} seu registro foi concluído com sucesso no dia {data_cadastro.day}/{data_cadastro.month}/{data_cadastro.year}')
print(f'Parabéns, você ganhou um cartão de compras no valor de {cartao}')





