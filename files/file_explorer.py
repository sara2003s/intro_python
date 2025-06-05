import os
from rich.console import Console

console = Console()

os.system('cls' if os.name == 'nt' else 'clear')

MENU = '''[bold green][1][bold green]: -> Criar arquivos
[bold green][2][bold green]: -> Ler arquivos
[bold green][3][bold green]: -> Editar arquivos
[bold green][4][bold green]: -> Deletar arquivos
[bold green][5][bold green]: -> Limpar tela
[bold green][6][bold green]: -> Lista diretoria
[bold green][7][bold green]: -> Mudar direção
[bold green][8][bold green]: -> Localizão atual
[bold green][0][bold green]: -> Encerrar Script'''

options_menu = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0')
OP = ''

while OP != '0':
    try:
        console.print(MENU)
        OP = console.input('Informe a opção desejada: ')

        if OP in options_menu:
            if OP == '1':
                os.system('cls' if os.name == 'nt' else 'clear')
                console.print(f'{'#' * 10} CRIANDO ARQUIVOS {'#' * 10}')
                fname = console.input('Informe o nome do arquivo: ')
                fname = f'{fname}.txt'

                with open(fname, 'x', encoding='utf8') as f:
                    console.print(f'Arquivo {fname.upper()} criado com sucesso')

            elif OP == '2':
                os.system('cls' if os.name == 'nt' else 'clear')
                console.print(f'{'#' * 10} LENDO ARQUIVOS {'#' * 10}')
                fname = console.input('Informe o nome do arquivo: ')
                fname = f'{fname}.txt'
                
                with open(fname, 'r', encoding='utf8') as f:
                    console.print(f.read())
            elif (OP == '3'):
                os.system('cls' if os.name == 'nt' else 'clear')
                console.print(f'{'#' * 10} EDITANDO ARQUIVOS {'#' * 10}')
                fname = console.input('Informe o nome do arquivo: ')
                fname = f'{fname}.txt'

                text = console.input('Digite o texto:\n')

                with open(fname, 'a', encoding='utf8') as f:
                    f.write(text + '\n')
            elif (OP == '4'):
                os.system('cls' if os.name == 'nt' else 'clear')
                console.print(f'{'#' * 10} EXCLUINDo ARQUIVOS {'#' * 10}')
                fname = console.input('Informe o nome do arquivo: ')
                fname = f'{fname}.txt'

                if os.path.exists(fname):
                    os.remove(fname)
                    console.print('Arquivo excluido com sucesso')
                else:
                    console.log('Arquivo não encontrado')
            elif (OP == '5'):
                os.system('cls' if os.name == 'nt' else 'clear')
            elif (OP == '6'):
                os.system('cls' if os.name == 'nt' else 'clear')
                list_dir = os.listdir()

                for i in list_dir:
                    console.print()
            elif (OP == '7'):
                os.system('cls' if os.name == 'nt' else 'clear')
                console.print(f'{'#' * 10} NAVEGANDO ENTRE AS PASTAS {'#' * 10}')
                destination = os.chdir(console.input('Mudar para a pasta: '))
                console.print('PASTA ATUAL:', os.getpid())
            elif (OP == '8'):
                os.system('cls' if os.name == 'nt' else 'clear')
                current = os.getcwd()
                console.print('[blue]DIRETÓRIO CORRENTE[/blue] [underline]{current}[/underline]')
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            console.print('f[bold red]Opção inválida, tente novamente[/bold red]')
    except FileExistsError:
        console.print('[bold yellow]o arquivo já existe [/bold yellow]')
    except FileExistsError:
        console.print('[bold yellow] arquivo não encontrado [/bold yellow]')

os.system('cls' if os.name == 'nt' else 'clear')

             

