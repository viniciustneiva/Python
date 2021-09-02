# set conjunto desordenado, não-indexado. Não duplica valores

utensilios = {"garfo", "colher", "faca"} #mesmo que tenham varios elementos iguais, não são considerados
louça = {"tijela", "prato", "copo", "faca"}
# utensilios.add("tesoura")
# utensilios.remove("garfo")
# utensilios.clear()
# utensilios.update(louça) # uniao entre os conjuntos sem repitir elementos iguais
mesa_de_jantar = utensilios.union(louça) #elementos encontrados nos dois conjuntos

for x in mesa_de_jantar:
    print(x)

print(utensilios.difference(louça)) # tudo que está no elemento de chamada que nao tem no do parametro

print(utensilios.intersection(louça)) #retorna elementos em comum
