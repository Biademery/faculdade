# Faça um cadastro de usuários com nome, idade e email, utilizando apenas o que você aprendeu até agora.

name = input("Type your name: ")
age = int(input("Type your age: "))
email = input("Type your email: ")

person = name, age, email

list = [person]

for person in list:
    print(f"Nome:{name}, age:{age}, email:{email}. Registration successful.")