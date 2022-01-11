import csv
import os
from rich.tree import Tree
from rich import print

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
        os.system('cls') 
        print(f"A tarefa '{name}' foi removida")

    @staticmethod 
    def visualizar_tarefas(filename):
        pendentes = Tree("[bold red]Tarefas pendentes[/] ")
        concluidas = Tree("[bold green] Tarefas concluídas[/]")
        with open(filename, 'r') as inp:
            for row in csv.reader(inp):
                if row[3] == "Pendente":
                    pendentes.add(f"[bold blue]{row[0]}, [/] [italic]categoria:[/] [bold]{row[1]}, [/] [italic]Data: [/] [bold]{row[2]}")
                elif row[3] == "Concluido":
                    concluidas.add(f"[bold blue]{row[0]}, [/] [italic]categoria:[/] [bold]{row[1]}, [/] [italic]Data: [/] [bold]{row[2]}")
        os.system('cls')            
        print(pendentes)
        print()
        print(concluidas)
 