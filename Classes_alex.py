import csv
import pandas as pd
class ToDoList:

    def __init__(self, titulo, data, categoria, status = 'Pendente'):
        self.titulo = titulo
        self.data = data
        self.categoria = categoria
        self.status = status
        self.filename = 'to_do_list.csv'

    def adicionar_linha(filename: str, linha: list):
        '''Função para adicionar uma nova tarefa'''
        try:
            open(filename)
        except FileNotFoundError as error:
            print('Arquivo não encontrado.', error)
        except KeyError:
            print('Chave não encontrada.')
        except Exception as error:
            print('Erro genérico:', error)

        with open(filename, 'a') as arquivo:
            escritor = csv.writer(arquivo, delimiter=';', lineterminator='\n')
            escritor.writerow(linha)

    def adicionar_tarefa(self):

        df = pd.read_csv(self.filename)

        self.titulo = input('Qual o título da tarefa?')
        self.data = input('Qual a sua data de realização?')
        self.categoria = input('Qual a categoria da tarefa? ')
        self.status = 'Pendente'
        
        linha_tarefa = [self.titulo, self.data, self.categoria, self.status]
        
        while self.titulo in df['titulo']:
            self.titulo = input('Dê outro nome à tarefa?')
        
        ToDoList.adicionar_linha(self.filename, linha_tarefa)

    def altera_status_tarefa(self, filename, title):
        
        df = pd.read_csv(filename)
        linha_titulo = df[df['titulo'] == title]

        if linha_titulo['status'] == 'Pendete':
            linha_titulo['status'] = 'Concluido'
        elif linha_titulo['status'] == 'Concluido':
            linha_titulo['status'] = 'Pendente'
        else:
            linha_titulo['status'] = 'Erro!'