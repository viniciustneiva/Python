

age = int(input("Qual sua idade?: "))


if age == 100:
    print("Você é um ancião!")
elif age >= 18:
    print("Você é maior de idade")
elif age < 0:
    print("Você digitou uma idade invalida")
else:
    print("Você é menor de idade")