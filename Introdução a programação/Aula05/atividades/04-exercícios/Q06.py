# Ler dois valores (considere que não serão lidos valores iguais) e escrevê-los em ordem crescente.

number1 = int(input("Digite um número: "))
number2 = int(input("Digite um número: "))
numbers = [number1, number2]

numbers.sort()

print(numbers)