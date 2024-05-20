#Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre
#a temperatura em graus Celsius.
graus_f = float(input("Digite a temperatura em graus Fahrenheit: "))
graus_c = (graus_f - 32) * 5 / 9
print(f"A temperatura em graus Celsius é: {graus_c:.2f}")
