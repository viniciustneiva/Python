#sequencia de iterações com loops aninhados

linhas = int (input("Quantas linhas?: "))
colunas = int(input("Quantas colunas?: "))
simbolo = input("Insira um símbolo: ")

for i in range(linhas):
    for j in range(colunas):
        print(simbolo, end="")
    print()