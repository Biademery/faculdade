# Q04 - Ler um vetor A de 10 números. Após, ler mais um número e guardar em uma variável X. 
# Armazenar em um vetor M o resultado de cada elemento de A multiplicado pelo valor X. Logo após, 
# imprimir o vetor M.
from random import randint

A = []
M = []


for i in range(10):
    i = A.append(randint(0, 100))

x = randint(0, 9)

for i in range(len(A)):
    M.append(x * A[i])

print(f"M: {M}")
    
