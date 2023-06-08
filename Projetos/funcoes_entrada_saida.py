nome = input('Qual é o seu nome: ')
sobrenome = input('Qual é o seu sobrenome: ')

print(f'Olá {nome} {sobrenome}, seja bem vindo!')
#end(Adiciona no final) | \n(Quebra de linha)
print(nome, sobrenome, end="... \n")
#sep(Separador entre variaveis)
print(nome, sobrenome, sep="-")
print(nome, sobrenome, sep="_", end="..")