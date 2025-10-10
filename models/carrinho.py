from models.produto import Produto
from collections import Counter


class Carrinho:
    itens = []

    @classmethod
    def adicionar_produto(cls, cliente, produto: Produto, qtd: int = 1):
        if produto.disponivel(qtd):
            for _ in range(qtd):
                cls.itens.append((cliente, produto))
                produto.reservar(1)
            return True
        return False

    @classmethod
    def cancelar(cls, cliente_parametro):
        for cliente, produto in cls.itens:
            if cliente.nome_completo.__eq__(cliente_parametro.nome_completo):
                produto.cancelar_compra()

    @classmethod
    def finalizar_compra(cls, cliente_parametro):
        produto_copia = []
        for cliente, produto in cls.itens[:]:
            if cliente.nome_completo.__eq__(cliente_parametro.nome_completo):
                produto_copia.append(produto.nome)
                cls.itens.remove((cliente, produto))
        return produto_copia
