#   tupla = conjunto ordenando, inalterável e indexável
#           usado para agrupar dados diversos

estudante = ("Neiva",21,"masculino")

print(estudante.count("Neiva")) #conta quantas vezes aparece
print(estudante.index("masculino")) #retorna a posicao

for i in estudante:
    print(str(i)+" ",end="")
print()
if "Neiva" in estudante:
    print("ele está aqui")