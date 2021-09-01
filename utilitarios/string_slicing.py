# slicing = criar uma "substring" atraves da extracao de elementos de outra string
# indexando[]  ou slice()
# [start:stop:step] sendo START O INICIO (INCLUSO) E STOP (EXCLUSO A IMPRESSAO), ou seja é necessario mais 1 pos
# step é a quantidade de elementos que pulam na contagem, usar -1 para string ao contrario
name = "Vinicius Neiva"

first_name = name[:8] #[0:8]
last_name = name[9:] # [9:fim]

reversed_name = name[::-1] #[0:fim:inverte]
print(first_name)
print(last_name)

print(reversed_name)

website = "http://google.com"
website_two = "http://wikipedia.com"

slice = slice(7,-4)

print(website[slice])
print(website_two[slice])