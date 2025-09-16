from utils.io import input_num
from services.compras import exibir_produtos, cadastrar_cliente, exbir_cliente

cliente_atual = None

def menu():
    lista_tabela = [
        'listar produtos',
        'cadastrar cliente',
        'listar cliente',
    ]

    for i, lista in enumerate(lista_tabela, start= 1):
        print(f"[{i}] {lista}")
    print()

    escolha = input_num('Opção')
    print()
    opcao_escolhida(escolha)


def opcao_escolhida(opcao):
    global cliente_atual
    match opcao:
        case 1: exibir_produtos()
        case 2: cliente_atual = cadastrar_cliente()
        case 3: exbir_cliente(cliente_atual)
        case _:...

if __name__ == "__main__":
    while True:
        menu()
