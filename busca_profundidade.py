import pygame
import sys

# Defina o tamanho da tela e outras constantes
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
BG_COLOR = (255, 255, 255)
AGENT_COLOR = (255, 0, 0)
BLOCK_SIZE = 20
SLEEP_TIME = 100

# Crie um grafo para a busca em profundidade
# Substitua esta definição de grafo pelo seu grafo personalizado
grafo = {
    (0, 0): [(0, 1)],
    (0, 1): [(0, 2), (1, 1)],
    (0, 2): [(0, 3)],
    (1, 1): [(2, 1)],
    (0, 3): [(1, 3)],
    (1, 3): [(1, 4)],
    (1, 4): [(2, 4)],
    (2, 1): [(3, 1)],
    (3, 1): [(4, 1)],
    (1, 3): [(1, 5)],
    (1, 5): [(2, 5)],
    (2, 4): [(2, 5)],
    (2, 5): [(3, 5)],
    (3, 5): [(4, 5)],
    (4, 1): [(4, 2)],
    (4, 2): [(4, 3)],
    (4, 3): [(4, 4)],
    (4, 4): [(4, 5)],
    (4, 5): [],
}

pygame.init()

# Cria a tela
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Busca em Profundidade")

# Desenha o ambiente
def draw_environment():
    screen.fill(BG_COLOR)
    for pos, neighbors in grafo.items():
        x, y = pos
        pygame.draw.rect(screen, (0, 0, 0), (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE), 1)
        for neighbor in neighbors:
            pygame.draw.line(screen, (0, 0, 0), (x * BLOCK_SIZE, y * BLOCK_SIZE), (neighbor[0] * BLOCK_SIZE, neighbor[1] * BLOCK_SIZE))

# Função para a busca em profundidade
def busca_profundidade(grafo, inicio, objetivo, visitados):
    if inicio == objetivo:
        return True

    visitados.add(inicio)
    pygame.draw.rect(screen, AGENT_COLOR, (inicio[0] * BLOCK_SIZE, inicio[1] * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
    pygame.display.update()
    pygame.time.delay(SLEEP_TIME)

    for vizinho in grafo[inicio]:
        if vizinho not in visitados:
            if busca_profundidade(grafo, vizinho, objetivo, visitados):
                return True

    return False

# Ponto de partida e objetivo
inicio = (0, 0)
objetivo = (4, 5)

# Conjunto para rastrear os vértices visitados
visitados = set()

if busca_profundidade(grafo, inicio, objetivo, visitados):
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
