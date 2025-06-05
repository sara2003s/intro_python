'''
Escreva um programa que processe a média de um determinado quantidade
de notas escolares fornecidas pelo usuário, o script deve receber o 
nome do aluno e em seguiuda, as notas que serão armazenadas em uma lista. 
A média deve ser calculada e exibida ao final com os status do aluno, de 
acordo com as regras abaixo:
- Aprovado(a): média maior ou igual a 7
- Recuperação: média maior ou igual a 5 e menor que 7
- Reprovado(a): média inferior a 5
Aluno: Nome do aluno
Notas: 10.0 9.5 8.4 10.0
Média: 8.7
Status: Aprovado(a)
'''
import os

# Declaração de variáveis
notas = []
status = ''
nome_aluno = ''
saida = ''

os.system('cls') 

# Entradas
nome_aluno = input('Aluno: ')
qtd_notas = int(input('Quantidade de notas: '))

for i in range(qtd_notas):
    notas.append(float(input(f'{i + 1} nota:')))

os.system('cls')

#Processamento
media = sum(notas) / len(notas)

if media >= 7:
    status = 'Aprovado(a)'
elif media < 5:
    status = 'Reprovado(a)'
else:
    status = 'Em recuperação'


# Saída
saida += f'Aluno: {nome_aluno}\n'
saida += 'Notas: 0'

for nota in notas:
    saida += f'{str(nota)}'

saida += f'\nMédia: {media}:.2f\n'
saida += f'Situação: {status}\n'
saida += '-' * 40

print(saida)