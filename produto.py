from pathlib import Path
from utils.io import input_num, input_text

# Produto('Mochila', 149.90, 3),
# Produto('Fone de Ouvido', 89.90, 5),
# Produto('Camiseta', 39.90, 10),
# Produto('Garrafa Térmica', 59.90, 8),
# Produto('Caneta Azul', 2.50, 100)

PASTA_PACK = Path(__file__).parent
CAMINHO_PRODUTOS = PASTA_PACK / "produtos.txt"

LISTA_PRODUTOS = []

if __name__ == "__main__":
    text_label = ["Produto", "Valor", "Quantidade"]

    print('*'*50)
    print(' ADICIONAR PRODUTO '.center(50))
    print('*'*50)

    # while True:
    qtd = input_num("Qual quantidade deseja adicionar")
    for _ in range(qtd):
        item = input_text(f"{text_label[0]}"), input_text(f"{text_label[1]}"), input_text(f"{text_label[2]}")
        with open(CAMINHO_PRODUTOS, 'a+', encoding='utf-8') as file:
            with open(CAMINHO_PRODUTOS, 'a+', encoding='utf-8') as file:
                file.seek(0, 2)
                if file.tell() > 0:
                    file.seek(file.tell() - 1)
                    last_char = file.read(1)
                    if last_char != '\n':
                        file.write('\n')
                file.write(f"{item[0]}, {item[1]}, {item[2]}")
        print('-'*50)

        # continuar = input_text("\nPressione ENTER para continuar ou digite SAIR para encerrar o sistema")
        # if continuar.upper() == 'SAIR':
        #     break


def obter_produtos():
    try:
        with open(CAMINHO_PRODUTOS, 'r', encoding='utf-8') as read:
            return read.read()
    except FileNotFoundError:
        return ''