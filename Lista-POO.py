class Viajante:
    def __init__(self, nome):
        self.nome = nome
class Viagem:
    def __init__(self):
        self.destinos = ['xique-xique', 'maranhão', 'maimi', 'petrolandia', 'juazeiro do norte']
    def mostrar_destinos(self):
        print('disponíveis:')
        for i, destino in enumerate(self.destinos, 1):
            print(f"{i}. {destino}")
    def escolher_destino(self, indice):
        return self.destinos[indice - 1]
class SistemaViagem:
    def iniciar(self):
        nome = input('Digite o nome do viajante:')
        viajante = Viajante(nome)
        viagem = Viagem()
        viagem.mostrar_destinos()
        escolha = int(input('Escolha o número da viajem: '))
        destino_escolhido = viagem.escolher_destino(escolha)
        print(f'{viajante.nome} escolheu viajar para {destino_escolhido}.')
SistemaViagem().iniciar()