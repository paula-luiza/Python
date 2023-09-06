#AC3
#1 Reajuste de salário

def aumentos(salario):

    print("Salário antes do reajuste:",salario)
    if salario <= 280:
        bonus = salario * 0.2
        salario_novo = salario * 1.2
        print("Bonus liquido de:",bonus)
        print("Bonus de 20%")
        print("Novo salário",salario_novo)

    elif salario > 280 and salario < 700:
        bonus = salario * 0.15
        salario_novo = salario * 1.15
        print("Bonus liquido de:",bonus)
        print("Bonus de 15%")
        print("Novo salário",salario_novo)

    elif salario > 700 and salario < 1500:
        bonus = salario * 0.1
        salario_novo = salario * 1.1
        print("Bonus liquido de:",bonus)
        print("Bonus de 10%")
        print("Novo salário",salario_novo)
    
    elif salario > 1500:
        bonus = salario * 0.05
        salario_novo = salario * 1.05
        print("Bonus liquido de:",bonus)
        print("Bonus de 5%")
        print("Novo salário",salario_novo)

aumentos(1700)

#2 Dias da Semana

def semana(num):
    if num == 1:
        print("Domingo")
    elif num == 2:
        print("Segunda-feira")
    elif num == 3:
        print("Terça-feira")
    elif num == 4:
        print("Quarta-feira")
    elif num == 5:
        print("Quinta-feira")
    elif num == 6:
        print("Sexta-feira")
    elif num == 7:
        print("Sábado")
    else:
        print("Inválido")

semana(5)

#3 Raízes de equação do segundo grau

def raizes(a,b,c):
    if a == 0:
        print("A equação não é do segundo grau")
        return False
    
    delta = b**2 - 4 * a * c

    if delta < 0:
        print("A equação não possui raízes reais")
        return False

    r1 = (-b + delta**(1/2)) / (2 * a)
    r2 = (-b - delta**(1/2)) / (2 * a)
    
    if delta == 0:
        return r1
    elif delta > 0:
        return r1,r2

print (raizes(1,4,4))