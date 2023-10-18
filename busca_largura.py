import pygame
import sys
from collections import deque

# Defina o tamanho da tela e outras constantes
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
BG_COLOR = (255, 255, 255)
AGENT_COLOR = (255, 255, 0)
BLOCK_SIZE = 20
SLEEP_TIME = 100

pygame.init()

def fechar_busca_largura():
    pygame.quit()
    sys.exit()

# Cria a tela
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Busca em Largura")

def carregar_grafo():
    grafo = {}
    # Carregue o grafo a partir do arquivo "grafo.py"
    try:
        exec(open("grafo.py").read())
    except FileNotFoundError:
        print("Arquivo 'grafo.py' não encontrado.")
    return grafo


# Função para desenhar o ambiente
def draw_environment(grafo):
    screen.fill(BG_COLOR)
    for pos, neighbors in grafo.items():
        x, y = pos
        pygame.draw.rect(screen, (0, 0, 0), (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE), 1)
        for neighbor in neighbors:
            pygame.draw.line(screen, (0, 0, 0), (x * BLOCK_SIZE, y * BLOCK_SIZE), (neighbor[0] * BLOCK_SIZE, neighbor[1] * BLOCK_SIZE))

# Função para a busca em largura
def busca_largura(grafo, inicio, objetivo):
    fila = deque()
    visitados = set()
    custo = {inicio: 0}  # Dicionário para rastrear o custo de cada posição
    posicao = {inicio: inicio}  # Dicionário para rastrear a posição do agente

    fila.append(inicio)
    visitados.add(inicio)

    while fila:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fechar_busca_largura()

        vertice = fila.popleft()
        pygame.draw.rect(screen, AGENT_COLOR, (vertice[0] * BLOCK_SIZE, vertice[1] * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
        pygame.display.update()
        pygame.time.delay(SLEEP_TIME)

        print(f"Posição: {vertice}, Custo: {custo[vertice]}")  # Imprime a posição e o custo

        if vertice == objetivo:
            return True

        for vizinho in grafo[vertice]:
            if vizinho not in visitados:
                fila.append(vizinho)
                visitados.add(vizinho)
                custo[vizinho] = custo[vertice] + calcular_custo(vertice, vizinho)  # Atualiza o custo
                posicao[vizinho] = vertice  # Atualiza a posição

    return False

# Função para calcular o custo com base no tipo de terreno (a ser implementada)
def calcular_custo(posicao_atual, posicao_vizinha):
    return 1

# Carregar o grafo a partir do arquivo "grafo.py"
try:
    grafo = {}
    exec(open("grafo.py").read())
except FileNotFoundError:
    print("Arquivo 'grafo.py' não encontrado.")
    sys.exit()

# Ponto de partida e objetivo
inicio = (0, 0)
objetivo = (4, 5)

if busca_largura(grafo, inicio, objetivo):
    print("Caminho encontrado!")

# Mantém a janela aberta até o usuário fechar
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fechar_busca_largura()
