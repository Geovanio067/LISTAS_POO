class Solicitante:
    def __init__(self, nome):
        self.nome = nome
class Biblioteca:
    def __init__(self):
        self.livros = [
            'Turma da monica','Diario de um banana', 'O Deus que detroi sonhos',
            'O Pequeno Príncipe', 'A Culpa é das Estrelas', '48 leis do poder',
            'Arte da guerra', 'O Alquimista',      ]
    def mostrar_livros(self):
        for i, l in enumerate(self.livros, 1):
            print(f'{i}. {l}')
    def escolher_livro(self, opcao):
        return self.livros[opcao - 1]
class Sistema:
    def iniciar(self):
        nome = input('Nome do alugador: ')
        s = Solicitante(nome)
        b = Biblioteca()
        b.mostrar_livros()
        escolha = int(input('Escolha o livro (número): '))
        livro = b.escolher_livro(escolha)
        print(f'{s.nome} alugou: {livro}')
Sistema().iniciar()