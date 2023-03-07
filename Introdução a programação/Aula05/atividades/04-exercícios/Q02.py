# Solicite ao usuário um valor numérico, inteiro ou real, e escrever se é positivo ou negativo (considere o valor zero como positivo).

number = int(input("Digite um número: "))

if number < 0:
    print("O número é negativo")
elif number >= 0:
    print("O número é positivo")