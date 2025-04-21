def adicionar_tarefa(lista_de_tarefas, tarefa):
    """Adiciona nova tarefa a uma lista pré-existente"""
    lista_de_tarefas.append(tarefa)
    print(' - - Tarefa adicionada com sucesso!')
    return lista_de_tarefas

def listar_tarefas(lista_de_tarefas):
    """Exibe lista de tarefas numerada"""
    print('\n')
    print(' - - Lista de Tarefas')
    print('-' * 50)
    n = 1
    for tarefa in lista_de_tarefas:
        print(f'{n} - {tarefa}')
        n += 1
    if len(lista_de_tarefas) < 1:
        print('Não há tarefas')
    print('-' * 50)

def deletar_tarefa(lista_de_tarefas, tarefa):
    """Deleta tarefa de uma lista pré-existente a partir do número dela"""
    lista_de_tarefas.pop((tarefa - 1))
    print(' - - Tarefa deletada')
    return lista_de_tarefas

def exibir_menu():
    """Exibe menu com opções para usuárie escolher"""
    print(' - - Escolha uma opção:\n' \
    '1 - Inserir nova tarefa\n' \
    '2 - Listar tarefas\n' \
    '3 - Deletar tarefa\n'
    '4 - Sair'
    )

# Inicialização de variáveis
lista_de_tarefas = []
continuar = True

# Cabeçalho do programa
print('\nBem-vinde à sua Lista de Tarefas!\n')

# Loop principal
while continuar:
    exibir_menu()
    opcao = input('Insira o que deseja fazer: ')

    if opcao == "1":
        tarefa = input('Insira uma nova tarefa: ')
        lista_de_tarefas = adicionar_tarefa(lista_de_tarefas, tarefa)
    elif opcao == "2":
        listar_tarefas(lista_de_tarefas)
    elif opcao == "3":
        # A validação verifica se o valor é numérico, se é menor do que o limite da lista e se é maior do que zero
        tarefa = input('Insira o número da tarefa que deseja deletar: ')
        if not tarefa.isnumeric() or int(tarefa) > len(lista_de_tarefas) or int(tarefa) < 1:
            print('!! Número inválido! Tente novamente.')
        else:
            deletar_tarefa(lista_de_tarefas, int(tarefa))
    elif opcao == "4":
        continuar = False
    else:
        print('!! Opção inválida! Tente novamente')
    print('\n')