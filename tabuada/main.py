import os
from rich.console import Console
from rich.table import Table    

console = Console()

def clear_screen():
    "Clear the console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def exibir_tabuada(tabuada, operacao):
    """Exibe a tabuada com base na operação e no número informado."""
    table = Table(title=f"Tabuada do {tabuada} com '{operacao}'")

    table.add_column("Expressão", style="cyan")
    table.add_column("Resultado", style="magenta")

    for i in range(1, 11):
        if operacao == '+':
            resultado = tabuada + i
            expressao = f"{tabuada} + {i}"
        elif operacao == '-':
            resultado = tabuada - i
            expressao = f"{tabuada} - {i}"
        elif operacao == '*':
            resultado = tabuada * i
            expressao = f"{tabuada} * {i}"
        elif operacao == '/':
            resultado = round(tabuada / i, 2)
            expressao = f"{tabuada} / {i}"

        table.add_row(expressao, str(resultado))

    console.print(table)

def display_menu():
    MENU_TABUADA = '''[bold green][1][/bold green]: -> Tabuada de 1
[bold green][2][/bold green]: -> Tabuada de 2
[bold green][3][/bold green]: -> Tabuada de 3
[bold green][4][/bold green]: -> Tabuada de 4
[bold green][5][/bold green]: -> Tabuada de 5
[bold green][6][/bold green]: -> Tabuada de 6
[bold green][7][/bold green]: -> Tabuada de 7
[bold green][8][/bold green]: -> Tabuada de 8
[bold green][9][/bold green]: -> Tabuada de 9
[bold green][10][/bold green]: -> Tabuada de 10
[bold green][0][/bold green]: -> Sair do Programa'''

    console.print(MENU_TABUADA)

    try:
        tabuada = int(input('Informe a tabuada desejada (0 PARA SAIR): '))
    except ValueError:
        console.print('[red]Entrada inválida! Digite um número.[/red]')
        return True

    if tabuada == 0:
        console.print('[bold red]Saindo do programa...[/bold red]')
        return False
    elif tabuada < 1 or tabuada > 10:
        console.print('[red]Tabuada inválida. Tente novamente.[/red]')
        return True

    operacao = input("Informe a operação desejada ('+', '-', '*', '/'): ")
    if operacao not in ['+', '-', '*', '/']:
        console.print('[red]Operação inválida. Tente novamente.[/red]')
        return True

    clear_screen()
    exibir_tabuada(tabuada, operacao)
    return True

if __name__ == "__main__":
    continuar = True
    while continuar:
        continuar = display_menu()
