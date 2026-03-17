lista = []
impar = []
par = []

while True:
    num = input("Digite um numero | Digite 0 para sair: ")

    if num.isnumeric():
        num = int(num)

        if num == 0:
            print("Saindo...")
            break

        lista.append(num)

        if num % 2 == 0:
            par.append(num)
        else:
            impar.append(num)

    else:
        print("Digite apenas numeros!")

print(f"Lista completa: {lista}")
print(f"Números pares: {par}")
print(f"Números ímpares: {impar}")
