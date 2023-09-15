'''
15/09/2023
Programação Estruturada
AC1

Paula Luiza R. de Oliveira
'''

#EX 1
a = float(input("Valor de a: "))
b = float(input("Valor de b: "))
c = float(input("Valor de c: "))

delta = (b ** 2) - 4 * a * c
raiz1 = (-b + delta ** 1/2) / 2 * a
raiz2 = (-b - delta ** 1/2) / 2 * a

print("A(s) raíz(es) são: ",raiz1, raiz2)

#EX 2

ano = int(input("Ano: "))
  
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
