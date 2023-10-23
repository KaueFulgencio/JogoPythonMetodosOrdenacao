import pygame
import sys

from collections import deque
from queue import PriorityQueue

from busca import carregar_grafo, executar_busca

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
BG_COLOR = (255, 255, 255)
AGENT_COLOR = (255, 50, 100)
BLOCK_SIZE = 70
SLEEP_TIME = 100

pygame.init()

def fechar_busca_profundidade():
    pygame.quit()
    sys.exit()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Busca em Profundidade")

grafo = carregar_grafo("grafo.py")

inicio = (0,0)
objetivo = (2,2)

def draw_environment(grafo):
    screen.fill(BG_COLOR)
    for pos, neighbors in grafo.items():
        x, y = pos
        pygame.draw.rect(screen, (0, 0, 0), (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE), 1)
        for neighbor in neighbors:
            pygame.draw.line(screen, (0, 0, 0), (x * BLOCK_SIZE, y * BLOCK_SIZE), (neighbor[0] * BLOCK_SIZE, neighbor[1] * BLOCK_SIZE))


def busca_profundidade(screen, grafo, inicio, objetivo, visitados=None):
    if visitados is None:
        visitados = set()

    visitados.add(inicio)
    pygame.draw.rect(screen, AGENT_COLOR, (inicio[0] * BLOCK_SIZE, inicio[1] * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
    pygame.display.update()
    pygame.time.delay(SLEEP_TIME)

    print(f"Posição: {inicio}")

    if inicio == objetivo:
        return True

    for vizinho in grafo[inicio]:
        if vizinho not in visitados:
            if busca_profundidade(screen, grafo, vizinho, objetivo, visitados):
                return True

    return False


if busca_profundidade(screen, grafo, inicio, objetivo):
    print("Caminho encontrado!")
else:
    print("Caminho não encontrado.")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fechar_busca_profundidade()