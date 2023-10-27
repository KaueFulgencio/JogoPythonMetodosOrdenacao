import pygame
import sys
from collections import deque
from grafo import grafo, recompensas, custos

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
BG_COLOR = (255, 255, 255)
AGENT_COLOR = (0, 0, 0)
BLOCK_SIZE = 40
SLEEP_TIME = 1000
TERRENO_CORES = {
    'solida': (139, 69, 19),
    'arenosa': (255, 255, 0),
    'rochosa': (192, 192, 192),
    'pantano': (0, 128, 0),
    'recompensa': (255, 165, 0)
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
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Busca em Largura")

def fechar_busca_largura():
    pygame.quit()
    sys.exit()

def desenha_mapa(grafo, recompensas):
    screen.fill(BG_COLOR)
    for pos, data in grafo.items():
        x, y = pos
        terreno = data['terreno']
        cor = TERRENO_CORES.get(terreno, (255, 255, 255))
        if pos in recompensas:
            cor = TERRENO_CORES['recompensa']  # Usar a cor laranja para as recompensas
        pygame.draw.rect(screen, cor, (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE), 0)
        pygame.draw.rect(screen, (0, 0, 0), (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE), 1)
        for neighbor in data['conexoes']:
            pygame.draw.line(screen, (0, 0, 0), (x * BLOCK_SIZE, y * BLOCK_SIZE), (neighbor[0] * BLOCK_SIZE, neighbor[1] * BLOCK_SIZE))

def busca_largura(screen, grafo, inicio, objetivo, custos, recompensas):
    fila = deque()
    visitados = set()
    custo = {inicio: 0}
    posicao = {inicio: inicio}
    custo_total = 0
    recompensa_total = 0  

    fila.append(inicio)
    visitados.add(inicio)

    while fila:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fechar_busca_largura()

        vertice = fila.popleft()

        x, y = vertice
        pygame.draw.circle(screen, AGENT_COLOR, (x * BLOCK_SIZE + BLOCK_SIZE // 2, y * BLOCK_SIZE + BLOCK_SIZE // 2), BLOCK_SIZE // 2)
        pygame.display.update()
        pygame.time.delay(SLEEP_TIME)

        print(f"Posição: ({x}, {y}), Custo: {custo[vertice]}, Recompensa: {recompensa_total}")

        if vertice == objetivo:
            caminho = reconstruir_caminho(posicao, objetivo)
            print("Caminho percorrido:", caminho)
            print("Preço final do percurso (custo):", custo_total)
            print("Recompensa total:", recompensa_total)
            return True

        for vizinho in grafo[vertice]['conexoes']:
            if vizinho not in visitados:
                fila.append(vizinho)
                visitados.add(vizinho)
                custo_vizinho = calcular_custo(vertice, vizinho)
                custo[vizinho] = custo[vertice] + custo_vizinho
                custo_total += custo_vizinho
                recompensa_vizinho = recompensas.get(vizinho, 0)  
                recompensa_total += recompensa_vizinho  
                posicao[vizinho] = vertice

    return False

def reconstruir_caminho(posicao, objetivo):
    caminho = [objetivo]
    while objetivo in posicao:
        objetivo = posicao[objetivo]
        caminho.insert(0, objetivo)
    return caminho

def calcular_custo(posicao_atual, posicao_vizinha):
    terreno_atual = grafo[posicao_atual]['terreno']
    terreno_vizinho = grafo[posicao_vizinha]['terreno']
    
    custos = {
        'solida': 1,
        'rochosa': 10,
        'arenosa': 4,
        'pantano': 20
    }

    custo_atual = custos.get(terreno_atual, 1)
    custo_vizinho = custos.get(terreno_vizinho, 1)

    return max(custo_atual, custo_vizinho)


def calcular_custo_terreno(terreno_atual, terreno_vizinho):
    custos = {
        ('solida', 'solida'): 1,
        ('solida', 'rochosa'): 10,
        ('solida', 'arenosa'): 4,
        ('solida', 'pantano'): 20,
        ('rochosa', 'rochosa'): 10,
        ('arenosa', 'arenosa'): 4,
        ('pantano', 'pantano'): 20
    }
    return custos.get((terreno_atual, terreno_vizinho), 1)

def carregar_dados():
    return grafo, recompensas, custos

grafo, recompensas, custos = carregar_dados()
desenha_mapa(grafo, recompensas)  
pygame.display.update()

if busca_largura(screen, grafo, (inicio_x, inicio_y), (objetivo_x, objetivo_y), custos, recompensas):
    print("Caminho encontrado!")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fechar_busca_largura()
