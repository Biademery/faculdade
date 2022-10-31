# 03 - Ler um vetor Q de 20 posições (aceitar somente números positivos). Escrever a seguir:
# A) O valor do maior elemento de Q e a respectiva posição que ele ocupa no vetor;
from random import randint

Q = []

for i in range(20):
    i = randint(0, 100)
    Q.append(i)


print(f"O valor do maior elemento é {max(Q)}, e sua posição no vetor é a {Q.index(max(Q))}")

# B) O valor do menor elemento de Q e a respectiva posição que ele ocupa no vetor;

print(f"O valor do menor elemento é {min(Q)}, e sua posição no vetor é a {Q.index(min(Q))}")