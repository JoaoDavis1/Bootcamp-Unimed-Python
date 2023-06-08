tipo_conta = input('Escolha o seu tipo de conta: \n Conta Normal \n Conta Universitaria \n Qual: ')

saldo = 2000.0
saque = float(input('Informe o valor a ser sacado: '))
cheque_especial = float(input('Informe o valor do Cheque Especial: '))

if tipo_conta == 'Conta Normal':
    if saldo >= saque:
        print('Saque Autorizado!')
    elif saldo <= (saldo + cheque_especial):
        print('Saque realizado com uso do cheque especial')
    else:
        print('Saldo Insuficiente')
elif tipo_conta == 'Conta Universitaria':
    if saldo >= saque:
        print('Saque Autorizado!')
    else:
        print('Saldo Insuficiente')
else: 
    print('Conta Inexistente!')