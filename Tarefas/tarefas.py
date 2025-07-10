import os

def menuinicial():
    print('Tarefas')
    with open('tarefas.txt', 'r') as tarefassalvas:
        ler = tarefassalvas.readlines()
        for numero, tarefa in enumerate(ler, start=1):
            print(f'{numero}. {tarefa.strip()}')
menuinicial()
def limpar():
     os.system('cls' if os.name == 'nt' else 'clear')
def adicionartarefa():
    tarefa = input('Adicione uma tarefa: ')
    print ('sua tarefa: ' + tarefa)
    with open('tarefas.txt', 'a') as salvartarefa:
        salvartarefa.write(tarefa + '\n')
        limpar()
def acoesnatarefa():
    acao = int(input('Oque deseja fazer na tarefa? \n 1 | marcar como feita \n 2 | excluir tarefa \n 3 | adicionar tarefa \n '))
    if acao == 1:
            enumeracao = int(input('Qual tarefa deseja marcar como feita? \n'))
            indicedatarefa = enumeracao - 1
            with open('tarefas.txt', 'r') as arquivo:
                tarefas = arquivo.readlines()
            tarefas[indicedatarefa] = '[FEITO] ' + tarefas[indicedatarefa]
            with open ('tarefas.txt', 'w', encoding='utf-8') as tarefaantiga:
                    tarefaantiga.writelines(tarefas)
                    limpar()
    elif acao == 2:
         selecionador = int(input('Qual tarefa deseja excluir? \n'))
         escolha = selecionador - 1
         with open('tarefas.txt', 'r') as arq:
             tarefas = arq.readlines()
         tarefas[escolha] = ''
         with open ('tarefas.txt', 'w') as excluir:
              excluir.writelines(tarefas)
              limpar()
    elif acao == 3:
         adicionartarefa()
acoesnatarefa()
while True:
     menuinicial()
     acoesnatarefa()