'''-------> Descrição do Exercício <-------
Tarefa 1 – Dicionários
Competências:
- Desenvolver um algoritmo viável para o problema;
- Saber utilizar as funções corretamente;
- Saber utilizar os comandos adequadamente;
- Gerar solução utilizando a estrutura de dicionários do python.
A reportagem acima, fala basicamente sobre o mercado de processadores no mundo. O
destaque fica para os processadores da Qualcomm, HiSilicon, Apple, Samsung e MediaTek.
Problema:
Faça um algoritmo que realize uma pesquisa de satisfação sobre qual das empresas acima o
usuário mais se identifica. Em sua pesquisa o usuário deverá escolher qual empresa ele mais
gosta e para essa empresa o usuário deve dar uma nota de 1 a 5.
Armazene esses dados em um dicionário ( pesquisa = {} ), a empresa e a nota para essa
empresa.
Armazene esses dados no dicionário utilizando o nome da empresa como chave, e as notas
recebidas em uma lista.
Não é necessária nenhuma identificação, ou validação do usuário. Este apenas escolhe uma
empresa e uma nota. Podendo realizar essas notas quantas vezes desejar.
Como sugestão:
Seu programa poderá utilizar o seguinte menu como guia:
Menu
0- Finalizar o Programa
1- Inserir Empresa
2- Realizar avaliação
3- Relatório geral
4- Relatório por empresa
Escolha:
Obs:
- Uma pessoa não precisa avaliar todas as empresas.
Na Opção 1: Ao inserir a empresa, validar para não inserir mais que uma vez a mesma empresa.
Na Opção 2: Ao realizar a avaliação, você deverá escolher uma das empresas do dicionário, e
avaliar com uma nota inteira de 1 a 5.
1- Péssimo
2- Ruim
3- Regular
4- Bom
5- Ótimo
Na Opção 3: Você deverá mostrar o nome da empresa e a soma de suas notas.
Na Opção 4: Você deverá escolher uma das empresas e mostrar suas notas individualmente e
no final, a média das notas recebidas.
Exemplo de como pode ficar o dicionário:
pesquisa {
QUALCOMM: [4,4,5,5,3,4]
HISILICON: [4,4,4,4,2,3,3,5]
APPLE: [5,5,4,4]
}
Você pode pensar em uma outra forma de montar o dicionário. Não precisa ser assim. Faça como
achar mais conveniente.
'''
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
