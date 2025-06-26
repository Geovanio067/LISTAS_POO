class Contato:
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone
    def __str__(self):
        return f'{self.nome} - {self.telefone}'
class Agenda:
    def __init__(self):
        self.contatos = []
    def adicionar(self, contato):
        self.contatos.append(contato)
    def listar(self):
        for c in self.contatos:
            print(c)
agenda = Agenda()
agenda.adicionar(Contato('macedo', '87-9121467'))
agenda.adicionar(Contato('xamã', '74-9122765'))
agenda.listar()