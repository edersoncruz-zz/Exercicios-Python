pesquisa = {}
def inserir():
    empresa = input("Nome da Empresa: ").upper()
    if not empresa in pesquisa:
        pesquisa[empresa] = []
    else:
        print("Cidade já cadastrada!")
        input("Digite [ENTER] para continuar...")
def avaliacao():
    if len(pesquisa) != 0:
        print("Marcas para Avaliar: ")
        for marcas in pesquisa.keys():
            print(marcas)
        marcaAval = input("Escolha: ").upper()
        if marcaAval not in pesquisa.keys():
            print("Marca digita não cadastrada...")
            input("Digite [ENTER] para continuar...")
        else:
            print('''   
    1- Péssimo
    2- Ruim
    3- Regular
    4- Bom
    5- Ótimo
                            ''')
            try:
                nota = int(input("Nota: "))
                if nota > 0 and nota < 6:
                    for marca in pesquisa.keys():
                        if marca == marcaAval:
                            pesquisa[marca].append(nota)
                else:
                    print("Digite um número entre 1-5")
                    input("Digite [ENTER] para continuar...")
            except:
                print("Digite um número entre 1-5")
                input("Digite [ENTER] para continuar...")
    else:
        print("Nenhuma marca foi inserida...")
        input("Digite [ENTER] para continuar...")
def relgeral():
    if len(pesquisa) != 0:
        for empresa,notas in pesquisa.items():
            print('Empresa: ',empresa)
            print('Avaliação:', sum(notas), 'pontos \n')
        input("Digite [ENTER] para continuar...")
    else:
        print("Nenhuma marca foi inserida...")
        input("Digite [ENTER] para continuar...")
def relempresa():
    if len(pesquisa) != 0:
        print("Empresa para gerar relatório: ")
        for marcas in pesquisa.keys():
                print(marcas)
        marcaRel = input("Escolha: ").upper()
        if marcaRel not in pesquisa.keys():
            print("Marca digita não cadastrada...")
            input("Digite [ENTER] para continuar...")
        else:
            for empresa,notas in pesquisa.items():
                if empresa == marcaRel:
                    if len(notas) != 0:
                        print("Empresa: ", empresa)
                        print("Notas: ", notas)
                        print("Média: ", sum(notas)/len(notas))
                        input("Digite [ENTER] para continuar...")
                    else:
                        print("Marca digitada sem avaliação...")
                        input("Digite [ENTER] para continuar...")
    else:
        print("Nenhuma marca foi inserida...")
        input("Digite [ENTER] para continuar...")
while True:
    print('''  
0-	Finalizar o Programa
1-	Inserir Empresa
2-	Realizar Avaliação
3-	Relatório Geral
4-	Relatório por Empresa
''')

    num = input("Escolha: ")
    if num == '0':
        quit("Programa Finalizado!")
    elif num == '1':
        inserir()
    elif num == '2':
        avaliacao()
    elif num == '3':
        relgeral()
    elif num == '4':
        relempresa()
    else:
        print("Por favor, Digite um número de 0 até 4 para continuar!")
        input("Digite [ENTER] para continuar...")
