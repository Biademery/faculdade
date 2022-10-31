# Q05 - Crie um vetor N que seja resultado da soma dos itens de outros dois vetores A e B.
#  Exemplo: A[0] + B[0] deverá ser salva em N[0].
from random import randint

N = []
A = []
B = []

for i in range(10):
    i = A.append(randint(0, 100))

for j in range(10):
    j = B.append(randint(0, 100))

for x in range(10):
  N.append(A[i] + B[j])

print(N)
