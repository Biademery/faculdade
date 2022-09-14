# Crie uma lista de convidados para um jantar em sua casa, com pelo menos 5 celebridades.

celebrity_list = [
    "Lisa Kudrow",
    "David Schwimmer",
    "Matthew Perry",
    "Courtney Cox",
    "Jennifer Aniston"]

# Envie um convite para cada uma dessas pessoas. Com a mesma mensagem e nome personalizado.

for name in celebrity_list:
    print(f"{name}, I'm delighted to invite you for a dinner and drinks. At my Home, 120 Poppy Hill Rd Johnstown, Montana. Saturday, June 7th at 5:30 p.m.")

# Sabendo que uma dessas pessoas não poderá ir ao seu jantar, você deverá enviar novos convites. Imprima o nome das pessoas que não poderão comparecer.

print("Lisa Kudrow can't come to my dinner")

# Modifique sua lista, substitua os desistentes por novos convidados.

new_celebrity_list = [
    "David Schwimmer",
    "Courtney Cox",
    "Matthew Perry",
    "Jennifer Aniston",
    "Matt LeBlanc"]

# Exiba um novo convite para cada pessoa que continua presente em sua lista.

for name in new_celebrity_list:
    print(f"{name}, I'm delighted to invite you for a dinner and drinks. At my Home, 120 Poppy Hill Rd Johnstown, Montana. Saturday, June 7th at 5:30 p.m.")