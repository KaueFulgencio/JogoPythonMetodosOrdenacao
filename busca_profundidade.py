import pygame
import sys

# Defina o tamanho da tela e outras constantes
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
BG_COLOR = (255, 255, 255)
AGENT_COLOR = (255, 0, 0)
BLOCK_SIZE = 20
SLEEP_TIME = 100

pygame.init()

# Cria a tela
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Busca em Profundidade")

# Função para exibir o ambiente
def draw_environment(grafo):
    screen.fill(BG_COLOR)
    for pos, neighbors in grafo.items():
        x, y = pos
        pygame.draw.rect(screen, (0, 0, 0), (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE), 1)
        for neighbor in neighbors:
            pygame.draw.line(screen, (0, 0, 0), (x * BLOCK_SIZE, y * BLOCK_SIZE), (neighbor[0] * BLOCK_SIZE, neighbor[1] * BLOCK_SIZE))

# Função para a busca em profundidade
def busca_profundidade(grafo, inicio, objetivo, visitados, recompensas):
    if inicio == objetivo:
        return True

    visitados.add(inicio)
    pygame.draw.rect(screen, AGENT_COLOR, (inicio[0] * BLOCK_SIZE, inicio[1] * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
    pygame.display.update()
    pygame.time.delay(SLEEP_TIME)

    if inicio in recompensas:
        recompensa = recompensas[inicio]
        print(f"Posição: {inicio}, Recompensa: {recompensa}")

    for vizinho in grafo[inicio]:
        if vizinho not in visitados:
            if busca_profundidade(grafo, vizinho, objetivo, visitados, recompensas):
                return True

    return False

# Ponto de partida e objetivo
inicio = (0, 0)
objetivo = (4, 5)

# Carregue o grafo a partir de "grafo.py"
try:
    grafo = {}
    exec(open("grafo.py").read())
except FileNotFoundError:
    print("Arquivo 'grafo.py' não encontrado.")
    sys.exit()

# Conjunto para rastrear os vértices visitados
visitados = set()

# Dicionário para rastrear as recompensas nas posições
recompensas = {
    (1, 1): 10,  # Exemplo de recompensa na posição (1, 1)
    (3, 3): 5,   # Exemplo de recompensa na posição (3, 3)
    # Adicione mais recompensas conforme necessário
}

draw_environment(grafo)

if busca_profundidade(grafo, inicio, objetivo, visitados, recompensas):
    print("Caminho encontrado!")
else:
    print("Caminho não encontrado.")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
sys.exit()
