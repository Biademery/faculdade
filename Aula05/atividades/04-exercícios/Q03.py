# As maçãs custam 1,30 cada, se forem compradas menos de uma dúzia, e 1,00 se forem compradas pelo menos 12. Escreva um programa que leia o número de maçãs compradas, calcule e escreva o custo total da compra.

maçãs = int(input("Quantas maçãs você quer comprar: "))

if maçãs < 12:
    valor_maça = maçãs * 1.30
    print(f"{valor_maça} reais")

elif maçãs >= 12:
    valor_maça = maçãs * 1
    print(f"{valor_maça} reais")
