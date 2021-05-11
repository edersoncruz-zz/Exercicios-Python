# Abrir/ou criar o arquivo
arq = open("meu_arquivo.txt", "a") #w-escrita/criar r- leitura a-adicionar

#manipular conteúdo
arq.write("Linha 1"+"\n")
arq.write("Linha 2"+"\n")
arq.write("Linha 3"+"\n")
arq.write("123"+"\n")

arq.close()

a = open("meu_arquivo.txt", "r")
for x in a:
    print(x)
a.close()
