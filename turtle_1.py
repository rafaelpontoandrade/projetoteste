from turtle import Turtle

# Inicializar uma turtle
t = Turtle()

""" # Definir a velocidade
t.speed(1)

#Movimentar a turtle para frente em px
t.forward(100)

#Rotacionar em x graus para a direita
t.right(90)
t.forward(100)

#Rotacionar em x graus para a esquerda
t.left(90)
t.forward(100)

#Movimentar a turtle para trás em px
t.backward(200)

#o input aqui será só para a janela não fechar quando a gente realizar os movimentos acima
input()
 """

jogar = True
continuar = 'S'

while jogar == True:
    
    direcao = input('Qual a direcao do movimento: F para frente | T para trás ')
    rotacao = int(input('Qual a rotacao do movimento: '))
    distancia = int(input('qual a distancia do movimento: '))

    if rotacao >= 0:
        t.right(rotacao)
    else:
        t.left(abs(rotacao))

    if direcao == 'F':
        t.forward(distancia)
    else:
        t.backward(distancia)
    
    continuar = input('Continuar jogando? S ou N ')

    if continuar in ('N', 'n', 'nao'):
        break 
