#Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
inteiro01 = int(input("Digite o primeiro número inteiro: "))
inteiro02 = int(input("Digite o segundo número inteiro: "))
real01 = float(input("Digite o primeiro número real: "))
#1. o produto do dobro do primeiro com metade do segundo .
resultado01 = (inteiro01 * 2) * (inteiro02 / 2)
print(f"O produto do dobro do primeiro com metado do segundo é: \n{inteiro01} x 2 x {inteiro02} : 2 = {resultado01}")
#2. a soma do triplo do primeiro com o terceiro.
resultado02 = (inteiro01 * 3) + real01
print(f"A soma do triplo do primeiro com o terceiro é: \n{inteiro01} x 3 + {real01} = {resultado02}")
#3. o terceiro elevado ao cubo.
resultado03 = real01 ** 3 
print(f"O cubo do terceiro é: \n{real01}^3 = {resultado03}") 