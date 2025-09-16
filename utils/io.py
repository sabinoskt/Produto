def input_num(prompt: str = None) -> int:
    entrada_num = int(input(f"{prompt}: "))
    return entrada_num

def input_text(prompt: str = None) -> str:
    while True:
        try:
            entrada_text = input(f"{prompt}: ")
            if entrada_text:
                return entrada_text
            else:
                print("vai deixar em branco serio?")
        except ValueError:
            print("Ai não em, número não, é texto por favor!")
