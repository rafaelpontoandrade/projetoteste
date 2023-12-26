# Em Python, um método de classe é um método que pertence à classe em si e não a uma instância específica da classe. Ele tem acesso à classe através do primeiro parâmetro, geralmente chamado de cls. Já um método estático não tem acesso nem à classe (cls) nem à instância (self), e pode ser pensado como uma função regular que pertence ao namespace da classe.

class Carro:
    numero_de_carros = 0  # Atributo de classe

    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        Carro.numero_de_carros += 1

    def exibir_info(self):
        print(f"Marca: {self.marca}, Modelo: {self.modelo}")

    @classmethod
    def total_de_carros(cls):
        print(f"Total de carros: {cls.numero_de_carros}")

    @staticmethod
    def info_geral():
        print("Carros são meios de transporte usados para locomoção terrestre.")

# Criando objetos da classe Carro
carro1 = Carro("Toyota", "Corolla")
carro2 = Carro("Honda", "Civic")

# Usando um método de instância
carro1.exibir_info()

# Usando um método de classe
Carro.total_de_carros()

# Usando um método estático
Carro.info_geral()


# numero_de_carros é um atributo de classe que mantém a contagem do número total de carros criados.
# exibir_info é um método de instância que acessa os atributos da instância (self.marca e self.modelo).
# total_de_carros é um método de classe que acessa o atributo de classe numero_de_carros através do cls.
# info_geral é um método estático que simplesmente imprime uma informação geral e não acessa nenhum atributo ou método específico da classe ou instância.
# Os métodos de classe são úteis quando você precisa de uma função que está relacionada à classe, mas não necessariamente a uma instância específica, enquanto os métodos estáticos são usados para funções que pertencem à classe, mas que são independentes tanto da classe quanto das instâncias.
