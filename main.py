import os
from models.cliente import listar_clientes
from utils.io import input_num
from services.compras import exibir_produtos, cadastrar_cliente, fazer_compra, listar_carrinho, finalizar_compra
from services.compras import LISTA_PRODUTOS


class SistemaCompras:
    def __init__(self):
        self.cliente_ativo = None
        self.carrinho_ativo = None

    def limpar_tela(self):
        os.system("cls" if os.name == "nt" else "clear")

    def executar(self):
        while True:
            self.limpar_tela()
            opcao = self.exibir_menu()

            if opcao == 7:
                print("Você saiu sistema!")
                break

            self.processar_opcao(opcao)
            input("\nPressione ENTER para continuar...")

    def exibir_menu(self) -> int:
        opcoes = [
            'Listar produtos',
            'Cadastrar cliente',
            'Listar clientes',
            'Fazer compra',
            'Ver carrinho',
            'Finalizar compra',
            'Sair'
        ]

        print('*'*20)
        print('SISTEMA DE COMPRAS'.center(20))
        print('*'*20)

        for i, opcao in enumerate(opcoes, 1):
            print(f"[{i}] {opcao}")
        return input_num('Escolha uma opção', minimo=1, maximo=7)

    def processar_opcao(self, opcao: int):
        try:
            match opcao:
                case 1: exibir_produtos(LISTA_PRODUTOS)
                case 2: self.cliente_ativo = cadastrar_cliente()
                case 3: listar_clientes(self.cliente_ativo)
                case 4:
                    if self.validar_cliente():
                        self.carrinho_ativo = fazer_compra(self.cliente_ativo)

                case 5: listar_carrinho(self.carrinho_ativo)
                case 6: finalizar_compra(self.carrinho_ativo)

        except Exception as e:
            print(f"Erro inesperado: {e}")

    def validar_cliente(self):
        if self.cliente_ativo is None:
            print("Nenhum cliente ativo! Cadastre um cliente primeiro!")
            return False
        return True


if __name__ == "__main__":
    sistema = SistemaCompras()
    sistema.executar()
