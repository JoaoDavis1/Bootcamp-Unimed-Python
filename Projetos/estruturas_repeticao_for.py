texto = input('Informe um texto: ')
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra.upper(), end=" ")
else:
    print('\nFim laço')