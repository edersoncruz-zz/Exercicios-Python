''' -------> Descrição do Exercício <-------
Exercício utilizando Listas

Faça um algoritmo que, através da digitação pelo teclado, armazene várias cidades e seus estados.

Exemplo da estrutura das listas:
lista_de_cidades	lista_de_estados
0 	PORTO ALEGRE	RIO GRANDE DO SUL
1	CANOAS		RIO GRANDE DO SUL
2	GRAVATAI		RIO GRANDE DO SUL
3	FLORIANÓPOLIS	SANTA CATARINA
4	TUBARÃO		SANTA CATARINA
5	SANTA MARIA		RIO GRANDE DO SUL



Exemplo da digitação dos dados:
Digite uma nova cidade: CANOAS
Digite o estado desta cidade: RIO GRANDE DO SUL

Seu programa deverá utilizar o seguinte menu:

Menu
0-	Finalizar o Programa
1-	Adicionar cidades e estados
2-	Listar as cidades e seus respectivos estados
3-	Alterar o nome de uma cidade
4-	Alterar o nome de um estado
5-	Listar todas as cidades de um determinado estado
6-	Retirar da lista uma cidade ou estado
Escolha:

Obs:
- Você não deve aceitar duas cidades com o mesmo nome.
- A opção 2 deverá ser no seguinte formato:
	Relatório Geral:
	Cidade: CANOAS		Estado: RIO GRANDE DO SUL
	Cidade: PORTO ALEGRE	Estado: RIO GRANDE DO SUL
	Cidade: GRAVATAI		Estado: RIO GRANDE DO SUL
	Cidade: FLORIANÓPOLIS	Estado: SANTA CATARINA
	Cidade: TUBARÃO		Estado: SANTA CATARINA

- A Opção 5, deverá pedir ao usuário para escolher um estado e listar todas as cidades deste estado. Exemplo:
Escolha o estado: SANTA CATARINA
As cidades deste estado são:
- FLORIANÓPLIS
- TUBARÃO

- Ao excluir um estado, não esqueça de excluir também todas as cidades relacionadas a este estado.

'''
def adicionar():
    cidadeCad = input('Digite uma nova cidade: ')
    if cidadeCad in listaCidades:
        print("Cidade já cadastrada!")
        input("Pressione [ENTER] para continuar")
    else:
        listaCidades.append(cidadeCad)
        print("Cidade Cadastrada com Sucesso!")
        listaEstados.append(input('Digite o estado dessa cidade: '))
        print("Estado Cadastrado com Sucesso!")
        input("Pressione [ENTER] para continuar")


def visualizar():
    print("Lista de Cidades e Lista de Estados:")
    x = 0
    while x < len(listaCidades):
        print(x, 'Cidade: ',listaCidades[x].ljust(30,'.'),"Estado:" ,listaEstados[x])
        x += 1
    input("Press [ENTER] para continuar")


def alterarc(cid):
    if cid in listaCidades:
        cidadeNov = input("Digite o nome correto: ")
        if cidadeNov in listaCidades:
            print("Cidade já está cadastrada!")
            input("Pressione [ENTER] para continuar")
        else:
            listaCidades[listaCidades.index(cid)] = cidadeNov
    else:
        print('Cidade não está na lista!')
        input("Pressione [ENTER] para continuar")

def alterare(est):
    if est in listaEstados:
        estadoNov = input("Digite o nome correto: ")
        if estadoNov in listaEstados:
            print("Estado já está cadastrada!")
            input("Pressione [ENTER] para continuar")
        else:
            listaEstados[listaEstados.index(est)] = estadoNov
            while est in listaEstados:
                listaEstados[listaEstados.index(est)] = estadoNov
        print("Estado cadastrado com sucesso!")
        input("Pressione [ENTER] para continuar")
    else:
        print('Estado não está na lista!')
        input("Pressione [ENTER] para continuar")

def listar(est):
    if est in listaEstados:
        print('Cidades do estado:', est)
        for i in range(len(listaEstados)-1, -1, -1):
            if listaEstados[i] == est:
                print(listaCidades[i])
        input("Pressione [ENTER] para continuar")
    else:
        print('Estado não está na lista!')
        input("Pressione [ENTER] para continuar")


def excluir(cidest):
    if cidest in listaCidades:
        listaEstados.pop(listaCidades.index(cidest))
        listaCidades.remove(cidest)
        print("Cidade excluída com sucesso!")
        input("Pressione [ENTER] para continuar")
    if cidest in listaEstados:
        listaCidades.pop(listaEstados.index(cidest))
        listaEstados.remove(cidest)
        while cidest in listaEstados:
            listaCidades.pop(listaEstados.index(cidest))
            listaEstados.remove(cidest)
        print('Estado excluído com sucesso!')
        input("Pressione [ENTER] para continuar")

listaCidades = []
listaEstados = []

while True:
    print('''Menu
            0-	Finalizar o Programa
            1-	Adicionar cidades e estados
            2-	Listar as cidades e seus respectivos estados
            3-	Alterar o nome de uma cidade
            4-	Alterar o nome de um estado
            5-	Listar todas as cidades de um determinado estado
            6-	Retirar da lista uma cidade ou estado''')

    num = input('Escolha: ')
    if num == '0':
        quit('Programa Finalizado!')
    elif num == '1':
        adicionar()
    elif num == '2':
        visualizar()
    elif num == '3':
        print("Cidades: ", listaCidades)
        cidade = (input("Qual cidade você deseja alterar? "))
        alterarc(cidade)
    elif num == '4':
        print("Estados: ", listaEstados)
        estado = (input("Qual estado você deseja alterar? "))
        alterare(estado)
    elif num == '5':
        estado = input("Qual estado você deseja listar as cidades? ")
        listar(estado)
    elif num == '6':
        cidest = input("Qual cidade/estado você deseja excluir? ")
        excluir(cidest)
