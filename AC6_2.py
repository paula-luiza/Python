"""
import json
    >>> obj = ['foo', {'bar': ['baz', None, 1.0, 2]}]
    >>> json.loads('["foo", {"bar":["baz", null, 1.0, 2]}]') == obj
    True
    >>> json.loads('"\\"foo\\bar"') == '"foo\x08ar'
    True
    >>> from io import StringIO
    >>> io = StringIO('["streaming API"]')
    >>> json.load(io)[0] == 'streaming API'
    True
Specializing JSON object 
"""

import json

def add_aluno(alunos, matricula, nome, email):
    alunos[matricula] = { 
        "nome": nome,
        "e-mail": email
    }
    return alunos

def pede_dados():
    with open('alunos.json', 'r') as file:
        dados_alunos = json.load(file)
    while True:
        matricula = input('Digite o número da matrícula')
        nome = input('Digite o nome do aluno: ')
        email = input('Digite o email do aluno: ')
        if matricula == "" or nome == "" or email == "":
            break
        add_aluno(dados_alunos, matricula, nome, email)
    escrever_arquivo(dados_alunos)


def escrever_arquivo(dados_alunos):
    with open('alunos.json', 'w') as file:
        json.dump(dados_alunos, file)
        print('dados salvos')

pede_dados()