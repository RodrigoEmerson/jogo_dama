import pygame


# Definindo as cores
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
AZUL = (0, 0, 255)

# Inicializando o Pygame
pygame.init()

# Definindo o tamanho da tela
TAMANHO_TELA = (480, 480)
tela = pygame.display.set_mode(TAMANHO_TELA)

# Definindo o nome da janela
pygame.display.set_caption("Jogo de Damas")

# Definindo o tamanho de cada célula do tabuleiro
TAMANHO_CELULA = 60

# Definindo o tabuleiro
tabuleiro = [[0, 1, 0, 1, 0, 1, 0, 1],
             [1, 0, 1, 0, 1, 0, 1, 0],
             [0, 1, 0, 1, 0, 1, 0, 1],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [2, 0, 2, 0, 2, 0, 2, 0],
             [0, 2, 0, 2, 0, 2, 0, 2],
             [2, 0, 2, 0, 2, 0, 2, 0]]


# Definindo as funções
def desenhar_tabuleiro():
    for linha in range(8):
        for coluna in range(8):
            cor = BRANCO if (linha + coluna) % 2 == 0 else PRETO
            pygame.draw.rect(tela, cor,
                             [coluna * TAMANHO_CELULA, linha * TAMANHO_CELULA, TAMANHO_CELULA, TAMANHO_CELULA])


def desenhar_pecas():
    for linha in range(8):
        for coluna in range(8):
            if tabuleiro[linha][coluna] != 0:
                cor = AZUL if tabuleiro[linha][coluna] == 1 else PRETO
                pygame.draw.circle(tela, cor, [coluna * TAMANHO_CELULA + TAMANHO_CELULA // 2,
                                               linha * TAMANHO_CELULA + TAMANHO_CELULA // 2], TAMANHO_CELULA // 2 - 5)


def mover_peca(origem, destino):
    tabuleiro[destino[0]][destino[1]] = tabuleiro[origem[0]][origem[1]]
    tabuleiro[origem[0]][origem[1]] = 0


def capturar_peca(peca):
    tabuleiro[peca[0]][peca[1]] = 0


def pode_mover_peca(jogador, origem, destino):
    if destino[0] < 0 or destino[0] > 7 or destino[1] < 0 or destino[1] > 7:
        return False

    if tabuleiro[destino[0]][destino[1]] != 0:
        return False

    if jogador == 1:
        if origem[0] - destino[0] == 1 and abs(origem[1] - destino[1]) == 1:
            return True
        elif origem[0] - destino[0] == 2 and abs(origem[1] - destino[1]) == 2 and tabuleiro[(origem[0] + destino[0]) // 2][(origem[1] + destino[1]) // 2] == 2:
            capturar_peca([(origem[0] + destino[0]) // 2, (origem[1] + destino[1]) // 2])
            return True
        else:
            return False
    else:
        if origem[0] - destino[0] == -1 and abs(origem[1] - destino[1]) == 1:
            return True
        elif origem[0] - destino[0] == -2 and abs(origem[1] - destino[1]) == 2 and tabuleiro[(origem[0] + destino[0]) // 2][(origem[1] + destino[1]) // 2] == 1:
            capturar_peca([(origem[0] + destino[0]) // 2, (origem[1] + destino[1]) // 2])
            return True
        else:
            return False


def pode_capturar(jogador, linha, coluna):
    if jogador == 1:
        if linha > 1 and coluna > 1 and tabuleiro[linha-1][coluna-1] == 2 and tabuleiro[linha-2][coluna-2] == 0:
            return True
        elif linha > 1 and coluna < 6 and tabuleiro[linha-1][coluna+1] == 2 and tabuleiro[linha-2][coluna+2] == 0:
            return True
        else:
            return False
    else:
        if linha < 6 and coluna > 1 and tabuleiro[linha+1][coluna-1] == 1 and tabuleiro[linha+2][coluna-2] == 0:
            return True
        elif linha < 6 and coluna < 6 and tabuleiro[linha+1][coluna+1] == 1 and tabuleiro[linha+2][coluna+2] == 0:
            return True
        else:
            return False


def fim_de_jogo():
    return len([peca for linha in tabuleiro for peca in linha if peca != 0]) <= 2


def pode_mover_peca(jogador, posicao_atual, posicao_nova):
    """
    Verifica se a peça do jogador pode ser movida para a posição nova.
    """
    linha_atual, coluna_atual = posicao_atual
    linha_nova, coluna_nova = posicao_nova

    # Verifica se a posição nova está dentro do tabuleiro
    if linha_nova < 0 or linha_nova > 7 or coluna_nova < 0 or coluna_nova > 7:
        return False

    # Verifica se a posição nova já contém outra peça
    if tabuleiro[linha_nova][coluna_nova] != 0:
        return False

    # Verifica se a peça pode se mover na diagonal
    if abs(coluna_nova - coluna_atual) == abs(linha_nova - linha_atual):
        if jogador == 1:
            if linha_nova < linha_atual:
                return False
        else:
            if linha_nova > linha_atual:
                return False
        return True

    return False


def pode_capturar(jogador, linha, coluna):
    """
    Verifica se a peça do jogador pode capturar alguma peça adversária na posição dada.
    """
    if jogador == 1:
        if linha > 1 and coluna > 1 and tabuleiro[linha-1][coluna-1] == 2 and tabuleiro[linha-2][coluna-2] == 0:
            return True
        elif linha > 1 and coluna < 6 and tabuleiro[linha-1][coluna+1] == 2 and tabuleiro[linha-2][coluna+2] == 0:
            return True
        else:
            if linha < 6 and coluna > 1 and tabuleiro[linha+1][coluna-1] == 1 and tabuleiro[linha+2][coluna-2] == 0:
                return True
            elif linha < 6 and coluna < 6 and tabuleiro[linha+1][coluna+1] == 1 and tabuleiro[linha+2][coluna+2] == 0:
                return True

    return False


jogador_atual = 1
peca_selecionada = None


while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            quit()

        elif evento.type == pygame.MOUSEBUTTONDOWN:
            posicao_mouse = pygame.mouse.get_pos()
            linha = posicao_mouse[1] // TAMANHO_CELULA
            coluna = posicao_mouse[0] // TAMANHO_CELULA
            
            if peca_selecionada == None:
                if tabuleiro[linha][coluna] != 0 and tabuleiro[linha][coluna] == jogador_atual:
                    peca_selecionada = (linha, coluna)
            else:
                if pode_mover_peca(jogador_atual, peca_selecionada, (linha, coluna)):
                    tabuleiro[linha][coluna] = jogador_atual
                    tabuleiro[peca_selecionada[0]][peca_selecionada[1]] = 0
            if pode_capturar(jogador_atual, linha, coluna):
                peca_selecionada = (linha, coluna)
            else:
                jogador_atual = 1 if jogador_atual == 2 else 2
                peca_selecionada = None


# Desenhando o tabuleiro
for linha in range(8):
    for coluna in range(8):
        cor_celula = branco if (linha + coluna) % 2 == 0 else preto
        pygame.draw.rect(tela, cor_celula, (coluna * tamanho_celula, linha * tamanho_celula, tamanho_celula, tamanho_celula))
        if tabuleiro[linha][coluna] != 0:
            cor_peca = vermelho if tabuleiro[linha][coluna] == 1 else amarelo
            pygame.draw.circle(tela, cor_peca, (
            coluna * tamanho_celula + tamanho_celula // 2, linha * tamanho_celula + tamanho_celula // 2), tamanho_peca)
        # Desenhando a peça selecionada
        if peca_selecionada != None:
            pygame.draw.circle(tela, verde, (peca_selecionada[1] * tamanho_celula + tamanho_celula // 2,
                                             peca_selecionada[0] * tamanho_celula + tamanho_celula // 2), tamanho_peca, 5)

# Atualizando a tela
pygame.display.update()
clock.tick(60)


if fim_de_jogo():
    print("Fim de jogo!")
    pygame.quit()
    quit()
