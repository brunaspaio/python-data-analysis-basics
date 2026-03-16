media = 0
contador = 0
soma_notas = 0
aluno = input("Digite o nome do aluno:\n ")

while True:
    inserir = (input("Deseja inserir uma nota? (s/n):\n "))
    if inserir == "n":
        print("saindo..")
        break
    nota = float(input("Informe a nota:\n "))
    soma_notas += nota
    contador +=1
media = (soma_notas)/contador
print(f"{aluno} sua media é {media:,.2} e voce esta ",end=" ")
if media <= 5 :
    print("Reprovado")
elif media <8:
    print("Recuperação")
elif media >= 8:
    print("Aprovado")
