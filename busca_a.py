import pygame
import sys
from queue import PriorityQueue
from grafo import grafo, custos, recompensas  

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
BG_COLOR = (255, 255, 255)
AGENT_COLOR = (155, 0, 100)
BLOCK_SIZE = 40
AGENT_RADIUS = BLOCK_SIZE // 2
SLEEP_TIME = 1000
TERRENO_CORES = {
    'solida': (139, 69, 19),
    'arenosa': (255, 255, 0),
    'rochosa': (192, 192, 192),
    'pantano': (0, 128, 0),
    'recompensa': (255, 165, 0)
}

# Aceita apenas valores inteiros como entrada
try:
    inicio_x = int(sys.argv[1])
    inicio_y = int(sys.argv[2])
    objetivo_x = int(sys.argv[3])
    objetivo_y = int(sys.argv[4])
except ValueError:
    print("Erro: Os valores de início e objetivo devem ser números inteiros.")
    sys.exit(1)

pygame.init()

def fechar_busca_a():
    pygame.quit()
    sys.exit()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Busca A*")

def desenha_mapa(grafo, recompensas):
    screen.fill(BG_COLOR)
    for pos, data in grafo.items():
        x, y = pos
        terreno = data['terreno']
        cor = TERRENO_CORES.get(terreno, (255, 255, 255))
        if pos in recompensas:
            cor = TERRENO_CORES['recompensa']  
        pygame.draw.rect(screen, cor, (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE), 0)
        pygame.draw.rect(screen, (0, 0, 0), (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE), 1)
        for neighbor in data['conexoes']:
            pygame.draw.line(screen, (0, 0, 0), (x * BLOCK_SIZE, y * BLOCK_SIZE), (neighbor[0] * BLOCK_SIZE, neighbor[1] * BLOCK_SIZE))

desenha_mapa(grafo, recompensas) 
pygame.display.update()

def calcular_heuristica(ponto, objetivo):
    x1, y1 = ponto
    x2, y2 = objetivo
    return abs(x1 - x2) + abs(y1 - y2)

def busca_a(screen, grafo, inicio, objetivo, custos, recompensas):
    fila_prioridade = PriorityQueue()
    fila_prioridade.put((0, inicio))
    visitados = set()
    custo = {}
    posicao = {}
    custo_acumulado = {}

    custo[inicio] = 0
    posicao[inicio] = inicio
    custo_acumulado[inicio] = 0

    while not fila_prioridade.empty():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fechar_busca_a()

        _, vertice = fila_prioridade.get()

        if vertice in visitados:
            continue

        visitados.add(vertice)
        x, y = vertice
        x_center, y_center = x * BLOCK_SIZE + BLOCK_SIZE // 2, y * BLOCK_SIZE + BLOCK_SIZE // 2
        pygame.draw.circle(screen, AGENT_COLOR, (x_center, y_center), AGENT_RADIUS)
        pygame.display.update()
        pygame.time.delay(SLEEP_TIME)

        print(f"Posição: {vertice}, Custo Acumulado: {custo_acumulado[vertice]}")

        if vertice == objetivo:
            return True

        for vizinho in grafo[vertice]['conexoes']:
            if vizinho in grafo:
                if vizinho not in visitados:
                    novo_custo = custo[vertice] + calcular_custo(vertice, vizinho)
                    if vizinho in recompensas:
                        recompensa = recompensas[vizinho]
                    else:
                        recompensa = 0
                    custo_com_recompensa = novo_custo + recompensa
                    if vizinho not in custo or custo_com_recompensa < custo[vizinho]:
                        custo[vizinho] = custo_com_recompensa
                        prioridade = custo_com_recompensa + calcular_heuristica(vizinho, objetivo)
                        fila_prioridade.put((prioridade, vizinho))
                        posicao[vizinho] = vertice
                        custo_acumulado[vizinho] = custo_acumulado[vertice] + novo_custo

    return False

def calcular_custo(posicao_atual, posicao_vizinha):
    terreno_atual = grafo[posicao_atual]['terreno']
    terreno_vizinho = grafo[posicao_vizinha]['terreno']
    
    custos = {
        'solida': 1,
        'rochosa': 10,
        'arenosa': 4,
        'pantano': 20
    }

    custo_atual = custos.get(terreno_atual, 1)
    custo_vizinho = custos.get(terreno_vizinho, 1)

    return max(custo_atual, custo_vizinho)
def calcular_custo_terreno(terreno_atual, terreno_vizinho):
    custos = {
        ('solida', 'solida'): 1,
        ('solida', 'rochosa'): 10,
        ('solida', 'arenosa'): 4,
        ('solida', 'pantano'): 20,
        ('rochosa', 'rochosa'): 10,
        ('arenosa', 'arenosa'): 4,
        ('pantano', 'pantano'): 20
    }
    return custos.get((terreno_atual, terreno_vizinho), 1)

for posicao, recompensa in recompensas.items():
    print(f"Recompensa em {posicao}: {recompensa}")

if busca_a(screen, grafo, (inicio_x, inicio_y), (objetivo_x, objetivo_y), custos, recompensas):
    print("Caminho encontrado!")
else:
    print("Caminho não encontrado.")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fechar_busca_a()
