"""
13/09/2023
Programação Estruturada

AC4
Paula Oliveira
"""
# EXERCICIO 1
def e_primo(num):
    primo = True
    for div in range(2, num):
        if num % div == 0:
            print(div)
            primo = False
    if primo == True:
         print("O número é primo.")
    else:
        print("O número não é primo.")
    
e_primo(12)
print("-"*15)
e_primo(7)

#EXERCICIO 2
# recebe divida
# mostra opcoes de parcelamento 
# deve ter: valor do juros, valor total da divida (com juros), qnt parcelas e valor parcela

def determina_perc_juros(num):
    if num == 1:
        return 0
    elif num == 3:
        return 0.10
    elif num == 6:
        return 0.15
    elif num == 9:
        return 0.20
    elif num == 12:
        return 0.25

def exibe_dados(divida, num_parcelas):
    taxa_juros = determina_perc_juros(num_parcelas)
    valor_juros = taxa_juros * divida
    divida_total = divida + valor_juros
    valor_parcela = divida_total / num_parcelas

    print("Valor dos Juros: ", valor_juros)
    print("Valor Total: ", divida_total)
    print("Quantidade de Parcelas: ", num_parcelas)
    print("Valor da Parcela", valor_parcela)
    print("-" *20)

def parcela(divida):
    exibe_dados(divida, 1)
    for par in range(3, 13, 3):
        exibe_dados(divida, par)    

parcela(100)

# EXERCICIO 3

def conta_numeros():
    conta = 0
    conta2 = 0
    conta3 = 0
    conta4 = 0
    num = 1

    while num > 0:
        num = int(input("Número: "))
      
        if num >= 0 and num <= 25:
            conta += 1
        elif num >= 26 and num <= 25:
            conta2 += 1
        elif num >= 51 and num <= 75:
            conta3 += 1
        elif num >= 76 and num <= 100:
            conta4 += 1

    print("Números no intervalo [0-25]: ", conta)
    print("Números no intervalo [26-50]: ", conta2)
    print("Números no intervalo [51-75]: ", conta3)
    print("Números no intervalo [76-100]: ", conta4)
   
conta_numeros()


