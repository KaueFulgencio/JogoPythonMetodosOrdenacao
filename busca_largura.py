import pygame
import sys
from collections import deque
from busca import carregar_grafo, executar_busca

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
BG_COLOR = (255, 255, 255)
AGENT_COLOR = (255, 255, 0)
BLOCK_SIZE = 70
SLEEP_TIME = 100

TERRENO_CORES = {
    'solida': (139, 69, 19),  
    'arenosa': (255, 255, 0),  
    'rochosa': (192, 192, 192),  
    'pantano': (0, 128, 0),  
    'premio': (255, 0, 0),  
    'recompensa': (0, 0, 255)  
}

pygame.init()

def fechar_busca_largura():
    pygame.quit()
    sys.exit()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Busca em Largura")

grafo = carregar_grafo("grafo.py")

inicio = (0, 2)
objetivo = (4, 5)

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


def busca_largura(screen, grafo, inicio, objetivo):
    fila = deque()
    visitados = set()
    custo = {inicio: 0}
    posicao = {inicio: inicio}

    fila.append(inicio)
    visitados.add(inicio)

    while fila:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fechar_busca_largura()

        vertice = fila.popleft()
        
        x, y = vertice 
        pygame.draw.circle(screen, AGENT_COLOR, (x * BLOCK_SIZE + BLOCK_SIZE // 2, y * BLOCK_SIZE + BLOCK_SIZE // 2), BLOCK_SIZE // 2)
        pygame.display.update()
        pygame.time.delay(SLEEP_TIME)

        print(f"Posição: ({x}, {y}), Custo: {custo[vertice]}")

        if vertice == objetivo:
            return True

        for vizinho in grafo[vertice]['conexoes']:
            if vizinho not in visitados:
                fila.append(vizinho)
                visitados.add(vizinho)
                custo[vizinho] = custo[vertice] + calcular_custo(vertice, vizinho)
                posicao[vizinho] = vertice

    return False


def calcular_custo(posicao_atual, posicao_vizinha):
    return 1

def calcular_custo_terreno(terreno_atual, terreno_vizinho):
    custos = {
        'solida': 1,  
        'rochosa': 10,
        'arenosa': 4,
        'pantano': 20
    }

    custo_atual = custos.get(terreno_atual, 1)
    custo_vizinho = custos.get(terreno_vizinho, 1)

    return max(custo_atual, custo_vizinho)

if busca_largura(screen, grafo, inicio, objetivo):
    print("Caminho encontrado!")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fechar_busca_largura()
