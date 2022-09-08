#allowed age
age = int(input("Type your age: "))

if age >= 18:
    print("You can join the party!")
elif age >= 16 and age <18:
    print("It's time to go home")
else:
    print("I'm gonna call your parents.")