from models.produto import Produto
from models.cliente import Cliente
from utils.io import input_text, input_num, input_confirmacao
from models.carrinho import Carrinho

LISTA_PRODUTOS = [
    Produto('Mochila', 149.90, 3),
    Produto('Fone de Ouvido', 89.90, 5),
    Produto('Camiseta', 39.90, 10),
    Produto('Garrafa Térmica', 59.90, 8),
    Produto('Caneta Azul', 2.50, 100)
]


def exibir_produtos(produtos):
    print('*'*68)
    print(" TABELA DE PRODUTOS ".center(68))
    print('*'*68)

    for i, produto in enumerate(produtos):
        status = 'Disponível' if produto.disponivel() else 'Indisponível'
        print(f"[{i:02d}] {produto.nome:<20} | R$ {produto.preco:>8.2f} | "
              f"Estoque: {produto.estoque:>3} | {status}")
    print('*'*68)
    print()


def escolher_produtos_para_compra() -> tuple[Produto, int]:
    produtos = LISTA_PRODUTOS
    exibir_produtos(produtos)

    indice = input_num('Escolha o produto', minimo=0, maximo=len(produtos)-1)
    produto_escolhiddo = produtos[indice]

    if not produto_escolhiddo.disponivel():
        print("Produto esgotado!")
        return None, 0

    print(f"\n Produto: {produto_escolhiddo.nome}")
    print(f"Preço unitário: R$ {produto_escolhiddo.preco}")
    print(f"Estoque disponivel: {produto_escolhiddo.estoque}")

    quantidade = input_num('Quantidade desejada', minimo=1, maximo=produto_escolhiddo.estoque)
    return produto_escolhiddo, quantidade


def cadastrar_cliente():
    print('*'*50)
    print(" CADASTRO DE CLIENTE ".center(50))
    print('*'*50)

    nome = input_text('Nome')
    sobrenome = input_text('Sobrenome')

    try:
        cliente = Cliente(nome, sobrenome)
        print(f"\nCliente {cliente.nome_completo} cadastrado com sucesso!\n")
        print(f"Total de clientes {len(Cliente.listar_de_clientes())}")
        return cliente
    except ValueError as e:
        print(f"Erro no cadastro: {e}")
        return None


def escolher_cliente(cliente=None):
    if cliente is None:
        print("Nenhum cliente ativo!")
        return None

    if len(cliente.listar_de_clientes()) > 1:
        print('\n*' * 20)
        print("ESCOLHA O CLIENTE")
        print('*' * 20)

        for i, client in enumerate(cliente.listar_de_clientes()):
            print(f"[{i:02d}] {client}")
        print()
        indice = input_num('Opção', minimo=0, maximo=len(cliente.listar_de_clientes()))
        return cliente.listar_de_clientes()[indice]
    return cliente.listar_de_clientes()[0]


def fazer_compra(cliente=None):
    cliente_atual = escolher_cliente(cliente)

    print(f"Iniciando compra para: {cliente_atual.nome_completo}")

    produto, quantidade = escolher_produtos_para_compra()
    if produto is None:
        return None

    if not input_confirmacao("Adicionar ao carrinho?"):
        print("Compra cancelada!")
        return None

    carrinho = Carrinho(cliente_atual)

    if carrinho.adicionar_produto(produto, quantidade):
        print(f"{quantidade}x {produto.nome} adicionado(s) ao carrinho!")
        return carrinho
    else:
        print("Erro: Estoque insuficiente!")
        return None


def listar_carrinho(carrinho):
    if carrinho is None:
        print("Carrinho vazio!")
        return

    print('*'*50)
    print(" SEU CARRINHO ".center(50))
    print('*'*50)
    print(f"Cliente: {carrinho.cliente.nome_completo}")
    print('*'*50)

    resumo = carrinho.obter_resumo()
    total_geral = 0

    for produto, qtd in resumo.items():
        subtotal = produto.preco * qtd
        total_geral += subtotal
        print(f"{produto.nome:<23} | ({qtd:}x) | {produto.preco:>6.2f} | {subtotal:>8.2f}")

    print('*'*50)
    print(f"{'TOTAL GERAL':<23} | {'':>2} R${total_geral:.2f}")
    print('*'*50)
    print()


def finalizar_compra(carrinho):
    if carrinho is None:
        print("Carrinho vazio!")
        return False

    print('*'*50)
    print(" FINALIZAÇÃO DA COMPRA ".center(50))
    print('*'*50)

    listar_carrinho(carrinho)

    if not input_confirmacao('Confirma o pagamento?'):
        print("Compra cancelada!")
        return False

    print("Processando pagamento...")
    print("Pagamento aprovado!")
    print(f"Compra finalizada para {carrinho.cliente.nome_completo}!")

    carrinho.limpar()
    return True
