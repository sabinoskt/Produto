from models.produto import Produto
from collections import Counter


class Carrinho:
    def __init__(self, cliente=None):
        self.cliente = cliente
        self.itens = []

    def adicionar_produto(self, produto: Produto, qtd: int = 1):
        if produto.disponivel(qtd):
            for _ in range(qtd):
                self.itens.append(produto)
            return True
        return False

    def calcular_total(self) -> float:
        return sum(produto.preco for produto in self.itens)

    def obter_resumo(self):
        return Counter(self.itens)

    def limpar(self):
        self.itens.clear()

    def finalizar_compra(self):
        for produto in self.itens:
            produto.reservar(1)
        self.itens.clear()
