arquivo = open('arq.txt', 'w')
arquivo.write('Alain .....')
arquivo.close()

with open('arq.txt', 'w') as arquivo:
    arquivo.write('Tudo tranqulao')

with open('arq.txt', 'r') as arquivo:
    print(arquivo.read())