opcao = -1

while opcao != 0:
    opcao = int(input('Escolha a opção do serviço que deseja \n [1]Sacar \n [2]Depositar \n [0]Sair \n Qual: '))

    if opcao == 1:
        print('== Você escolheu a opção de saque ==')
        input('Qual valor deseja sacar: ')
        print('Sacando...')

    elif opcao == 2:
        print('== Você escolheu a opção de deposito ==')
        input('Qual valor deseja depositar: ')
        print('Depositado com sucesso!')
else:
    print('Agradeçemos por usar nosso sistema bancário!')
