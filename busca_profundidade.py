import pygame
import sys
from collections import deque
from busca import carregar_grafo, executar_busca

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
BG_COLOR = (255, 255, 255)
AGENT_COLOR = (255, 50, 100)
BLOCK_SIZE = 50
SLEEP_TIME = 1000
#Dicionario dos terrenos
TERRENO_CORES = {
    'solida': (139, 69, 19),
    'arenosa': (255, 255, 0),
    'rochosa': (192, 192, 192),
    'pantano': (0, 128, 0),
    'premio': (255, 0, 0),
    'recompensa': (0, 0, 255)
}
try:
    inicio_x = int(sys.argv[1])
    inicio_y = int(sys.argv[2])
    objetivo_x = int(sys.argv[3])
    objetivo_y = int(sys.argv[4])
except ValueError:
    print("Erro: Os valores de início e objetivo devem ser números inteiros válidos.")
    sys.exit(1)

pygame.init()

def fechar_busca_profundidade():
    pygame.quit()
    sys.exit()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Busca em Profundidade")

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

print(grafo)

def busca_profundidade(screen, grafo, inicio, objetivo, visitados=None, custo=0):
    if visitados is None:
        visitados = set()

    visitados.add(inicio)
    pygame.draw.rect(screen, AGENT_COLOR, (inicio[0] * BLOCK_SIZE, inicio[1] * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
    pygame.display.update()
    pygame.time.delay(SLEEP_TIME)

    print(f"Posição: {inicio}, Custo: {custo}")

    if inicio == objetivo:
        return True

    for vizinho in grafo[inicio]['conexoes']:
        if vizinho not in visitados:
            if busca_profundidade(screen, grafo, vizinho, objetivo, visitados, custo + calcular_custo(inicio, vizinho)):
                return True

    return False

def calcular_custo(posicao_atual, posicao_vizinha):
    return 1  

if busca_profundidade(screen, grafo, (inicio_x, inicio_y), (objetivo_x, objetivo_y)):
    print("Caminho encontrado!")
else:
    print("Caminho não encontrado.")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fechar_busca_profundidade()
