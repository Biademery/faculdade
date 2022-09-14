# Faça um programa que mostre as tabuadas dos números de 1 a 10.
for num in range(1,11):
    print(f"{num} times table")

    for num2 in range(1,11):
        result = num * num2
        print(f'{num} x {num2} = {result}')