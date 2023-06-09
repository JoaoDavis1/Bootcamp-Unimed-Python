saldo = 1000
saque = 350
limite = 200

#Operador E (Todos precisam ser True para resultado ser True)
print(saldo >= saque and saque <= limite)
print(saldo >= saque and saque >= limite)

#Operador OU (Apenas um precisa ser True para resultado ser True)
print(saldo >= saque or saque <= limite)
print(saldo <= saque or saque <= limite)

#Operador de Negação
print(not 100 > 200)

#Parênteses
print((saldo >= saque and saque <= limite) or (saldo >= saque and saque >= limite))

