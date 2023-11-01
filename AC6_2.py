# EXERCICIO 1

import random

def roda_dado():
    return random.randint(1, 6)

def jogar_dados():
    results= []
    for cont in range(1, 100+1):
        num = roda_dado()
        results.append(num)
    return results

def conta_valores():
    possibilidades = [1,2,3,4,5,6]
    resultados = jogar_dados()
    print(resultados)
    for i in range(6):
        y = possibilidades[i]
        print(f'{y}: {resultados.count(y)} vezes;')
    print('*' * 20)

conta_valores()
  

# EXERCICIO 2

import json

def add_aluno(alunos, matricula, nome, email):
    # adiciona aluno no dicionario
    alunos[matricula] = { 
        "nome": nome,
        "e-mail": email
    }

def pede_dados():
    # verifica se arquivo existe e pede dados dos alunos
    try:
        with open('alunos.json', 'r') as file:
            dados_alunos = json.load(file)
    except FileNotFoundError:
        dados_alunos = {}


    while True:
        matricula = input('Digite o número da matrícula: ')
        nome = input('Digite o nome do aluno: ')
        email = input('Digite o email do aluno: ')
        if matricula == "" or nome == "" or email == "":
            break
        add_aluno(dados_alunos, matricula, nome, email)
        
    escrever_arquivo(dados_alunos)


def escrever_arquivo(dados_alunos):
    # escreve dados no arquivo
    with open('alunos.json', 'w') as file:
        json.dump(dados_alunos, file, indent=4)
        print('Dados salvos.')

pede_dados()


# EXERCÍCIO 3

from datetime import datetime, date
import locale

def recebe_data():
    try:
        locale.setlocale(locale.LC_TIME,'pt')
        usuario = input('Digite uma data no formato DD/MM/AAAA: ')
        data = datetime.strptime(usuario, "%d/%m/%Y")
        print(data.strftime('%d de %B de %Y'))
    except ValueError:
        return None
    
recebe_data()
