

temp = int(input("Qual a temperatura atual? "))

if not(temp >= 0 and temp <= 30):
    print("O tempo está zoado")
    
elif not(temp < 0 or temp > 30):
    print("A temperatura está suave")

