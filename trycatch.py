try:
    valor = int(input('Digite um valor: '))
    print (valor * 10.2)
except:
    print('Favor digitar apenas números')

try:
    meses = [1,2,3,4,5,6,7,8,9,10,11,12]
    print(meses[15])
except IndexError as erro:
    print('Favor acessar um índice válido')
    print(erro)

internet = None
try:
    print('Fazendo conexao com a' + internet)
except TypeError as erro:
    print('Não há conexão com a internet')
finally:
    print('Desfazendo a compra!')
    
#Finally é a execução do código mesmo com erro.



