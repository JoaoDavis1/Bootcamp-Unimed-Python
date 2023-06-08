saldo = input('Qual seu saldo: ')
valor = input('Qual valor do saque: ')
valor_depositado = input('Qual valor depositado: ')

def sacar(valor):

    if saldo >= valor:
        print('Valor sacado com sucesso!')

    print('Obrigado por utilizar nossos serviços!')


sacar(valor)

def depositado(valor_depositado):

    print(f'O valor depositado foi de R${valor_depositado}')

depositado(valor_depositado)