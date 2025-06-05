import os
from rich import print

os.system('cls')

peso = float(input('Informe o seu peso:'))
altura = float(input('Informe a sua altura'))

imc = peso / (altura ** 2)

tabela_imc = '''Acima de 40.0: Obesidade grau III
Entre 35.0 e 39.9: Obesidade grau II
Entre 25.0 e 29.9: Obesidade grau I
Entre 25.0 e 29.0: Sobrepeso
Entre 18.6 e 24.9: Normal
'''

if imc > 40.0:
    resultado = '[bold red]Obesidade grau III[/bold red]'
elif imc >= 35.0 and imc <= 39.9:
    resultado = '[bold red]Obesidade grau II [/bold red]'
elif imc >=30 and imc <= 34.9:
    resultado = '[bold red]Obesidade grau I [/bold red]'
elif imc >= 25.0 and imc <= 24.9:
    resultado = '[bold red]Sobrepeso [/bold red]'
elif imc >= 18.6 and imc <= 24.9:
    resultado = '[bold red]Normal [/bold red]'
else:
    resultado = '[bold red]Abaixo do normal[/bold red]'

print(tabela_imc)
print(f'Seu indice de massa corporal está em {imc:.2f} e seu status é {resultado}')