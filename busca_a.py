import pygame
import sys
from queue import PriorityQueue

# Defina o tamanho da tela e outras constantes
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
BG_COLOR = (255, 255, 255)
AGENT_COLOR = (255, 0, 0)
BLOCK_SIZE = 20
SLEEP_TIME = 100

pygame.init()

# Crie a tela
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Busca A*")

# Carregue o grafo a partir de "grafo.py"
def carregar_grafo():
    grafo = {}
    # Carregue o grafo a partir do arquivo "grafo.py"
    try:
        exec(open("grafo.py").read())
    except FileNotFoundError:
        print("Arquivo 'grafo.py' não encontrado.")
    return grafo

grafo = {
    (0, 0): [(0, 1), (1, 0)],
    (0, 1): [(0, 0), (1, 1)],
    (0, 2): [(0, 3)],
    (1, 0): [(0, 0), (1, 1), (2, 0)],
    (1, 1): [(0, 1), (2, 1)],
    (1, 2): [(2, 2)],
    (2, 0): [(1, 0)],
    (2, 1): [(1, 1), (2, 2)],
    (2, 2): [(1, 2), (2, 1)],
    (3, 3): [(4, 3)],
    (4, 3): [(3, 3), (5, 3)],
    (5, 3): [(4, 3)],
    (6, 6): [(6, 7)],
    (6, 7): [(6, 6), (7, 7)],
    (7, 7): [(6, 7), (8, 7)],
    (8, 7): [(7, 7), (8, 8)],
    (8, 8): [(8, 7)],
    (9, 9): [(9, 10)],
    (9, 10): [(9, 9), (10, 10)],
    (10, 10): [(9, 10), (10, 11)],
    (10, 11): [(10, 10), (10, 12)],
    (10, 12): [(10, 11)],
}

recompensas = {
    (1, 1): 10,
    (4, 3): 5,
    (10, 11): 8,
}

# Desenhe o ambiente
def draw_environment():
    screen.fill(BG_COLOR)
    for pos, neighbors in grafo.items():
        x, y = pos
        pygame.draw.rect(screen, (0, 0, 0), (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE), 1)
        for neighbor in neighbors:
            pygame.draw.line(screen, (0, 0, 0), (x * BLOCK_SIZE, y * BLOCK_SIZE), (neighbor[0] * BLOCK_SIZE, neighbor[1] * BLOCK_SIZE))
    for recompensa, valor in recompensas.items():
        x, y = recompensa
        pygame.draw.rect(screen, (255, 255, 0), (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
        font = pygame.font.Font(None, 36)
        recompensa_text = font.render(str(valor), True, (0, 0, 0))
        screen.blit(recompensa_text, (x * BLOCK_SIZE + BLOCK_SIZE // 3, y * BLOCK_SIZE + BLOCK_SIZE // 3))

# Função para calcular a heurística (distância) entre dois pontos
def calcular_heuristica(ponto, objetivo):
    x1, y1 = ponto
    x2, y2 = objetivo
    return abs(x1 - x2) + abs(y1 - y2)

# Função para a busca A*
def busca_a_estrela(grafo, inicio, objetivo, recompensas):
    fila_prioridade = PriorityQueue()
    fila_prioridade.put((0, inicio))
    visitados = set()
    custo = {}  # Dicionário para rastrear o custo de cada posição
    posicao = {}  # Dicionário para rastrear a posição do agente

    custo[inicio] = 0
    posicao[inicio] = inicio

    while not fila_prioridade.empty():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        _, vertice = fila_prioridade.get()

        if vertice in visitados:
            continue

        visitados.add(vertice)
        pygame.draw.rect(screen, AGENT_COLOR, (vertice[0] * BLOCK_SIZE, vertice[1] * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
        pygame.display.update()
        pygame.time.delay(SLEEP_TIME)

        print(f"Posição: {vertice}, Custo: {custo[vertice]}")  # Imprime a posição e o custo
        if vertice in recompensas:
            print(f"Recompensa: {recompensas[vertice]}")  # Exibe a recompensa, se existir

        if vertice == objetivo:
            return True

        for vizinho in grafo[vertice]:
            if vizinho not in visitados:
                novo_custo = custo[vertice] + calcular_custo(vertice, vizinho)
                if vizinho not in custo or novo_custo < custo[vizinho]:
                    custo[vizinho] = novo_custo
                    prioridade = novo_custo + calcular_heuristica(vizinho, objetivo)
                    fila_prioridade.put((prioridade, vizinho))
                    posicao[vizinho] = vertice

    return False

# Função para calcular o custo com base no tipo de terreno
def calcular_custo(posicao_atual, posicao_vizinha):
    # Implemente a lógica para verificar o tipo de terreno e atribuir o custo correspondente
    return 1  # Custo padrão

# Ponto de partida e objetivo
inicio = (0, 0)
objetivo = (4, 5)

draw_environment()

if busca_a_estrela(grafo, inicio, objetivo, recompensas):
    print("Caminho encontrado!")
else:
    print("Caminho não encontrado.")

# Mantém a janela aberta até o usuário fechar
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
sys.exit()
