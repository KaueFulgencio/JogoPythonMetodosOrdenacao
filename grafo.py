grafo = {
    (0, 0): {'terreno': 'solida', 'custo': 1, 'conexoes': [(0, 1), (1, 0)]},
    (0, 1): {'terreno': 'solida', 'custo': 1, 'conexoes': [(0, 0), (0, 2), (1, 1)]},
    (0, 2): {'terreno': 'rochosa', 'custo': 10, 'conexoes': [(0, 1), (0, 3), (1, 2)]},
    (0, 3): {'terreno': 'rochosa', 'custo': 10, 'conexoes': [(0, 2), (1, 3)]},
    (1, 0): {'terreno': 'solida', 'custo': 1, 'conexoes': [(0, 0), (1, 1), (2, 0)]},
    (1, 1): {'terreno': 'arenosa', 'custo': 4, 'conexoes': [(0, 1), (1, 0), (1, 2), (2, 1)]},
    (1, 2): {'terreno': 'solida', 'custo': 1, 'conexoes': [(0, 2), (1, 1), (1, 3)]},
    (1, 3): {'terreno': 'solida', 'custo': 1, 'conexoes': [(0, 3), (1, 2), (2, 3)]},
    (2, 0): {'terreno': 'rochosa', 'custo': 10, 'conexoes': [(1, 0), (2, 1), (3, 0)]},
    (2, 1): {'terreno': 'solida', 'custo': 1, 'conexoes': [(1, 1), (2, 0), (2, 2)]},
    (2, 2): {'terreno': 'solida', 'custo': 1, 'conexoes': [(1, 2), (2, 1), (3, 2)]},
    (2, 3): {'terreno': 'solida', 'custo': 1, 'conexoes': [(1, 3), (3, 3)]},
    (3, 0): {'terreno': 'rochosa', 'custo': 10, 'conexoes': [(2, 0), (3, 1), (4, 0)]},
    (3, 1): {'terreno': 'rochosa', 'custo': 10, 'conexoes': [(2, 1), (3, 0), (3, 2)]},
    (3, 2): {'terreno': 'solida', 'custo': 1, 'conexoes': [(2, 2), (3, 1), (3, 3)]},
    (3, 3): {'terreno': 'solida', 'custo': 1, 'conexoes': [(2, 3), (3, 2), (4, 3)]},
    (4, 0): {'terreno': 'solida', 'custo': 1, 'conexoes': [(3, 0), (4, 1), (5, 0)]},
    (4, 1): {'terreno': 'arenosa', 'custo': 4, 'conexoes': [(3, 1), (4, 0), (4, 2)]},
    (4, 2): {'terreno': 'solida', 'custo': 1, 'conexoes': [(3, 2), (4, 1), (4, 3)]},
    (4, 3): {'terreno': 'rochosa', 'custo': 10, 'conexoes': [(3, 3), (4, 2), (5, 3)]},
    (4, 4): {'terreno': 'solida', 'custo': 1, 'conexoes': [(3, 4), (4, 3), (5, 4)]},
    (4, 5): {'terreno': 'solida', 'custo': 1, 'conexoes': [(3, 5), (4, 4), (5, 5)]},
    (5, 0): {'terreno': 'solida', 'custo': 1, 'conexoes': [(4, 0), (5, 1), (6, 0)]},
    (5, 1): {'terreno': 'arenosa', 'custo': 4, 'conexoes': [(4, 1), (5, 0), (5, 2)]},
    (5, 2): {'terreno': 'solida', 'custo': 1, 'conexoes': [(4, 2), (5, 1), (5, 3)]},
    (5, 3): {'terreno': 'solida', 'custo': 1, 'conexoes': [(4, 3), (5, 2), (6, 3)]},
    (5, 4): {'terreno': 'solida', 'custo': 1, 'conexoes': [(4, 4), (5, 3), (6, 4)]},
    (5, 5): {'terreno': 'rochosa', 'custo': 10, 'conexoes': [(4, 5), (5, 4), (6, 5)]},
    (6, 0): {'terreno': 'solida', 'custo': 1, 'conexoes': [(5, 0), (6, 1), (7, 0)]},
    (6, 1): {'terreno': 'solida', 'custo': 1, 'conexoes': [(5, 1), (6, 0), (6, 2)]},
    (6, 2): {'terreno': 'arenosa', 'custo': 4, 'conexoes': [(5, 2), (6, 1), (6, 3)]},
    (6, 3): {'terreno': 'solida', 'custo': 1, 'conexoes': [(5, 3), (6, 2), (7, 3)]},
    (6, 4): {'terreno': 'solida', 'custo': 1, 'conexoes': [(5, 4), (6, 3), (7, 4)]},
    (6, 5): {'terreno': 'arenosa', 'custo': 4, 'conexoes': [(5, 5), (6, 4), (7, 5)]},
    (7, 0): {'terreno': 'solida', 'custo': 1, 'conexoes': [(6, 0), (7, 1), (8, 0)]},
    (7, 1): {'terreno': 'solida', 'custo': 1, 'conexoes': [(6, 1), (7, 0), (7, 2)]},
    (7, 2): {'terreno': 'rochosa', 'custo': 10, 'conexoes': [(6, 2), (7, 1), (7, 3)]},
    (7, 3): {'terreno': 'solida', 'custo': 1, 'conexoes': [(6, 3), (7, 2), (8, 3)]},
    (7, 4): {'terreno': 'solida', 'custo': 1, 'conexoes': [(6, 4), (7, 3), (8, 4)]},
    (7, 5): {'terreno': 'solida', 'custo': 1, 'conexoes': [(6, 5), (7, 4), (8, 5)]},
    (8, 0): {'terreno': 'arenosa', 'custo': 4, 'conexoes': [(7, 0), (8, 1), (9, 0)]},
    (8, 1): {'terreno': 'solida', 'custo': 1, 'conexoes': [(7, 1), (8, 0), (8, 2)]},
    (8, 2): {'terreno': 'solida', 'custo': 1, 'conexoes': [(7, 2), (8, 1), (8, 3)]},
    (8, 3): {'terreno': 'arenosa', 'custo': 4, 'conexoes': [(7, 3), (8, 2), (9, 3)]},
    (8, 4): {'terreno': 'arenosa', 'custo': 4, 'conexoes': [(7, 4), (8, 3), (8, 5)]},
    (8, 5): {'terreno': 'solida', 'custo': 1, 'conexoes': [(7, 5), (8, 4), (9, 5)]},
    (9, 0): {'terreno': 'solida', 'custo': 1, 'conexoes': [(8, 0), (9, 1), (10, 0)]},
    (9, 1): {'terreno': 'solida', 'custo': 1, 'conexoes': [(8, 1), (9, 0), (9, 2)]},
    (9, 2): {'terreno': 'rochosa', 'custo': 10, 'conexoes': [(8, 2), (9, 1), (9, 3)]},
    (9, 3): {'terreno': 'solida', 'custo': 1, 'conexoes': [(8, 3), (9, 2), (10, 3)]},
    (9, 4): {'terreno': 'solida', 'custo': 1, 'conexoes': [(8, 4), (9, 3), (9, 5)]},
    (9, 5): {'terreno': 'solida', 'custo': 1, 'conexoes': [(8, 5), (9, 4), (10, 5)]},
    (10, 0): {'terreno': 'solida', 'custo': 1, 'conexoes': [(9, 0), (10, 1), (11, 0)]},
    (10, 1): {'terreno': 'solida', 'custo': 1, 'conexoes': [(9, 1), (10, 0), (10, 2)]},
    (10, 2): {'terreno': 'solida', 'custo': 1, 'conexoes': [(9, 2), (10, 1), (10, 3)]},
    (10, 3): {'terreno': 'solida', 'custo': 1, 'conexoes': [(9, 3), (10, 2), (11, 3)]},
    (10, 4): {'terreno': 'rochosa', 'custo': 10, 'conexoes': [(9, 4), (10, 3), (11, 4)]},
    (10, 5): {'terreno': 'solida', 'custo': 1, 'conexoes': [(9, 5), (10, 4)]},
    (11, 0): {'terreno': 'arenosa', 'custo': 4, 'conexoes': [(10, 0), (11, 1)]},
    (11, 1): {'terreno': 'solida', 'custo': 1, 'conexoes': [(10, 1), (11, 0), (11, 2)]},
    (11, 2): {'terreno': 'rochosa', 'custo': 10, 'conexoes': [(10, 2), (11, 1), (11, 3)]},
    (11, 3): {'terreno': 'solida', 'custo': 1, 'conexoes': [(10, 5), (11, 4)]},
    (11, 4): {'terreno': 'solida', 'custo': 1, 'conexoes': [(10, 5)]},
}
#1 = Terreno sólido e plano
#4 =  Terreno arenoso
#10 =  Terreno rochoso
custos = {
    (0, 0): 1,  
    (0, 1): 1,  
    (0, 2): 1,  
    (0, 3): 10, 
    (0, 4): 1,  
    (0, 5): 20, 
    (1, 0): 1,  
    (1, 1): 1,  
    (1, 2): 1,  
    (1, 3): 4,  
    (1, 4): 1,  
    (1, 5): 1,  
    (2, 0): 10, 
    (2, 1): 1,  
    (2, 4): 1,  
    (2, 5): 1,  
    (3, 2): 4,  
    (3, 3): 1,  
    (3, 4): 20, 
    (3, 5): 20, 
    (4, 0): 1,  
    (4, 1): 4,  
    (4, 2): 1,  
    (4, 3): 10, 
    (4, 4): 1,  
    (4, 5): 10, 
    (5, 0): 1,  
    (5, 1): 1,  
    (5, 2): 4,  
    (5, 3): 1,  
    (5, 4): 1,  
    (5, 5): 1, 
    (6, 4): 1,  
    (6, 5): 4,  
    (7, 0): 1,  
    (7, 1): 1,  
    (7, 2): 10, 
    (7, 3): 1,  
    (7, 4): 1,  
    (7, 5): 1,  
    (8, 0): 4,  
    (8, 1): 1,  
    (8, 2): 1,  
    (8, 3): 4,  
    (8, 4): 4,  
    (8, 5): 1,  
    (9, 0): 1,  
    (9, 1): 1,  
    (9, 2): 10, 
    (9, 3): 1,  
    (9, 4): 1,  
    (9, 5): 1,  
    (10, 0): 1, 
    (10, 1): 1, 
    (10, 2): 1, 
    (10, 3): 1, 
    (10, 4): 10, 
    (10, 5): 1, 
    (11, 0): 4, 
    (11, 1): 1, 
    (11, 2): 10,
    (11, 3): 1, 
    (11, 4): 1, 
    (11, 5): 1, 
}

recompensas = {
    (1, 1): 10,
    (4, 5): 5,
    (10, 12): 10,
    (9, 5): 10,
    (5, 3): 5, 
    (11, 4): 5,
    (2, 3): 5 ,
}

def carregar_dados():
    return grafo, recompensas, custos