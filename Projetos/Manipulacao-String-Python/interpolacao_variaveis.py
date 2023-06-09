nome = "João"
idade = 18
profissao = "Programador"
linguagem = "Python"

#metodo old (%)
print('Olá, meu nome é %s. Eu tenho %d anos, trabalho como %s e estou matriculado no curso de %s' 
% (nome, idade, profissao, linguagem))

#metodo format
print('Olá, meu nome é {}. Eu tenho {} anos, trabalho como {} e estou matriculado no curso de {}' 
.format (nome, idade, profissao, linguagem))
#metodo format com indice
print('Olá, meu nome é {2}. Eu tenho {3} anos, trabalho como {0} e estou matriculado no curso de {1}' 
.format (profissao, linguagem, nome, idade))

#f-string
print(f'Olá, meu nome é {nome}. Eu tenhon {idade} anos, trabalho como {profissao} e estou matriculado no curso de {linguagem}.')

#formatar strings com f-string
PI = 3.14159

print(f'O valor de Pi é: {PI:.2f}')