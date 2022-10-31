# Q02 - Escreva um algoritmo que permita a leitura das notas de uma turma de 20 alunos.
#  Calcular a média da turma e contar quantos alunos obtiveram nota acima desta média calculada.
#  Escrever a média da turma e o resultado da contagem.

notas = []
soma = 0
contador = 0

for nota in range(20):
    notas.append(float(input("Digite uma nota: ")))
    soma = soma + notas[nota]

media = soma/20

for nota in notas:
    if nota > media:
        contador += 1
        
print(f"A média da turma foi {media}, e {contador} alunos tiveram a nota maior que a média!")