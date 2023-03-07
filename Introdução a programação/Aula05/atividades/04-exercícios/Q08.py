# Faça um algoritmo para ler: quantidade atual em estoque, quantidade máxima em estoque e quantidade mínima em estoque de um produto. Calcular e escrever a quantidade média ((quantidade média = quantidade máxima + quantidade mínima)/2). Se a quantidade em estoque for maior ou igual a quantidade média, escrever a mensagem 'Não efetuar compra', senão escrever a mensagem 'Efetuar compra'.

quant_estoque = int(input("Digite a quantidade atual em estoque: "))
quant_max = int(input("Digite a quantidade máxima em estoque: "))
quant_min = int(input("Digite a quantidade mínima em estoque: "))

quant_media = (int(quant_max) + int(quant_min)/2)

if quant_estoque >= quant_media:
    print("Não efetuar compra")
else:
    print("Efetuar compra")