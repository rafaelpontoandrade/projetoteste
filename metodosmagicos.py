class Livro:
    def __init__(self, titulo, autor, paginas):
        # Método construtor: inicializa cada nova instância da classe.
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def __str__(self):
        # Método para definir a representação em string da instância.
        # Chamado pela função print() e pela função str().
        return f"{self.titulo} por {self.autor}"

    def __repr__(self):
        # Método para definir a representação oficial da instância.
        # Útil para depuração. Chamado pela função repr().
        return f"Livro('{self.titulo}', '{self.autor}', {self.paginas})"

    def __len__(self):
        # Método para retornar o 'tamanho' do objeto.
        # Neste caso, o número de páginas do livro.
        return self.paginas

# Criando uma instância da classe Livro
meu_livro = Livro("1984", "George Orwell", 328)

# Usando os métodos mágicos
print(meu_livro)  # Usa __str__: "1984 por George Orwell"
print(repr(meu_livro))  # Usa __repr__: "Livro('1984', 'George Orwell', 328)"
print(len(meu_livro))  # Usa __len__: 328
