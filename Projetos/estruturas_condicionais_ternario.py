MAIOR_IDADE = 18

nome = input('Qual o seu nome: ')
idade = int(input('Qual sua idade: '))

status = 'já pode' if idade >= MAIOR_IDADE else 'ainda não pode'

print(f'Olá {nome}, você {status} tirar sua carteira de motorista!')