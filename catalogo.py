biodiversidade_de_plantas = [
    {
        # Mandacaru

        # Identificação Básica e Taxonomia
        "nome_popular": "Mandacaru",
        "nome_cientifico": "Cereus jamacaru",
        "genero": "Cereus",
        "familia": "Cactaceae",
        "ordem": "Caryophyllales",
        "reino": "Plantae",
        "bioma": "Caatinga",

        # Morfologia e Ecologia
        "habito": "Arbusto ou árvore pequena",
        "estrategia_seca": "Armazenamento de água nos caules",
        "presenca_de_espinhos": True,
        "epoca_floracao": "Janeiro, março, abril, julho, setembro, outubro e dezembro (observação de 2010 a 2012)",
        "epoca_frutificacao": "Fevereiro, abril, setembro, outubro e dezembro (observação de 2010 a 2012)",

        # Etnobotânica e Usos
        "uso_principal": "Alimentação humana, forragem animal e uso ornamental",

        # Status, Distribuição e Registro
        "endemismo_caatinga": False,
        "status_conservacao": None,
        "coordenadas_gps": None,
        "fonte_referencia": "Embrapa - Avaliação dos aspectos fenológicos da espécie Cereus jamacaru (2014)",
    },
    {
        # Xique-xique

        # Identificação
        "nome_popular": "Xique-xique",
        "nome_cientifico": "Xiquexique gounellei",
        "genero": "Xiquexique",
        "familia": "Cactaceae",
        "ordem": "Caryophyllales",
        "reino": "Plantae",
        "bioma": "Caatinga e Cerrado",

        # Morfologia e Ecologia
        "habito": "Cacto de crescimento arbustivo",
        "estrategia_seca": "Armazenamento de água nos caules",
        "presenca_de_espinhos": True,
        "epoca_floracao": None,
        "epoca_frutificacao": None,

        # Etnobotânica e Usos
        "uso_principal": "Alimentação e forragem animal",

        # Status, Distribuição e Registro
        "endemismo_caatinga": False,
        "status_conservacao": None,
        "coordenadas_gps": None,
        "fonte_referencia": "Flora e Funga do Brasil - Jardim Botânico do Rio de Janeiro; Flora da APA Serra Branca/Raso da Catarina",
    },
    {
        # Coroa-de-frade

        # Identificação
        "nome_popular": "Coroa-de-frade",
        "nome_cientifico": "Melocactus zehntneri",
        "genero": "Melocactus",
        "familia": "Cactaceae",
        "ordem": "Caryophyllales",
        "reino": "Plantae",
        "bioma": "Caatinga",

        # Morfologia e Ecologia
        "habito": "Cacto suculento de formato globoso",
        "estrategia_seca": "Armazenamento de água no caule",
        "presenca_de_espinhos": True,
        "epoca_floracao": None,
        "epoca_frutificacao": None,

        # Etnobotânica e Usos
        "uso_principal": "Uso ornamental",

        # Status, Distribuição e Registro
        "endemismo_caatinga": None,
        "status_conservacao": None,
        "coordenadas_gps": None,
        "fonte_referencia": "Flora e Funga do Brasil; identificação científica pendente de confirmação",
    },
    {
        # Palma-forrageira

        # Identificação
        "nome_popular": "Palma-forrageira",
        "nome_cientifico": "Opuntia ficus-indica",
        "genero": "Opuntia",
        "familia": "Cactaceae",
        "ordem": "Caryophyllales",
        "reino": "Plantae",
        "bioma": "Caatinga (cultivada no Semiárido)",

        # Morfologia e Ecologia
        "habito": "Planta suculenta de crescimento arbustivo",
        "estrategia_seca": "Armazenamento de água nos cladódios",
        "presenca_de_espinhos": None,
        "epoca_floracao": None,
        "epoca_frutificacao": None,

        # Etnobotânica e Usos
        "uso_principal": "Forragem para alimentação animal",

        # Status, Distribuição e Registro
        "endemismo_caatinga": False,
        "status_conservacao": None,
        "coordenadas_gps": None,
        "fonte_referencia": "Embrapa - Cultivares de Palma Forrageira; Instituto Nacional do Semiárido",
    }
]

# Recebe cada dicionário da lista, um de cada vez
def buscar_especie_planta(nome):

    for especie in biodiversidade_de_plantas:

        if especie["nome_popular"].lower() == nome.lower():

            return especie

    return None # retorna None se não encontrar

def buscar_especie_por_nome_cientifico(nome_cientifico):

    for especie in biodiversidade_de_plantas:

        if especie["nome_cientifico"] is not None:

            if especie["nome_cientifico"].lower() == nome_cientifico.lower():

                return especie

    return None


# Função responsável por exibir as informações de uma espécie
# Recebe o dicionário da planta encontrado pela função de busca

def exibir_informacoes_especie(especie):

    print("\n" + "="*20)
    print(     "PROJECT_CAATINGA")
    print(  "CATÁLOGO DA BIODIVERSIDADE")
    print("\n" + "="*20)

    # Identificação Básica 
    print("\n", especie ["nome_popular"].upper())

    if especie["nome_cientifico"] is not None:
        print("Nome científico:", especie["nome_cientifico"])
    else:
        print("Nome científico: Não informado") 

    # Taxonomia
    print("\n[ 01 ] IDENTIFICAÇÃO E TAXONOMIA")
    print("-"*20)

    if especie ["genero"] is not None:
        print("Genero:", especie["genero"])
    else:
        print("Genero: Não informado")

    if especie ["familia"] is not None:
        print("Família:", especie["familia"])
    else:
        print("Família: Não informado")

    if especie ["ordem"] is not None:
        print("Ordem:", especie["ordem"])
    else:
        print("Ordem: Não informado")

    if especie ["reino"] is not None:
        print("Reino:", especie["reino"])
    else:
        print("Reino: Não informado")  

    if especie ["bioma"] is not None:
        print("Bioma:", especie["bioma"])
    else:
        print("Bioma: Não informado")  

    # Morfologia e ecologia
    print("\n[ 02 ] MORFOLOGIA E ECOLOGIA")
    print("-"*20)

    if especie ["habito"] is not None:
        print("Hábito:", especie["habito"])
    else:
        print("Hábito: Não informado")  

    if especie ["estrategia_seca"] is not None:
        print("Estratégia contra a seca:", especie["estrategia_seca"])
    else:
        print("Estratégia contra a seca: Não informado")  

    if especie ["presenca_de_espinhos"] is True:
        print("presença de espinhos: Sim")
    elif especie ["presenca_de_espinhos"] is False:
        print("presença de espinhos: Não")
    else:
        print("presença de espinhos: Não informado")

    if especie ["epoca_floracao"] is not None:
        print("Época de floração:", especie["epoca_floracao"])
    else:
        print("Época de floração: Não informado") 

    if especie ["epoca_frutificacao"] is not None:
        print("Época de frutificação:", especie["epoca_frutificacao"])
    else:
        print("Época de frutificação: Não informado")

    # Etnobotânica e Usos
    print("\n[ 03 ] ETNOBOTÂNICA E USOS")
    print("-"*20)

    if especie ["uso_principal"] is not None:
        print("Uso principal:", especie["uso_principal"])
    else:
        print("Uso principal: Não informado")

    # Status, Distribuição e Registro
    print("\n[ 04 ] CONSERVAÇÃO E DISTRIBUIÇÃO")
    print("-"*20)

    if especie["endemismo_caatinga"] is True:
        print("Endemismo na Caatinga: Sim")
    elif especie["endemismo_caatinga"] is False:
        print("Endemismo na Caatinga: Não")
    else:
        print("Endemismo na Caatinga: Não informado")


# Menu interativo
while True:

    print("=== Menu PRINCIPAL ====")
    print("1 - Consultar espécie")
    print("2 - Consultar espécie pelo nome científico")
    print("0 - sair")

    # aceita apenas 1, 2 ou 0 como escolha
    while True:

        opcao = input("Escolha uma opção (1, 2 ou 0):\n ")

        if opcao == "0" or opcao == "1" or opcao == "2":
            break
        else:
            print("Entrada inválida! Digite 1, 2 ou 0.")


    # opção para consultar a espécie
    if opcao == "1":

        # Solicita ao usuário o nome popular da espécie
        while True:
            try:

                nome_da_especie = input("Digite o nome popular da espécie:\n").strip()

                # Verifica se está vazio ou se existe qualquer número no texto
                if not nome_da_especie or any(caractere.isdigit() for caractere in nome_da_especie):
                    raise ValueError

                break

            except ValueError:
                print("Não foi possível identificar a espécie, tente novamente")

        print(f"Nome informado: {nome_da_especie}")
        
        # Condição para a exibição das info
        resultado = buscar_especie_planta(nome_da_especie)

        if resultado is not None:
            exibir_informacoes_especie(resultado)
        else:
            print("Espécie não encontrada, tente novamente")


    elif opcao == "2":

        # Solicita ao usuário o nome científico da espécie
        while True:
            try:

                nome_cientifico = input("Digite o nome científico da espécie:\n ").strip()

                #verifica se está vazio ou se existe qualquer número no texto
                if not nome_cientifico or any(caractere.isdigit() for caractere in nome_cientifico):
                    raise ValueError

                break

            except ValueError:
                print("Não foi possível identificar a espécie, tente novamente")

        print(f"Nome científico informado: {nome_cientifico}")

        # Condição para a exibição das info
        resultado = buscar_especie_por_nome_cientifico(nome_cientifico)

        if resultado is not None:
            exibir_informacoes_especie(resultado)
        else:
            print("Espécie não encontrada, tente novamente")

    # opção para fechar o menu
    elif opcao == "0":

        print("Encerrando o programa...")
        break

    else:
        print("Opção inválida, tente novamente")
