#Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que
#calcule seu peso ideal, utilizando as seguintes fórmulas:
#1. Para homens: (72.7*h) - 58
#2. Para mulheres: (62.1*h) - 44.7
altura = float(input("Digite a sua altura em metros: "))
genero = input("Digite o seu gênero (M para masculino, F para feminino): ").strip().upper()  # strip para que os espacos não interfiram na resposta e upper para caso maiuscula ou minuscula
if genero == 'M':
    peso_ideal = (72.7 * altura) - 58
elif genero == 'F':  # Corrigido para elif
    peso_ideal = (62.1 * altura) - 44.7
else:
    peso_ideal = None

if peso_ideal is not None:
    print(f"Seu peso ideal é: {peso_ideal:.2f} kg")
else:
    print("Gênero inválido. Use 'M' para masculino ou 'F' para feminino.")

