class Afazer:
    def __init__(self, titulo, descricao=''):
        self.titulo = titulo
        self.descricao = descricao
    
    def __hash__(self):
        return hash(self.titulo)
    
    def __eq__(self, outro):
        return self.titulo == outro.titulo
    
    def __str__(self):
        if self.descricao:
            return f'{self.titulo} - {self.descricao}'
        return self.titulo
class Agenda:
    def __init__(self, data):
        self.data = data
        self.afazeres = set()
    def add_afazer(self, afazer):
        self.afazeres.add(afazer) 
    def listar(self):
        print(f'Agenda do dia: {self.data}')
        if not self.afazeres:
            print('Nenhum afazer para hoje.')
            return
        for afazer in self.afazeres:
            print(f'- {afazer}')
agenda = Agenda('26/06/2025')
agenda.add_afazer(Afazer('Comprar mantimentos', 'Leite, ovos, pão'))
agenda.add_afazer(Afazer('Estudar Python'))
agenda.add_afazer(Afazer('Exercício físico', 'Corrida de 30 minutos'))
agenda.listar()
