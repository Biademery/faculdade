# Utilizando a lista do exercício anterior, exiba uma saudação ("Olá como vai você"), personalizado com o nome de cada amigo. A saudação deve ser a mesma, alterando apenas o nome do amigo.
friends_list = [
    "Analicia",
    "Pedro",
    "João",
    "Bia"]

for name in friends_list:
    print(f"Olá, {name}. Como vai você?")