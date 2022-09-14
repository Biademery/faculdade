# Ler as notas da 1a. e 2a. avaliações de um aluno. Calcular a média aritmética simples e escrever uma mensagem que diga se o aluno foi ou não aprovado (considerar que nota igual ou maior que 6 o aluno é aprovado). Escrever também a média calculada.

av1 = int(input("Nota da AV1: "))
av2 = int(input("Nota da AV2: "))
media = (av1 + av2)/2

if media >= 6:
    print(f"Sua média é {media}, você está aprovado")
else:
    print(f"Sua média é {media}, você está reprovado")