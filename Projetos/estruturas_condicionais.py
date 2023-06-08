saldo = 2500.0
saque = float(input('Informe o valor do saque: '))

if saldo >= saque:
    print('Saque Autorizado!')
else:
    print('Saldo Insuficiente!')

opcao = int(input('Escolha a opção do serviço que deseja \n [1]Sacar \n [2]Depositar \n Qual: '))

if opcao == 1:
    print('== Você escolheu a opção de saque ==')
    input('Qual valor deseja sacar: ')

elif opcao == 2:
    print('== Você escolheu a opção de deposito ==')
    input('Qual valor deseja depositar: ')

else:
    print('Opção Inválida!')