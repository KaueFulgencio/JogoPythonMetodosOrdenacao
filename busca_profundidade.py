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
def draw_environment(ambiente, recompensas):
    screen.fill(BG_COLOR)
    for y, row in enumerate(ambiente):
        for x, cell in enumerate(row):
            pygame.draw.rect(screen, (0, 0, 0), (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE), 1)
            if cell == ' ':
                pygame.draw.rect(screen, (0, 255, 0), (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))  # Terreno caminhável
            elif cell == '$':
                pygame.draw.rect(screen, (255, 255, 0), (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))  # Recompensa
            elif cell == '▓':
                pygame.draw.rect(screen, (0, 0, 0), (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))  # Parede
    pygame.draw.rect(screen, AGENT_COLOR, (agente[0] * BLOCK_SIZE, agente[1] * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))  # Agente
    pygame.display.update()


def carregar_grafo():
    grafo = {}
    # Carregue o grafo a partir do arquivo "grafo.py"
    try:
        exec(open("grafo.py").read())
    except FileNotFoundError:
        print("Arquivo 'grafo.py' não encontrado.")
    return grafo

# Função para a busca em profundidade
def busca_profundidade(ambiente, agente, objetivo, visitados, recompensas):
    x, y = agente
    if agente == objetivo:
        return True

    visitados.add(agente)
    draw_environment(ambiente, recompensas)
    pygame.time.delay(SLEEP_TIME)

    if ambiente[y][x] == '$':
        recompensa = recompensas.get((x, y), 0)
        print(f"Posição: ({x}, {y}), Recompensa: {recompensa}")

    for dx, dy in [(0, -1), (1, 0), (0, 1), (-1, 0)]:
        novo_x, novo_y = x + dx, y + dy
        if 0 <= novo_x < len(ambiente[0]) and 0 <= novo_y < len(ambiente) and (novo_x, novo_y) not in visitados and ambiente[novo_y][novo_x] != '▓':
            if busca_profundidade(ambiente, (novo_x, novo_y), objetivo, visitados, recompensas):
                return True

    return False

# Carregue o ambiente a partir de "ambiente.txt"
try:
    ambiente = [list(row) for row in open("ambiente.txt").read().splitlines()]
    agente = (1, 1)  # Ponto de partida
    objetivo = (9, 4)  # Objetivo
    recompensas = {
        (5, 1): 10,  # Exemplo de recompensa na posição (5, 1)
        (7, 1): 5,   # Exemplo de recompensa na posição (7, 1)
        (3, 3): 2    # Exemplo de recompensa na posição (3, 3)
    }
    visitados = set()

    draw_environment(ambiente, recompensas)

    if busca_profundidade(ambiente, agente, objetivo, visitados, recompensas):
        print("Caminho encontrado!")
    else:
        print("Caminho não encontrado.")
except FileNotFoundError:
    print("Arquivo 'ambiente.txt' não encontrado.")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
sys.exit()
