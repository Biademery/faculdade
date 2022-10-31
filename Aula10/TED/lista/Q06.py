# Q06 - Faça um algoritmo para ler um vetor de 20 números. Após isto, deverá ser lido mais um 
# número qualquer e verificar se esse número existe no vetor ou não. Se existir, o algoritmo deve 
# gerar um novo vetor sem esse número. (Considere que não haverão números repetidos no vetor).

from random import randint

vetor = []

for i in range(20):
    i = randint(0, 100)
    vetor.append(i)


x = float(input("Digite um número para ver se tem no vetor: "))
print(vetor)

if x in vetor:
  vetor.remove(x)
  print(f"Vetor: {vetor}")
else:
  print("Número não encontrado")