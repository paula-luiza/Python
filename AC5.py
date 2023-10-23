"""
21/10/2023
AC5 - PROGRAMAÇÃO ESTRUTURADA
PAULA LUIZA OLIVEIRA
"""

# 1- Recebe um valor de n inteiro imprime até a n-ésima linha

def valor_n():
    num = int(input('Digite um número inteiro:'))
    imprime_num(num)

def imprime_num(num):
    trig = []
    for count in range(1, num+1):
        x = str(count)
        trig.append(x)
        print('  '.join(trig))
        count = count + 1
    print('-' * 20)

valor_n()

# 2-Faça uma função que informe a quantidade de dígitos de um determinado número inteiro informado.

def recebe_num():
    valor = str(input('Digite um número inteiro:'))
    dig = len(valor)
    if '-' in valor:
        dig = len(valor) - 1
    print(f'O número possui {dig} dígitos')
    print('-' * 20)

recebe_num()

# 3 - Recebe 2 números inteiros e divide o 1o pelo 2o

def divisao():
    while True:
        try:
            div1 = int(input('Informe o dividendo: '))
            div2 = int(input('Informe o divisor: '))
            quo = div1 / div2
        except (ValueError, ZeroDivisionError):
            print('Erro!')
        else:
            break
        finally:
            print(quo)
            print('-' * 20)
        
divisao()


        
