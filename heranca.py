# Classe Base
class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def exibir_info(self):
        print(f"Marca: {self.marca}, Modelo: {self.modelo}")

# Classe Derivada
class Carro(Veiculo):
    def __init__(self, marca, modelo, num_portas):
        super().__init__(marca, modelo)
        self.num_portas = num_portas

    def exibir_info_carro(self):
        print(f"Marca: {self.marca}, Modelo: {self.modelo}, Portas: {self.num_portas}")

# Criando um objeto da classe Carro
meu_carro = Carro("Toyota", "Corolla", 4)

# Usando métodos da classe Carro
meu_carro.exibir_info()
meu_carro.exibir_info_carro()


# Métodos mágicos (Magic Methods, dunder methods (double underscore))

class Pessoa:
    def __init__(self):
        self.nome = 'Sou uma pessoa'
# self.nome = 'Sou uma pessoa' - Aqui, um atributo chamado nome é criado e atribuído um valor inicial 'Sou uma pessoa'. Este atributo nome será parte de cada instância da classe Pessoa.

pessoa = Pessoa()
print(pessoa.nome)


