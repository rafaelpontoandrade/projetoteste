#Decorators são uma funcionalidade poderosa em Python que permitem adicionar funcionalidades extras a uma função existente sem modificar seu código fonte. Um decorator é uma função que recebe outra função como argumento e retorna uma nova função com a adição das funcionalidades desejadas.
#Decorator é um design pattern

#exemplo
def meu_decorator(funcao):
    def wrapper():
        print('Antes')
        funcao() #aqui eh a referencia da minha funcao parabens
        print('Depois')
    return wrapper

def parabens():
    print('Parabens')

#Resultado recebeu a referencia da funcao wrapper()
resultado = meu_decorator(parabens)
resultado()

print('------------------')

# Pensando bem nesse decorato. A funcao parabéns pode ser alterada ou acrescentar o que eu quiser, que não vai ser necessário alterar a funcao decorator.

# Existe uma maneira ainda mais enxugada de escrever um decorator:
def meu_decorator2(funcao):
    def wrapper():
        print('Antes2')
        funcao() #aqui eh a referencia da minha funcao parabens2
        print('Depois2')
    return wrapper

@meu_decorator2
def parabens2():
    print('Parabens2')

parabens2()

