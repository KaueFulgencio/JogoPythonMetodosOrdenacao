# Definição do grafo com as posições e conexões
grafo = {
    (0, 0): [(0, 1)],
    (0, 1): [(0, 0), (1, 1)],
    (1, 1): [(0, 1), (2, 1)],
    (2, 1): [(1, 1), (2, 2)],
    (2, 2): [(2, 1)],
    (3, 3): [(4, 3)],
    (4, 3): [(3, 3)],
}

tipos_terreno = {
    (0, 0): "Terreno A",
    (0, 1): "Terreno B",
    (1, 1): "Terreno C",
    (2, 1): "Terreno D",
}

recompensas = {
    (1, 1): 10,
    (4, 3): 5,
}
