class Produto:
    def __init__(self, nome: str, preco: float, estoque: int) -> None:
        self.nome = nome
        self.preco = preco
        self.estoque = estoque

    def __str__(self):
        return f"{self.nome} {self.preco} {self.estoque}"

    def __repr__(self):
        return f"{self.nome} {self.preco} {self.estoque}"

    def disponivel(self, qtd: int = 1) -> bool:
        return self.estoque >= qtd

    def reservar(self, qtd: int = 1) -> bool:
        if self.disponivel(qtd):
            self.estoque -= qtd
            return True
        return False

    def cancelar_compra(self):
        self.estoque += 1
