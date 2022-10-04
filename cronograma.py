cronograma= []
tarefas= {}

def line():
    print('='*60)

def all():
    line()
    print(cronograma,'\n')
    line()
  
line()
print(f"{'MEU CRONOGRAMA DIÁRIO' : ^60}")

option= 0
while option != 5:
    line()
    print('''ESCOLHA UMA OPÇÃO:
    
    [1] VER TODAS AS TAREFAS
    [2] ADICIONAR NOVA TAREFA
    [3] EDITAR TAREFA
    [4] REMOVER TAREFA
    [5] SAIR DO PROGRAMA''')
    line()
    try:
        option= int(input('Selecionar opção desejada: '))
    except:               
        print('ERRO! Por favor digite apenas um dos números listados.')

    #todas tarefas
    if option == 1:
        if not cronograma:
            print('NÃO HÁ TAREFAS! Vamos lá, adicione uma..')
        else:    
            all()
            print(f'\nTemos o total de {len(cronograma)} tarefas para realizar.')

    #adicionar tarefa    
    if option == 2:
        tarefas.clear()
        try:
            line()
            print(f"{'ADICIONAR TAREFA' : ^50}")
            line()
            tarefas['Tarefa'] = str(input('Nome da Tarefa: ')).upper()
        except:    
            print('ERRO! Digite apenas LETRAS.')
        tarefas['Horário']= str(input('Horário [00.00]: '))  
        tarefas['Nível de Prioridade']= float(input('Nível de Prioridade (0 - 10): '))    #NÍVEIS DE PRIORIDADE - AZUL: 1 a 4 BAIXO - AMARELO: 5 - 8 MEDIO - VERMELHO: 9 - 10 ALTO
        cronograma.append(tarefas.copy()) 
        while True:
            r= str(input('Quer continuar ultilizando o programa? [S/N] ')).upper()[0]
            if r in 'SN':
                break
            print('Error! Responda apenas S ou N.')
        if r == 'N':
            all()
            break

    #editar tarefa        
    if option == 3:
        line()
        print(f"{'EDITAR TAREFA' : ^50}")
        line()
        procurar_tarefa= str(input('Digite o nome da tarefa para editar: ')).upper()
        for procurar_tarefa in cronograma:
            line()
            editar= int(input(f'A tarefa "{procurar_tarefa}" foi encontrada. \n Oque voê deseja editar:  \n [1] Nome da tarefa \n [2] Horário \n [3] Nível de Prioridade \n Seleciona a opção desejada: '))
            line()
            if editar == 1:
                name= str(input('Atualizar nome da Tarefa: ')).upper()   
                tarefas['Tarefas']= tarefas.append(name) 
                print(f'O nome  foi atualizado com sucesso.')
                break
            if editar == 2:
                tarefas['Horário']= str(input('Atualizar Horário [00.00]: '))  
                cronograma.append(tarefas)              
                print(f'O horário foi atualizado com sucesso.')
                break
            if editar == 3:
                tarefas['Nível de Prioridade']= str(input('Atualizar nível de prioridade: '))
                print(f'O nível de prioridade foi atualizado com sucesso.')
   
            else:
                print('\n ERRO! Por favor digite apenas um dos números listados.')

    #apagar tarefa
    if option == 4:
        line()
        print(f"{'REMOVER TAREFA' : ^50}")
        all()
        line()
        remover_tarefa= str(input('Digite o nome da tarefa para remover: ')).upper()
        if remover_tarefa not in cronograma:          
            print(f'A tarefa {remover_tarefa} não foi encontrada. Tente novamente!')
        else:
            rmv= str(input(f'Tem certeza quer deseja remover {remover_tarefa} ?[S/N] ')).upper()[0]
            if rmv in 'SN':
                print('ERRO! Responda apenas S ou N.')        
            if rmv == 'S':   
                cronograma.clear()
                print('Tarefa removida com sucesso.')       

    #sair do programa
    if option == 5:
        print('Obrigado por ultilizar nossos serviços. Volte sempre!')
        line()
        break
   
