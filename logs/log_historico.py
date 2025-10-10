from datetime import datetime
from pathlib import Path

DIR_PASTA = Path(__file__).parent
CAMINHO_PASTA = DIR_PASTA/'historico.txt'


def salvar_historico(cliente, produto):
    with open(CAMINHO_PASTA, 'a+', encoding='utf-8') as file:
        data_registro = datetime.now().strftime('%d/%m/%Y %H:%M')
        file.write(f"{data_registro} | {cliente} | {produto}\n")
