# Solicite ao usuário um valor numérico, inteiro ou real, e verifique se ele é maior ou menor que 10. O programa deve escrever a mensagem correspondente (maior ou menor) e informar o valor digitado pelo usuário.


number = int(input("Digite um número: "))


if number < 10:
    print(f"{number} é menor que 10")
elif number > 10:
    print(f"{number} é maior que 10")

