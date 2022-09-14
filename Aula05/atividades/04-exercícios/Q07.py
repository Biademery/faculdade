#Faça um algoritmo para ler: número da conta do cliente, saldo, débito e crédito. Após, calcular e escrever o saldo atual (saldo atual = saldo - débito + crédito). Também testar se saldo atual for maior ou igual a zero escrever a mensagem 'Saldo Positivo', senão escrever a mensagem 'Saldo Negativo'.

numero_conta = int(input("Digite o número da sua conta: "))
saldo = int(input("Digite seu saldo: "))
debito = int(input("Digite seu débito: "))
credito = int(input("Digite seu crédito: "))

saldo_atual = int(saldo) - int(debito) + int(credito)

if saldo_atual >= 0:
    print("Saldo positivo")
else:
    print("Saldo negativo")