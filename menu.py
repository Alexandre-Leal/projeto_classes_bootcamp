import os
from user_prompt import inquire, perguntas
from classe_todolist import todo_list
from rich import print

def menu_ou_sair():
    
    decisao = False
    print()
    while decisao not in ["0","1"]:
        decisao = input("Digite 1 para retonar ao menu ou 0 para encerrar o programa ").lower()

    if decisao == "1":
        menu()
    elif decisao == "0":
        return



def menu():
    decision = inquire()


    filename = "to_do_list.csv"

    if decision == 'Adicionar tarefa':
        parametros = perguntas()
        add = todo_list(parametros)
        add.adicionar_linha_csv()
        menu_ou_sair()
    if decision == 'Alterar status da tarefa':
        todo_list.altera_status_tarefa(filename,input("Qual o nome da tarefa que você deseja alterar o status? "))
        menu_ou_sair()
    if decision == 'Remover tarefa':
        os.system('cls')
        todo_list.remover_tarefa(filename,input("Qual tarefa deseja remover? \n"))
        menu_ou_sair()
    if decision == 'Visualizar tarefas':
        todo_list.visualizar_tarefas(filename)
        menu_ou_sair()

    if decision == 'Encerrar':
        os.system('cls')
        print("[bold red]Programa encerrado[/]")
        return
menu()


