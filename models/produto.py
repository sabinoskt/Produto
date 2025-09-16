class Produto:
    def __init__(self, produtos: str, preco: float, estoque: int) -> None:
        self.produtos = produtos
        self.preco = preco
        self.estoque = estoque

    def __str__(self):
        return f"{self.produtos}"

    @property
    def disponivel(self):
        return self.estoque > 0


    def comprado(self):
        self.estoque -= 1
