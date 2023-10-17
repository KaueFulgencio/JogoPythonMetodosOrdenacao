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
}

# Embaralhe o grafo
keys = list(grafo.keys())
random.shuffle(keys)
grafo = {key: grafo[key] for key in keys}

# Dicionário de tipos de terreno e recompensas
tipos_terreno = {
    (0, 0): "Solido e plano",
    (0, 1): "Solido e plano",
    (0, 2): "Solido e plano",
    (1, 1): "Solido e plano",
    (0, 3): "Solido e plano",
    (1, 3): "Solido e plano",
    (1, 4): "Solido e plano",
    (2, 1): "Solido e plano",
    (3, 1): "Solido e plano",
    (1, 3): "Solido e plano",
    (1, 5): "Solido e plano",
    (2, 4): "Solido e plano",
    (2, 5): "Solido e plano",
    (3, 5): "Solido e plano",
    (4, 1): "Solido e plano",
    (4, 2): "Solido e plano",
    (4, 3): "Solido e plano",
    (4, 4): "Solido e plano",
    (4, 5): "Solido e plano",
}

recompensas = {
    (1, 1): 10,  # Exemplo de recompensa na posição (1, 1)
    (3, 3): 5,   # Exemplo de recompensa na posição (3, 3)
    # Adicione mais recompensas conforme necessário
}

# Definição do ponto de partida e objetivo
ponto_inicial = (0, 0)
objetivo = (4, 5)

# Função para calcular o custo com base no tipo de terreno
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
