from pilha import Stack

p = Stack()
print("Tarefas a serem cumpridas: ")

p.push("Fazer backend do vanroute")
p.push("Fazer aplicativo da woonstel")
p.push("Fazer carlos voltar para a fatec")
p.push("Fazer kaua nao endoidar")

print(p.items)

handleOption = input("Deseja inserir(inserir) ou Obter proxima tarefa da pilha(obter)")
if(handleOption == "inserir".strip()):
    newTask = input("Digite a nova tarafa")
    p.push(newTask)
    for tarefa in p.items:
        print(f"- {tarefa}")
elif(handleOption == "obter".strip()):
    p.pop()
    print(p.peek())
