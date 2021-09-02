# dicionario = um conjunto de elementos ALTERAVEL, NÃO-ORDENADO, com um unico par de chave:valor
#              Rápido por conta do uso de hashing, permite acesso a um valor rapidamente

capitais ={
    'USA':'Washington DC',
    'India':'New Dheli',
    'China':'Beijing',
    'Russia':'Moscow', 
    'Brasil' : 'Ouro Preto' 
}

#print(capitais['Germany']) # ERRO, pois nao existe o elemento

print(capitais.get('Russia')) # Jeito correto!, caso nao for encontrado, retorna None

print(capitais.keys()) #printa as chaves

print(capitais.values()) # printa os valores
capitais.update({'Brasil' : 'Brasília'})
print(capitais.items()) #printa tudo
capitais.update({'Germany' : 'Berlin'})
capitais.pop('India')
for key,value in capitais.items():
    print(key+" : "+value)

