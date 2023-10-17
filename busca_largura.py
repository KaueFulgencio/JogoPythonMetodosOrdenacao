import pygame
import sys
from collections import deque

# Defina o tamanho da tela e outras constantes
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
BG_COLOR = (255, 255, 255)
AGENT_COLOR = (255, 0, 0)
BLOCK_SIZE = 20
SLEEP_TIME = 100  

#custo dos terrenos
CUSTO_SOLIDO = 1
CUSTO_ROCHOSO = 10
CUSTO_ARENSOSO = 4
CUSTO_PANTANO = 20

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

def fechar_busca_largura():
    pygame.quit()

# Cria a tela
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Busca em Largura")

# Desenha o ambiente
def draw_environment():
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
    custo = {}  # Dicionário para rastrear o custo de cada posição
    posicao = {}  # Dicionário para rastrear a posição do agente

    fila.append(inicio)
    visitados.add(inicio)
    custo[inicio] = 0
    posicao[inicio] = inicio

    while fila:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

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
                posicao[vizinho] = vizinho  # Atualiza a posição

    return False

# Função para calcular o custo com base no tipo de terreno
def calcular_custo(posicao_atual, posicao_vizinha):
    # implementar a lógica para verificar o tipo de terreno e atribuir o custo correspondente
    return CUSTO_SOLIDO

# Ponto de partida e objetivo
inicio = (0, 0)
objetivo = (4, 5)

if busca_largura(grafo, inicio, objetivo):
    print("Caminho encontrado!")
    # Após a conclusão da busca, mostra o botão "Retornar ao Menu"
    retornar_button = pygame.draw.rect(screen, (0, 0, 255), (650, 10, 140, 40))
    font = pygame.font.Font(None, 36)
    retornar_text = font.render("Menu", True, (255, 255, 255))
    screen.blit(retornar_text, (660, 20))
    pygame.display.update()
else:
    print("Caminho não encontrado.")

# Mantém a janela aberta até o usuário fechar
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if retornar_button.collidepoint(event.pos):
                fechar_busca_largura()

pygame.quit()
sys.exit()
