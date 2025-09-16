from models.pessoa import Pessoa

class Cliente(Pessoa):
    lista_de_clientes = []

    def __init__(self, nome, sobrenome) -> None:
        super().__init__(nome, sobrenome)
        self.lista_de_produtos = []
        Cliente.lista_de_clientes.append(self)

    @classmethod
    def listar_de_clientes(cls):
        return cls.lista_de_clientes
