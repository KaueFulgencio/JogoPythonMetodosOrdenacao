import pygame
import sys
from queue import PriorityQueue
from busca import carregar_grafo  

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
BG_COLOR = (255, 255, 255)
AGENT_COLOR = (255, 0, 0)
BLOCK_SIZE = 50
SLEEP_TIME = 1000

#só aceita valor inteiro vindo do input
try:
    inicio_x = int(sys.argv[1])
    inicio_y = int(sys.argv[2])
    objetivo_x = int(sys.argv[3])
    objetivo_y = int(sys.argv[4])
except ValueError:
    print("Erro: Os valores de início e objetivo devem ser números inteiros válidos.")
    sys.exit(1)

pygame.init()

def fechar_busca_gulosa():
    pygame.quit()
    sys.exit()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Busca Gulosa")

grafo = carregar_grafo("grafo.py")  

#inicio = (5, 5)
#objetivo = (10, 10)

def calcular_heuristica(ponto, objetivo):
    x1, y1 = ponto
    x2, y2 = objetivo
    return abs(x1 - x2) + abs(y1 - y2)

def busca_gulosa(screen, grafo, inicio, objetivo):
    fila_prioridade = PriorityQueue()
    fila_prioridade.put((0, inicio))
    visitados = set()
    posicao = {inicio: inicio}

    while not fila_prioridade.empty():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fechar_busca_gulosa()

        _, vertice = fila_prioridade.get()

        if vertice in visitados:
            continue

        visitados.add(vertice)
        x, y = vertice
        pygame.draw.circle(screen, AGENT_COLOR, (x * BLOCK_SIZE + BLOCK_SIZE // 2, y * BLOCK_SIZE + BLOCK_SIZE // 2), BLOCK_SIZE // 2)
        pygame.display.update()
        pygame.time.delay(SLEEP_TIME)

        print(f"Posição: ({x}, {y})")

        if vertice == objetivo:
            return reconstruir_caminho(posicao, inicio, objetivo)

        for vizinho in grafo[vertice]['conexoes']:
            if vizinho not in visitados:
                prioridade = calcular_heuristica(vizinho, objetivo)
                fila_prioridade.put((prioridade, vizinho))
                posicao[vizinho] = vertice

    return None

def reconstruir_caminho(posicao, inicio, objetivo):
    caminho = [objetivo]
    atual = objetivo
    while atual != inicio:
        atual = posicao[atual]
        caminho.append(atual)
    caminho.reverse()
    return caminho

caminho = busca_gulosa(screen, grafo, (inicio_x, inicio_y), (objetivo_x, objetivo_y))
if caminho:
    print("Caminho encontrado:", caminho)
else:
    print("Caminho não encontrado.")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fechar_busca_gulosa()
