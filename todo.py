tasks = []

def menu():
    print("\n📝 LISTA DE TAREFAS")
    print("1 - Adicionar tarefa")
    print("2 - Listar tarefas")
    print("3 - Remover tarefa")
    print("0 - Sair")


def adicionar_tarefa():
    tarefa = input("Digite a tarefa: ")
    tasks.append(tarefa)
    print("✅ Tarefa adicionada!")

def listar_tarefas():
    if not tasks:
        print("Nenhuma tarefa cadastrada.")
    else:
        print("\n📋 Suas tarefas:")
        for i, tarefa in enumerate(tasks):
            print(f"{i} - {tarefa}")

def remover_tarefa():
    listar_tarefas()
    try:
        indice = int(input("Digite o número da tarefa para remover: "))
        tarefa_removida = tasks.pop(indice)
        print(f"❌ Tarefa removida: {tarefa_removida}")
    except:
        print("❌ Er
