'''
15/09/2023
Programação Estruturada
AC2

Paula Luiza R. de Oliveira
'''

#EX 1
def a_receber(salario, horas):
  total = salario * horas
  print(total)
  print("-"*20)

a_receber(50,20)
a_receber(70,80)

#EX 2   
def numeros(x, y, z):
  print("(1)",(2*x) * (y/2))
  print("(2)",(3*x) + z)
  print("(3)",z ** 3) 
  print("-"*20)

numeros(2,3,4)
numeros(-1,5,10)
numeros(-2,-4,8)

#EX 3
def numeros2(x, y, z):
  return ((2*x) * (y/2))
  return ((3*x) + z)
  return (z ** 3)

numeros2(2,3,4)

#EX 4
def e_bissexto(ano):
  if ano % 4 == 0:
    if ano % 100 == 0:
      if ano % 400 == 0:
        print(ano, "é bissexto")
      else:
        print(ano, "não é bissexto")
    else:
      print(ano, "é bissexto")
    
  else:
    print(ano, "não é bissexto")
  

e_bissexto(1995)
e_bissexto(2012)
e_bissexto(1900)
e_bissexto(2000)


