#Faça um Programa que pergunte quanto você ganha por hora e o número de horas
#trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
salario = float(input("Digite o quanto você ganha por hora: "))
horas = int(input("Digite o número de horas trabalhadas por mês: "))
salario_mensal = salario * horas
print(f"Você ganha R${salario_mensal: .2f} por mês")