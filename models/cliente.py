from models.pessoa import Pessoa


class Cliente(Pessoa):
    lista_de_clientes = []

    def __init__(self, nome, sobrenome) -> None:
        super().__init__(nome, sobrenome)
        self.is_active = True
        Cliente.lista_de_clientes.append(self)

    @classmethod
    def listar_de_clientes(cls):
        return cls.lista_de_clientes


def listar_clientes(cliente):
    if cliente is None:
        print("Nenhum cliente ativo")
        return

    print("\nTODOS OS CLIENTES CADASTRADOS:")
    clientes = Cliente.listar_de_clientes()
    if clientes:
        for i, client in enumerate(clientes, 1):
            status = "ATIVO" if client.is_active else "INATIVO"
            print(f"[{i}] {client.nome_completo} - {status}")
    else:
        print("Nenhum cliente cadastrado ainda!")
    print()
