from models.produto import Produto
from models.cliente import Cliente
from utils.io import input_text


lista_produtos = [
    Produto('Mochila', 149.90, 3),
    Produto('Fone de Ouvido', 89.90, 5),
    Produto('Camiseta', 39.90, 10),
    Produto('Garrafa Térmica', 59.90, 8),
    Produto('Caneta Azul', 2.50, 100)
]

def exibir_produtos():
    for produto in lista_produtos:
        estoque = f"Estoque [{produto.estoque}]"
        preco = f'{produto.preco:.2f}'
        disponivel = 'Disponível' if produto.disponivel else 'Indisponível'
        print(f"{produto} {preco} {estoque} {disponivel}")
    print()


def cadastrar_cliente():
    nome = input_text('Nome')
    sobrenome = input_text('Sobrenome')
    cliente = Cliente(nome, sobrenome)
    print(f"Cliente: {nome} {sobrenome} cadastrado com sucesso!")
    return cliente

def exbir_cliente(cliente):
    for i in cliente.listar_de_clientes():
        print(i)
    print()
