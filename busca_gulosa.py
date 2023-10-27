import pygame
import sys
from queue import PriorityQueue
from busca import carregar_grafo  

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
BG_COLOR = (255, 255, 255)
AGENT_COLOR = (255, 0, 0)
BLOCK_SIZE = 40
SLEEP_TIME = 1000
TERRENO_CORES = {
    'solida': (139, 69, 19),
    'arenosa': (255, 255, 0),
    'rochosa': (192, 192, 192),
    'pantano': (0, 128, 0),
    'premio': (255, 0, 0),
    'recompensa': (0, 0, 255)
}

# Só aceita valor inteiro vindo do input
try:
    inicio_x = int(sys.argv[1])
    inicio_y = int(sys.argv[2])
    objetivo_x = int(sys.argv[3])
    objetivo_y = int(sys.argv[4])
except ValueError:
    print("Erro: Os valores de início e objetivo devem ser números inteiros.")
    sys.exit(1)

pygame.init()

def fechar_busca_gulosa():
    pygame.quit()
    sys.exit()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Busca Gulosa")

grafo = carregar_grafo("grafo.py")

def draw_environment(grafo):
    screen.fill(BG_COLOR)
    for pos, data in grafo.items():
        x, y = pos
        terreno = data['terreno']
        cor = TERRENO_CORES.get(terreno, (255, 255, 255))
        pygame.draw.rect(screen, cor, (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE), 0)
        pygame.draw.rect(screen, (0, 0, 0), (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE), 1)
        for neighbor in data['conexoes']:
            pygame.draw.line(screen, (0, 0, 0), (x * BLOCK_SIZE, y * BLOCK_SIZE), (neighbor[0] * BLOCK_SIZE, neighbor[1] * BLOCK_SIZE))

draw_environment(grafo) 
pygame.display.update()

def calcular_heuristica(ponto, objetivo):
    x1, y1 = ponto
    x2, y2 = objetivo
    return abs(x1 - x2) + abs(y1 - y2)

def buscar_gulosa(screen, grafo, inicio, objetivo):
    fila_prioridade = PriorityQueue()
    fila_prioridade.put((0, inicio, 0))  
    visitados = set()
    posicao = {inicio: inicio}

    while not fila_prioridade.empty():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fechar_busca_gulosa()

        _, vertice, custo_acumulado = fila_prioridade.get() 

        if vertice in visitados:
            continue

        visitados.add(vertice)
        x, y = vertice
        pygame.draw.circle(screen, AGENT_COLOR, (x * BLOCK_SIZE + BLOCK_SIZE // 2, y * BLOCK_SIZE + BLOCK_SIZE // 2), BLOCK_SIZE // 2)
        pygame.display.update()
        pygame.time.delay(SLEEP_TIME)

        print(f"Posição: ({x}, {y}), Custo Acumulado: {custo_acumulado}")

        if vertice == objetivo:
            caminho, custo_total = reconstruir_caminho(posicao, inicio, objetivo, custo_acumulado)
            return caminho, custo_total  

        for vizinho in grafo[vertice]['conexoes']:
            if vizinho not in visitados:
                prioridade = calcular_heuristica(vizinho, objetivo)
                novo_custo_acumulado = custo_acumulado + calcular_custo(vertice, vizinho)
                fila_prioridade.put((prioridade, vizinho, novo_custo_acumulado))
                posicao[vizinho] = vertice

    return None, 0  

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

def reconstruir_caminho(posicao, inicio, objetivo, custo_acumulado):
    caminho = [objetivo]
    custo_total = custo_acumulado 
    atual = objetivo
    while atual != inicio:
        anterior = posicao[atual]
        custo_total += calcular_custo(anterior, atual)  
        caminho.append(anterior)
        atual = anterior
    caminho.reverse()
    return caminho, custo_total

caminho, custo_total = buscar_gulosa(screen, grafo, (inicio_x, inicio_y), (objetivo_x, objetivo_y))
if caminho:
    print("Caminho encontrado:", caminho)
    print("Custo total da rota:", custo_total)
else:
    print("Caminho não encontrado.")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fechar_busca_gulosa()
