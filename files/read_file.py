nome_arquivo = input('Nome do arquivo: ')

f = open(f'./{nome_arquivo}.txt', encoding='utf8')

print(f.read(10))

f.close()