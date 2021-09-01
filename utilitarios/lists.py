#lista = usada para armazenar multiplos itens em uma única variável

comida = ["pizza", "hamburguer", "hotdog", "spaghetti", "bolo"]

print(comida[1])
print(comida[::])

comida.append("sorvete") #insere na ultima posicao
comida.remove("hotdog") #remove o elemento escolhido

for i in comida:
     print(i+" ",end="")

print()
comida.pop() #remove o ultimo elemento

for i in comida:
     print(i+" ",end="")

print()
comida.insert(0,"lasanha") #insere numa posicao especifica
for i in comida:
     print(i+" ",end="")

print()
comida.sort() # ordena os itens
for i in comida:
     print(i+" ",end="")

print()

comida.clear() # trunca a lista (limpa)
comida.insert(0,"pipoca")
for i in comida:
    print(i+" ",end="")