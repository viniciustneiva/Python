import time

for i in range(10): #laço controlado
    print(i) # 0 1 2 3 4 5 6 7 8 9 
    print(i+1) # 1 2 3 4 5 6 7 8 9 10


for i in range(50,100,2): # o terceiro parâmetro funciona igual o step
    print(i)

for i in "Vinicius":   #imprime letra por letra
    print(i)

for seconds in range (10,0,-1): #contador regressivo
    print(seconds)
    time.sleep(1) #funciona com numeros flutuantes
print("funcionou")