class Cliente:
    def __init__(self, nome):
        self.nome = nome
class Feira:
    def __init__(self):
        self.frutas = ['Maçã', 'Banana', 'Laranja', 'Uva', 'Abacaxi', 'Melancia']
    def mostrar_frutas(self):
        for i, f in enumerate(self.frutas, 1):
            print(f'{i}. {f}')
    def escolher_fruta(self, opcao):
        return self.frutas[opcao - 1]
class Sistema:
    def iniciar(self):
        nome = input('Seu nome: ')
        c = Cliente(nome)
        f = Feira()
        f.mostrar_frutas()
        escolha = int(input('Escolha a fruta (número): '))
        fruta = f.escolher_fruta(escolha)
        print(f'{c.nome} escolheu: {fruta}.')
Sistema().iniciar()