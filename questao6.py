#Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em
#graus Fahrenheit.
graus_c = float(input("Digite a temperatura em graus Celsius: "))
graus_f = (graus_c * 1.8) + 32
print(f"A temperatura em graus Fahrenheit é: {graus_f:.2f}")