'''-------> Descrição do Exercício <-------
Altere seu código, da tarefa anterior, para que:

- ao iniciar o programa leia o arquivo texto (bkp.txt) carregando os dados para o dicionário.

- ao finalizar o programa atualize o arquivo bkp.txt, com os novos dados ou empresas acrescidas.
'''

import ast
import os
pesquisa = {}
def menu():
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
            print("Programa Finalizado!")
            break
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
def inserir():
    global pesquisa
    empresa = input("Nome da Empresa: ").upper()
    if not empresa in pesquisa:
        pesquisa[empresa] = []
    else:
        print("Cidade já cadastrada!")
        input("Digite [ENTER] para continuar...")
def avaliacao():
    global pesquisa
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
    global pesquisa
    if len(pesquisa) != 0:
        for empresa,notas in pesquisa.items():
            print('Empresa: ',empresa)
            print('Avaliação:', sum(notas), 'pontos \n')
        input("Digite [ENTER] para continuar...")
    else:
        print("Nenhuma marca foi inserida...")
        input("Digite [ENTER] para continuar...")
def relempresa():
    global pesquisa
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
def carrega_arquivo_txt():
    global pesquisa
    pesquisa = {}
    if os.path.exists('bkp.txt'):
        with open('bkp.txt', 'r') as arq:
            content = arq.read()
            pesquisa = ast.literal_eval(content)
def guarda_arquivo_txt():
    global pesquisa
    with open('bkp.txt', 'w', encoding='utf-8') as arq:
        arq.write(str(pesquisa))


# Main:
carrega_arquivo_txt()
menu()
guarda_arquivo_txt()
