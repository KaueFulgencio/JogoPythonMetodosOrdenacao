'''
grafo = {
    (0, 0): [(0, 1), (1, 0)],
    (0, 1): [(0, 0), (1, 1)],
    (1, 0): [(0, 0), (1, 1)],
    (1, 1): [(0, 1), (1, 0), (2, 2)],
    (2, 2): [(1, 1), (3, 3)],
    (3, 3): [(2, 2), (4, 5)],
    (4, 5): [(3, 3), (5, 5)],
    (5, 5): [(4, 5)],
}
'''

grafo = {
    (0, 0): {'terreno': 'solida', 'custo': 1, 'conexoes': [(0, 1), (1, 0)]},
    (0, 1): {'terreno': 'solida', 'custo': 1, 'conexoes': [(0, 0), (1, 1), (0, 2)]},
    (0, 2): {'terreno': 'rochosa', 'custo': 10, 'conexoes': [(0, 1), (1, 2)]},
    (1, 0): {'terreno': 'solida', 'custo': 1, 'conexoes': [(0, 0), (1, 1), (2, 0)]},
    (1, 1): {'terreno': 'arenosa', 'custo': 4, 'conexoes': [(0, 1), (1, 0), (1, 2), (2, 1)]},
    (1, 2): {'terreno': 'solida', 'custo': 1, 'conexoes': [(0, 2), (1, 1)]},
    (2, 0): {'terreno': 'rochosa', 'custo': 10, 'conexoes': [(1, 0), (2, 1)]},
    (2, 1): {'terreno': 'solida', 'custo': 1, 'conexoes': [(1, 1), (2, 0), (2, 2)]},
    (2, 2): {'terreno': 'solida', 'custo': 1, 'conexoes': [(1, 2), (2, 1), (3, 3)]},
    (3, 3): {'terreno': 'solida', 'custo': 1, 'conexoes': [(2, 2), (4, 5)]},
    (4, 5): {'terreno': 'pantano', 'custo': 20, 'conexoes': [(3, 3), (5, 5)]},
    (5, 5): {'terreno': 'solida', 'custo': 1, 'conexoes': [(4, 5), (6, 6)]},
    (6, 6): {'terreno': 'solida', 'custo': 1, 'conexoes': [(5, 5), (6, 7)]},
    (6, 7): {'terreno': 'solida', 'custo': 1, 'conexoes': [(6, 6), (7, 7)]},
    (7, 7): {'terreno': 'arenosa', 'custo': 4, 'conexoes': [(6, 7), (8, 7)]},
    (8, 7): {'terreno': 'solida', 'custo': 1, 'conexoes': [(7, 7), (8, 8)]},
    (8, 8): {'terreno': 'solida', 'custo': 1, 'conexoes': [(8, 7), (9, 9)]},
    (9, 9): {'terreno': 'arenosa', 'custo': 4, 'conexoes': [(8, 8), (9, 10)]},
    (9, 10): {'terreno': 'solida', 'custo': 1, 'conexoes': [(9, 9), (10, 10)]},
    (10, 10): {'terreno': 'pantano', 'custo': 20, 'conexoes': [(9, 10), (10, 11)]},
    (10, 11): {'terreno': 'arenosa', 'custo': 4, 'conexoes': [(10, 10), (10, 12)]},
    (10, 12): {'terreno': 'solida', 'custo': 1, 'conexoes': [(10, 11)]}
}



custos = {
    (0, 0): 1,  # Terreno sólido e plano
    (0, 1): 1,  # Terreno sólido e plano
    (1, 0): 1,  # Terreno sólido e plano
    (1, 1): 1,  # Terreno sólido e plano
    (2, 2): 10, # Terreno rochoso
    (3, 3): 4,  # Terreno arenoso
    (4, 5): 20, # Terreno pântano
    (5, 5): 1,  # Terreno sólido e plano
}

recompensas = {
    (1, 1): 10,
    (4, 5): 5,
}

def carregar_dados():
    return grafo, recompensas, custos