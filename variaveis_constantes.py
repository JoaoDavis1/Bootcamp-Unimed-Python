#Variaveis mudam de valor
idade = 18
nome = 'João David'
print(f'Olá meu nome é {nome} e tenho {idade} anos.')

idade = 17
nome = 'Ana'
print(f'Olá meu nome é {nome} e tenho {idade} anos.')

#É permitido declarar variaveis ou constantes na mesma linha:
idade, nome = 24, 'Marco Polo'
print(idade, nome)

limite_saque_diario = 580

#Constantes não mudam de valor
# (Em python não existe palavra reservada para Constantes, declarar constante toda maiúscula como convensão)

ESTADOS_SUDESTE = ['MG', 'RJ', 'SP', 'ES']
print(ESTADOS_SUDESTE)

VALOR = 15.9