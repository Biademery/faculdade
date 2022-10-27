# Q02 - Faça um algoritmo para ler um vetor de 30 números. Após isto, ler mais um número qualquer, 
# calcular e escrever quantas vezes esse número aparece no vetor.

grades = []

for i in range(20):
    grades.append(float(input("Digite uma nota: ")))

accumulator = 0

for grade in grades:
    accumulator = accumulator + grades

sum = accumulator / len(grades)

counter = 0

for g in grades:
    if g > sum:
        counter += 1

print(f"{counter} foram as notas")