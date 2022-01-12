import csv
import os
from pandas.core.frame import DataFrame
from rich.tree import Tree
from rich import print
import pandas as pd
import numpy as np
from datetime import datetime


class todo_list:

    filename = "to_do_list.csv"
    
    def __init__(self,parametros):
        self.name = parametros[0]
        self.categoria = parametros[1]
        self.data = parametros[2]
        self.parametros = parametros

    def adicionar_linha_csv(self):

        try:
            open(self.filename)
        except FileNotFoundError as error:
            print('Arquivo não encontrado.', error)
        except KeyError:
            print('Chave não encontrada.')
        except Exception as error:
            print('Erro genérico:', error)

        with open(self.filename, 'r') as inp:
            for row in csv.reader(inp):
                if row[0] == self.name:
                    os.system('cls')
                    print("[bold red]Essa tarefa já existe. Escolha outro nome.[/]")
                    return
                  
    
        with open(self.filename, 'a',newline='') as arquivo:
            escritor = csv.writer(arquivo, delimiter=',', lineterminator='\n')
            escritor.writerow(self.parametros)


        os.system('cls')
        print(f"[bold green] A tarefa '{self.name}' foi adicionada com sucesso.[/]")

    @staticmethod       
    def remover_tarefa(filename,name):
        
        with open(filename, 'r') as inp, open('edit.csv', 'w') as out:
            writer = csv.writer(out,delimiter=',', lineterminator='\n')
            for row in csv.reader(inp):
                if row[0] != name:
                    writer.writerow(row)
   
        os.remove("to_do_list.csv")
        os.rename('edit.csv', 'to_do_list.csv')
        os.system('cls') 
        print(f"A tarefa '{name}' foi removida")

    @staticmethod 
    def visualizar_tarefas(filename):
        
        pendentes = Tree("[bold red]Tarefas pendentes[/] ")
        concluidas = Tree("[bold green] Tarefas concluídas[/]")
        with open(filename, 'r') as inp:
            for row in csv.reader(inp):
                if row[3] == "Pendente":
                    pendentes.add(f"[italic]tarefa: [/][bold blue]{row[0]}[/] [italic]categoria:[/] [bold]{row[1]} [/] [italic]Data: [/] [bold]{row[2]}")
                if row[3] == "Concluido":
                               concluidas.add(f"[italic]tarefa: [/][bold blue]{row[0]}[/] [italic]categoria:[/] [bold]{row[1]} [/] [italic]Data: [/] [bold]{row[2]}")
        os.system('cls')            
        print(pendentes)
        print()
        print(concluidas)

    @staticmethod
    def altera_status_tarefa(filename, tarefa):

          
        df = pd.read_csv(filename)
        
        linha_titulo = df[df['tarefa'] == tarefa]
       
 
        status = list(linha_titulo['status'])

        if len(linha_titulo) == 0:
            print(f'A tarefa: {tarefa} não exista.')
            return
        else:
                               
            if status[0] == 'Pendente':
                novo_status = 'Concluido'
                df.loc[df['tarefa'] == tarefa , 'status'] = novo_status
            
            elif status[0] == 'Concluido':
                novo_status = 'Pendente'
                df.loc[df['tarefa'] == tarefa , 'status'] = novo_status
                
            else:
                raise ValueError("Há algum problema no status dessa tarefa")
            

            df.to_csv('to_do_list.csv',index= False)
            os.system('cls')
            print(f"A tarefa '{tarefa}' teve seu status alterado para [bold]{novo_status}[/]")
        

    
