import inquirer
from datetime import datetime, timedelta
from check import check_data_correta


def inquire():
    print("Bem vindo à todo-list!")
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
    inquirer.Text('data', message="Para quando é essa tarefa?. Formato mm/dd/yyyy, ou 'Hoje' ou 'Amanha'")
    ]
    
    parametros = list(inquirer.prompt(perguntas_tarefa).values())
    parametros.append("Pendente")
    data_errada = parametros[2]
    data_corrigida = check_data_correta(data_errada)
    parametros[2] = data_corrigida
        
    return parametros





