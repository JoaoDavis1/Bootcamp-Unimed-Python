while True:
    numero = int(input('Digite um número: '))

    if numero == 8:
        break

    print(numero)

for numero in range(101):

    if numero % 2 == 1:
        continue

    print(numero, end=" ")