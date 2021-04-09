''' -------> Descrição do Exercício <-------
Exercício de revisão 01

Faça um algoritmo que, através da digitação pelo teclado, armazene em uma lista vários nomes de cidades brasileiras.
Exemplo:
Digite uma nova cidade: CANOAS

Seu programa deverá utilizar o seguinte menu:

Menu
0-	Finalizar o Programa
1-	Cadastrar cidades
2-	Listar as cidades cadastradas
3-	Alterar o nome de alguma cidade digitada erradamente
4-	Excluir uma cidade da lista
Escolha:

Obs:
- Você não deve aceitar duas cidades com o mesmo nome.
'''
def cadastrar():
    cidadeCad = input("Qual cidade você deseja cadastrar? ")
    if cidadeCad in lista:
        print('Cidade já Cadastrada!!')
    else:
        lista.append(cidadeCad)
        print("Cidade Cadastrada com Sucesso!")

def listar():
    print('Cidades Cadastras :', lista)

def alterar():
    print('Cidades: ',lista)
    cidadeAlt = input('Qual cidade você deseja alterar? ')
    if cidadeAlt in lista:
        cidadeNov = input('Qual nome correto? ')
        if cidadeNov in lista:
            print('Cidade já cadastrada!!!')
        else:
            lista[lista.index(cidadeAlt)] = cidadeNov
    else:
        print("Cidade não está na lista!!!!")

def excluir():
    print('Cidades: ', lista)
    cidadeEx = input(('Qual cidade você deseja excluir? '))
    if cidadeEx in lista:
        del(lista[lista.index(cidadeEx)])
    else:
        print("Cidade não está na lista !!!!!")

lista = []

while True:
    print('''Menu 
    0 - Finalizar o programa 
    1 - Cadastrar cidades
    2 - Listar as cidades cadastradas
    3 - Alterar o nome de alguma Cidade digitada erradamente
    4 - Excluir uma cidade da lista''')
    num = int(input('Escolha : '))
    if (num < 0) or (num > 4):
        print('ATENÇÃO ! Digite um número entre 0 e 4!')
    elif num == 0:
        break
    elif num == 1:
        cadastrar()
    elif num == 2:
        listar()
    elif num == 3:
        alterar()
    elif num == 4:
        excluir()
