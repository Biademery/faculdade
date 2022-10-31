# Q02 - Faça um algoritmo para ler um vetor de 30 números. Após isto, ler mais um número qualquer, 
# calcular e escrever quantas vezes esse número aparece no vetor.

from random import randint

vetor = []
quantidade = 0

for i in range(30):
    i = randint(0, 100)
    vetor.append(i)

x = float(input("Digite um número para ver se tem no vetor: "))

for i in vetor:
  if x == i:
    quantidade += 1
print(vetor)
print(f"Quantidade de vezes que o número {x} aparece no vetor: {quantidade}")