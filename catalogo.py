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
        "estrategia_seca": "Armazenamento de água",
        "presenca_de_espinhos": True,
        "epoca_floracao": None,
        "epoca_frutificacao": None,

        # Etnobotânica e Usos
        "uso_principal": "Alimentação e uso ornamental",

        # Status, Distribuição e Registro
        "endemismo_caatinga": False,
        "status_conservacao": None,
        "coordenadas_gps": None,
        "fonte_referencia": None,
    },
    {
        # Xique-xique

        # Identificação
        "nome_popular": "Xique-xique",
        "nome_cientifico": None,
        "genero": None,
        "familia": None,
        "ordem": None,
        "reino": None,
        "bioma": None,

        # Morfologia e Ecologia
        "habito": None,
        "estrategia_seca": None,
        "presenca_de_espinhos": None,
        "epoca_floracao": None,
        "epoca_frutificacao": None,

        # Etnobotânica e Usos
        "uso_principal": "Alimentação e uso ornamental",

        # Status, Distribuição e Registro
        "endemismo_caatinga": None,
        "status_conservacao": None,
        "coordenadas_gps": None,
        "fonte_referencia": None,
    },
    {
        # Coroa-de-frade

        # Identificação
        "nome_popular": "Coroa-de-frade",
        "nome_cientifico": None,
        "genero": None,
        "familia": None,
        "ordem": None,
        "reino": None,
        "bioma": None,
 
        # Morfologia e Ecologia
        "habito": None,
        "estrategia_seca": None,
        "presenca_de_espinhos": None,
        "epoca_floracao": None,
        "epoca_frutificacao": None,
 
        # Etnobotânica e Usos
        "uso_principal": "Alimentação e uso ornamental",
 
        # Status, Distribuição e Registro
        "endemismo_caatinga": None,
        "status_conservacao": None,
        "coordenadas_gps": None,
        "fonte_referencia": None,       
    },
    {
        # Palma-forrageira
        
        # Identificação
        "nome_popular": "Palma-forrageira",
        "nome_cientifico": None,
        "genero": None,
        "familia": None,
        "ordem": None,
        "reino": None,
        "bioma": None,
 
        # Morfologia e Ecologia
        "habito": None,
        "estrategia_seca": None,
        "presenca_de_espinhos": None,
        "epoca_floracao": None,
        "epoca_frutificacao": None,
 
        # Etnobotânica e Usos
        "uso_principal": "Alimentação e uso ornamental",
 
        # Status, Distribuição e Registro
        "endemismo_caatinga": None,
        "status_conservacao": None,
        "coordenadas_gps": None,
        "fonte_referencia": None,     

    }
]

for especie in biodiversidade_de_plantas:
    print("Nome popular:", especie["nome_popular"])
    print("Nome científico:", especie["nome_cientifico"])
    print("Gênero:", especie["genero"])
    print("Família:", especie["familia"])
    print("Ordem:", especie["ordem"])
    print("Reino:", especie["reino"])
    print("Bioma:", especie["bioma"])
    print("Hábito:", especie["habito"])
    print("Estratégia contra a seca:", especie["estrategia_seca"])
    print("Presença de espinhos:", especie["presenca_de_espinhos"])
    print("Época de floração:", especie["epoca_floracao"])
    print("Época de frutificação:", especie["epoca_frutificacao"])
    print("Uso principal:", especie["uso_principal"])
    print("Endemismo:", especie["endemismo_caatinga"])
    print("Status de conservação:", especie["status_conservacao"])
    print("Coordenadas GPS:", especie["coordenadas_gps"])
    print("Fonte:", especie["fonte_referencia"])

def buscar_especie_planta(nome):
    for especie in biodiversidade_de_plantas:
        if especie["nome_popular"].lower() == nome.lower():
            return especie
        
    return None # volta para ao dicionário se não encontrar  


# Condição para a exibição das info

# Mandacaru
resultado = buscar_especie_planta("Mandacaru")
if resultado is not None:
    print(resultado)
else:
    print("Espécie de planta não encontrada")







