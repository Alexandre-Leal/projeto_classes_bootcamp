import inquirer
import datetime
import os
import csv




def inquire():
    questions = [
    inquirer.List('option',
        message='Escolha uma das opções abaixo',
        choices=[
        'Adicionar tarefa',
        'Alterar status da tarefa',
        'Remover tarefa',
        'Visualizar tarefas',
        'Encerrar'
        ])]

    resp = list(inquirer.prompt(questions).values())
    return resp[0]


def perguntas():
    perguntas_tarefa = [
    inquirer.Text('name', message='Qual é o nome da tarefa?'),
    inquirer.Text('categoria', message='Qual a categoria da tarefa?'),
    inquirer.Text('data', message='Para quando é essa tarefa?')
    ]
    
    parametros = list(inquirer.prompt(perguntas_tarefa).values())
    return parametros
### MODULE BREAK ####


class todo_list:

    filename = "teste.csv"
    
    def __init__(self,parametros):
        self.name = parametros[0]
        self.categoria = parametros[1]
        self.data = parametros[2]
        
        self.parametros = parametros

    def adicionar_linha_csv(self):
        with open(self.filename, 'a',newline='') as arquivo:
            escritor = csv.writer(arquivo, delimiter=',', lineterminator='\n')

            escritor.writerow(self.parametros)
    
    @staticmethod       
    
    def remover_tarefa(filename,name):
        
        with open(filename, 'r') as inp, open('edit.csv', 'w') as out:
            writer = csv.writer(out,delimiter=',', lineterminator='\n')
            for row in csv.reader(inp):
                if row[0] != name:
                    writer.writerow(row)
   
        os.remove("teste.csv")
        os.rename('edit.csv', 'teste.csv')
        print(f"A tarefa '{name}' foi removida")

    @staticmethod 
    def visualizar_tarefas(filename):
        with open(filename, 'r') as inp:
            for row in csv.reader(inp):
                print(f"Tarefa: {row[0]}. Categoria: {row[1]}. Data: {row[2]}")

### MODULE BREAK ###

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
        todo_list.remover_tarefa(filename,input("Qual tarefa deseja remover?"))
    if decision == 'Visualizar tarefas':
        todo_list.visualizar_tarefas(filename)
    if decision == 'Encerrar':
        print("Programa encerrado")
        return
menu()

