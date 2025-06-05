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

os.system('cls')

alunos = []

while True:
    nome = input('Aluno(a):')
    notas = []

    i = 0
    while i < 4:
        nota = float(f'{i + 1} ª nota:')
        if nota < 0 or nota > 10:
            print ('Nota inválida! Informe uma nota entre 0 10')
            continue
        notas.append(nota)
        i += 1 

    aluno = {
        'nome': nome,
        'notas': notas
    }
    alunos. append(alunos)

    os.system('cls')
    print('Aluno(a) cadastrado com sucesso')
    print('Cadastrar novo(a) aluno(a)? ')
    continuar = input('Digite "S" para sim ou "N" para não:')

    if continuar |+ "S":
        break
    
