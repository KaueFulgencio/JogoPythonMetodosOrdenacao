import random

import random

# Definição do grafo com recompensas e tipos de terreno
grafo = {
    (0, 0): [(0, 1)],
    (0, 1): [(0, 2), (1, 1)],
    (0, 2): [(0, 3)],
    (1, 1): [(2, 1)],
    (0, 3): [(1, 3)],
    (1, 3): [(1, 4)],
    (1, 4): [(2, 4)],
    (2, 1): [(3, 1)],
    (3, 1): [(4, 1)],
    (1, 3): [(1, 5)],
    (1, 5): [(2, 5)],
    (2, 4): [(2, 5)],
    (2, 5): [(3, 5)],
    (3, 5): [(4, 5)],
    (4, 1): [(4, 2)],
    (4, 2): [(4, 3)],
    (4, 3): [(4, 4)],
    (4, 4): [(4, 5)],
    (4, 5): [],
    # Adicione mais conexões conforme necessário
}

# Definição dos tipos de terreno e recompensas
tipos_terreno = {
    (0, 0): "Parede",
    (0, 1): "Terreno Normal",
    (0, 2): "Terreno Rochoso",
    (1, 1): "Terreno Normal",
    (0, 3): "Terreno Arenoso",
    (1, 3): "Terreno Normal",
    (1, 4): "Terreno Normal",
    (2, 1): "Terreno Normal",
    (3, 1): "Terreno Pantanoso",
    (1, 3): "Terreno Normal",
    (1, 5): "Terreno Normal",
    (2, 4): "Terreno Normal",
    (2, 5): "Terreno Normal",
    (3, 5): "Terreno Normal",
    (4, 1): "Terreno Normal",
    (4, 2): "Terreno Normal",
    (4, 3): "Terreno Normal",
    (4, 4): "Terreno Normal",
    (4, 5): "Parede",
}

recompensas = {
    (0, 1): 2,
    (0, 3): 5,
    (1, 4): 10,
    (4, 1): 3,
    (3, 5): 8,
    # Adicione mais recompensas conforme necessário
}

# Definição do ponto de partida e objetivo
ponto_inicial = (0, 0)
objetivo = (4, 5)

# Embaralhe o grafo
keys = list(grafo.keys())
random.shuffle(keys)
grafo = {key: grafo[key] for key in keys}

def calcular_custo(posicao_atual, posicao_vizinha):
    terreno_atual = tipos_terreno.get(posicao_atual, "Desconhecido")
    terreno_vizinho = tipos_terreno.get(posicao_vizinha, "Desconhecido")
    
    custo = 0  
    
    if terreno_atual == "Solido e plano":
        if terreno_vizinho == "Solido e plano":
            custo = 1
        elif terreno_vizinho == "Rochoso":
            custo = 10
        elif terreno_vizinho == "Arenoso":
            custo = 4
        elif terreno_vizinho == "Pântano":
            custo = 20
    
    return custo

# Imprima o grafo
for posicao, vizinhos in grafo.items():
    print(f"Posição: {posicao}, Tipo de Terreno: {tipos_terreno.get(posicao, 'Desconhecido')}, Recompensa: {recompensas.get(posicao, 'Nenhuma')}")
    print(f"Vizinhos: {vizinhos}")
    print()

# Imprima o ponto de partida e objetivo
print(f"Ponto de Partida: {ponto_inicial}")
print(f"Objetivo: {objetivo}")
