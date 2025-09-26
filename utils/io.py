def input_num(prompt: str = None, minimo: int = None, maximo: int = None) -> int:
    while True:
        try:
            entrada_num = int(input(f"{prompt}: "))
            if (minimo is not None and entrada_num < minimo) or (maximo is not None and entrada_num > maximo):
                print(f"Erro: Por favor digite entre numero {minimo} e {maximo}")
                continue
            return entrada_num
        except KeyboardInterrupt:
            exit()


def input_text(prompt: str = None) -> str:
    while True:
        try:
            entrada_text = input(f"{prompt}: ")
            if entrada_text:
                return entrada_text
            else:
                print("vai deixar em branco, serio isso?")
        except ValueError:
            print("Ai não em, número não, é texto por favor!")
        except KeyboardInterrupt:
            exit()


def input_confirmacao(prompt: str = "Confirma a operação?") -> bool:
    while True:
        try:
            resposta = input(f"{prompt} (s/n) ").strip().lower()
            if resposta in ['s', 'sim', 'y', 'yes']:
                return True
            elif resposta in ['n', 'nao', 'não', 'no']:
                return False
            else:
                print("Digite 's' para sim ou 'n' para não")
        except KeyboardInterrupt:
            return False
