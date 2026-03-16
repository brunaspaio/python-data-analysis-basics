from datetime import date
maior = 0
menor = 0

for i in range(7):
    anoNasc = int(input("Digite seu ano de nascimento: "))
    atual = date.today().year
    idade = atual - anoNasc
    if idade >= 18:
        maior = maior +1
    else:
        menor = menor +1
print(f"Maior de idade {maior}")
print(f"Menor de idade {menor}")
