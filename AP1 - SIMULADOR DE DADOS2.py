"""" 
AP1 - PROGRAMAÇÃO ESTRUTURADA
04/10/2023

PAULA LUIZA ROCHA DE OLIVEIRA
AMANDA

"""""
#EXERCICIO 1 - SIMULADOR DE DADOS

import random

def tam_dado():
    #pede o tamanho do dado, confere se é inteiro ou uma string vazia
    while True:
        dado = input("Forneça o tamanho do dado que está rolando: ") #pergunta o tamanho do dado
        if dado.isnumeric():
            dado = int(dado)
            if dado > 0: 
                return dado  
            else:
                print("Tamanho do dado deve ser maior que 0")#se menor igual que 0 
        elif dado =="":
            return None # vazio, retorna nada
        else: 
            print("Informação inválida.")

def qnt_dado():
    #pede o numero de dados e confere se é inteiro ou string vazia
    while True:
        num = input("Forneça a quantidade de dados que está rolando: ") #pergunta o tamanho do dado
        if num.isnumeric():
            num = int(num)
            if num > 0:
                return num
            else:
                print("Quantidade de dados deve ser maior que 0.") #se menor igual que 0 
        elif num =="":
            return 1 #vazio, retorna 1
        else: 
            print("Informação inválida.")
        
def dado_rola():
    #rola o numero de dados com valores aleatorios
    dado = tam_dado() 
    num = qnt_dado()

    if dado == None:
        return # vazio, retorna
    
    for rolagem in range (1, num+1):
        valor = random.randint(1,dado)
        print("Lançamento n.", rolagem, "-", valor)

    print(num, "dado(s) de ", dado, "lados")

    for _ in range (num):
        print(valor, " ", end='')

"""
def imprime_resultados(j):
    for i in range(1, j):

        pass
"""

dado_rola()