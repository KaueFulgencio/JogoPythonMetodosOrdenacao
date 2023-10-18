import pygame
import sys

# Configurações da tela
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
BG_COLOR = (255, 255, 255)
AGENT_COLOR = (255, 255, 0)
BLOCK_SIZE = 20
SLEEP_TIME = 100

# Inicialização do Pygame
pygame.init()

# Cria a tela
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Busca em Profundidade")

def carregar_grafo():
    grafo = {}
    try:
        exec(open("grafo.py").read())
    except FileNotFoundError:
        print("Arquivo 'grafo.py' não encontrado.")
    return grafo

def draw_environment(ambiente, recompensas, agente, grafo):
    screen.fill(BG_COLOR)

    # Desenha o ambiente
    for y, row in enumerate(ambiente):
        for x, cell in enumerate(row):
            pygame.draw.rect(screen, (0, 0, 0), (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE), 1)
            if cell == ' ':
                pygame.draw.rect(screen, (0, 255, 0), (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))  # Terreno caminhável
            elif cell == '$':
                pygame.draw.rect(screen, (255, 255, 0), (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))  # Recompensa
            elif cell == '▓':
                pygame.draw.rect(screen, (0, 0, 0), (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))  # Parede

    # Desenha o agente
    x, y = agente
    pygame.draw.rect(screen, AGENT_COLOR, (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))

    # Desenha o grafo
    for origem, conexoes in grafo.items():
        origem_x, origem_y = origem
        origem_x, origem_y = origem_x * BLOCK_SIZE, origem_y * BLOCK_SIZE
        for conexao in conexoes:
            destino_x, destino_y = conexao
            destino_x, destino_y = destino_x * BLOCK_SIZE, destino_y * BLOCK_SIZE
            pygame.draw.line(screen, (0, 0, 0), (origem_x, origem_y), (destino_x, destino_y))

    pygame.display.update()

def busca_profundidade(ambiente, agente, objetivo, visitados, recompensas, grafo):
    x, y = agente

    if agente == objetivo:
        print("Objetivo alcançado!")
        return True

    visitados.add(agente)
    draw_environment(ambiente, recompensas, agente, grafo)
    pygame.time.delay(SLEEP_TIME)

    if ambiente[y][x] == '$':
        recompensa = recompensas.get((x, y), 0)
        print(f"Posição: ({x}, {y}), Recompensa: {recompensa}")

    for dx, dy in [(0, -1), (1, 0), (0, 1), (-1, 0)]:
        novo_x, novo_y = x + dx, y + dy
        if 0 <= novo_x < len(ambiente[0]) and 0 <= novo_y < len(ambiente) and (novo_x, novo_y) not in visitados and ambiente[novo_y][novo_x] != '▓':
            if busca_profundidade(ambiente, (novo_x, novo_y), objetivo, visitados, recompensas, grafo):
                return True

    print("Objetivo não alcançado.")
    return False

def main():
    try:
        ambiente = [list(row) for row in open("ambiente.txt").read().splitlines()]
        agente = (1, 1)  # Ponto de partida
        objetivo = (9, 4)  # Objetivo
        recompensas = {
            (5, 1): 10,
            (7, 1): 5,
            (3, 3): 2
        }
        visitados = set()

        grafo = carregar_grafo()
        draw_environment(ambiente, recompensas, agente, grafo)

        if busca_profundidade(ambiente, agente, objetivo, visitados, recompensas, grafo):
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

if __name__ == "__main__":
    main()
