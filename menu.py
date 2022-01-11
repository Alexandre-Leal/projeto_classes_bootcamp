import datetime
import os
import csv
from user_prompt import inquire, perguntas
from classe_todolist import todo_list
from rich import print


def menu():
    decision = inquire()


    filename = "teste.csv"

    if decision == 'Adicionar tarefa':
        parametros = perguntas()
        add = todo_list(parametros)
        add.adicionar_linha_csv()
    if decision == 'Alterar status da tarefa':
        pass
    if decision == 'Remover tarefa':
        os.system('cls')
        todo_list.remover_tarefa(filename,input("Qual tarefa deseja remover? \n"))
    if decision == 'Visualizar tarefas':
        todo_list.visualizar_tarefas(filename)
    if decision == 'Encerrar':
        os.system('cls')
        print("[bold red]Programa encerrado[/]")
        return
menu()

