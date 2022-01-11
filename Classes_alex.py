import csv
import pandas as pd

class ToDoList:

    def __init__(self, parametros):
        self.titulo = parametros[0]
        self.data = parametros[2]
        self.categoria = parametros[1]
        self.status = 'Pendente'
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

        with open(self.filename, 'a') as arquivo:
            escritor = csv.writer(arquivo, delimiter=';', lineterminator='\n')
            escritor.writerow(linha)

    def adicionar_tarefa(self, parametros):

        df = pd.read_csv(self.filename)

        self.titulo = parametros[0]
        while self.titulo in df['titulo']:
            self.titulo = input('Dê outro nome à tarefa?')
        
        ToDoList.adicionar_linha(self.filename, parametros)

    @staticmethod
    def altera_status_tarefa(filename, tarefa):
        
        df = pd.read_csv(filename)
        
        linha_titulo = df[df['titulo'] == tarefa]

        if len(linha_titulo) == 0:
            print(f'A tarefa: {tarefa} não exista.')

        if linha_titulo['status'] == 'Pendete':
            linha_titulo['status'] = 'Concluido'
        elif linha_titulo['status'] == 'Concluido':
            linha_titulo['status'] = 'Pendente'
        else:
            linha_titulo['status'] = 'Erro!'