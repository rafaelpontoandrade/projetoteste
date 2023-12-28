def boasvindas():
    print('Bem vindos')

boasvindas()

print('------------------')

def bemvindo(nome):
    print(f'Bem-vindo {nome}')

bemvindo('Rafael')

print('-------------------')

# Posso definir um valor padrão para o argumento
# Se eu quiser usar o valor padrão, basta não passar nenhum argumento na chamada da função.

def valorpadrao(valor='Valor Padrao'):
    print(valor)

valorpadrao()
valorpadrao('sobescrevendo o valor padrao')

print('------------------')

# Quando eu tenho dois parâmetros minha funcao, e um deles tem um valor setado. Essa variável deve estar na última posição
#Exemplo

def valorpadrao2(valor, valor2='Valor Padrao'):
    print(f'{valor} {valor2}')

valorpadrao2('Casa')

print('------------------')

# Outra coisa em Python é a diferença dos argumentos. Temos os argumentos posicionais, que é como eu já sei, mando os arguimentos na ordem da funcao.
# funcaoexemplo(argumento1, argumento2) e na chamada eu sei que o primeiro argumento na chamada vai para o arguimento1 e o segundo para o argumento 2
# Porém, em Python tem como eu mandar na ordem que eu quiser (argumentos nomeados), mas deixando explícito na chamada qual argumento é qual.

# Exemplo

def exibir_preco(nome_produto, preco):
    print (f'{nome_produto} custa {preco}')

exibir_preco(preco=10, nome_produto='chinelo')

# Para obrigar o a funcao a ser do tipo Argumento nomeado, basta eu colocar um * e tudo que vier pra frente dele, o usuário precisa deixar explícito para quem ele vai passar o valor.

# Exemplo

def exibir_preco2(*, nome_produto, preco):
    print (f'{nome_produto} custa {preco}')

exibir_preco2(nome_produto = 'panetone', preco = 10)

# Além disso, posso deixar parcial como Arguimento nomeado.

def exibir_preco3(nome_produto, *, preco):
    print (f'{nome_produto} custa {preco}')

exibir_preco3('caju', preco = 30)


# Em Python eu também consigo ter quantidade de valores dinamicos em chamada de funçoes
# quando eu coloco um * antes da variavel, eu sinalizo que ela pode receber diversos valores
# Porém, o últumo elemento precisa ser nomeado na chamada da funcao, para o Python saber onde acaba os multiplos valores das variaveis que sao marcadas como multivaloradas
# Exempo

def somar(*valores, b):
    print(valores)
    for valor in valores:
        b += valor
    print(b)

somar (10, 20, 30, b=10)

print('------------------------')

# Eu também consigo fazer o envio de multiplos valores nomeados, para isso eu marco o parametro com **
# Exemplo


def concatenar(nome, *valores, **valores_nomeados):
    print(nome)
    for valor in valores:
        print(valor)
    for valor in valores_nomeados.values():
        print(valor)


concatenar ('Rafael', 10, 20, 30, a=10, b=11, c=12)
















