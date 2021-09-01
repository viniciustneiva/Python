# Declarações para controle de Loops
# break = usado para finalizar o loop COMPLETAMENTE
# continue = avança para a proxima iteração do loop
# pass = não faz nada, apenas marca a posição

#exemplo break 
while True:
    name = input("Digite seu nome: ")
    if name != "":
        break
#exemplo continue
numero_telefone = input("Digite seu telefone: ")

for i in numero_telefone:
    if i == "-":
       continue
    print(i, end="") 
print()
#exemplo pass
for i in range(1, 21):
    if i == 17:
        pass
    else:
        print(str(i)+" ",end="")
