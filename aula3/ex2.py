from fila import Queue

f = Queue()

while True:
    print("\n--- Sistema de Call Center ---")
    print("1. Inserir contato")
    print("2. Próximo contato")
    print("3. Sair")
    
    option = input("Escolha uma opção: ")
    contatos = []
    if option == "1":
        nome = input("Nome do cliente: ")
        telefone = input("Telefone: ")
        contato = f"{nome} ({telefone})"
        f.enqueue(contato)
        print("Contato adicionado com sucesso!")
        
        contatos.append(contato)
    elif option == "2":
        if f.isEmpty(): 
            print("Fila vazia!")
        else:
            prox = f.dequeue()
            print(f"\n>>> ATENDER AGORA: {contato} <<<")
            
    elif option == "3":
        print("Encerrando sistema...")
        break
        
    else:
        print("Opção inválida, tente novamente.")