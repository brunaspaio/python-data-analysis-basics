tarefas = []
while True:
    print("\n1 - Adicionar tarefa")
    print("2 - Listar tarefas")
    print("3 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        tarefa = input("Digite a tarefa: ")
        tarefas.append(tarefa)

    elif opcao == "2":
      if len(tarefas) == 0:
        print("Nenhuma tarefa cadastrada.")
      
    else:
        for t in tarefas:
            print("-", t)
