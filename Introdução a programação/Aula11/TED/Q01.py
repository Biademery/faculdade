# Q01 - Escreva um algoritmo que permita a leitura dos nomes de 10 clubes de futebol e armazene os 
# nomes lidos em um vetor (lista). Após isto, o algoritmo deve permitir a leitura de mais 1 nome 
# qualquer de clube e depois escrever a mensagem ACHEI, se o nome estiver entre os 10 nomes lidos 
# anteriormente (guardados no vetor), ou NÃO ACHEI caso contrário


clubs = []

for a in range(10):
    clubs.append(input("Digite um novo clube: "))

search_club = input("Digite o clube que deseja buscar: ")

for b in clubs:
    if search_club == b:
        print("Achei!")
    else:
        print("Não achei!")