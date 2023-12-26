#We can use the Python built-in function map() to apply a function to each item in an iterable (like a list or dictionary) and return a new iterator for retrieving the results
# A ideia é aplicar uma funcao evitando o uso da estrutura de repeticao for.
# O map vai editar os itens da lista, ou seja, a função onde será aplicada já faz alterações nos itens.
# map é mais rápido e prático que o for
# Enquanto o filter vai filtrar itens em uma lista, mas vai retornar apenas verdadeiro ou falso, nele, não vamos fazer nenhuma alteração na lista.
# Perceba que a principal diferença está na função, no caso do filter o resultado é somente dos valores que atendem a condição

precos = [12,34,42,57,99,232]
print (f'Lista original: {precos}')

#MAP
def aumenta_precos(valor):
    if valor < 50:
        return valor * 1.5
    else:
        return valor

print (f'Aplicado o aumento: {list(map(aumenta_precos, precos))}') #Um objeto map retorna um valor do tipo map, por isso precisamos converter isso em uma lista
    

#FILTER
def valores_acima_50(valor):
    if valor > 50:
        return True
    else:
        return False


print (f'Valores acima de 50: {list(filter(valores_acima_50, precos))}')


# Iterando em uma lista de lista

pintura = [
    ['Classica', 'Azul', 1857],
    ['Medieval', 'Vermelha', 1867],
    ['Moderna', 'Verde', 1897]
]

def ehantiga(value):
    if value[2] < 1890:
        return True
    else:
        return False 
    
print (f'Pintura antiguidade: {list(filter(ehantiga, pintura))}')
    
















