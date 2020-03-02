import pygame
from pygame.locals import *
from random import randint

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 600

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
direcao = LEFT

pygame.display.set_caption('Snake - Israel Alves Lucena Gomes')
snake = [(200, 200), (210, 200), (220, 200)]

snake_skin = pygame.Surface((10, 10))
snake_skin.fill((255, 255, 255))
food = pygame.Surface((10, 10))
food.fill((255, 0, 0))

dificuldade = 20


def posicao_no_grid():
    x = randint(0, 590)
    y = randint(0, 590)

    return x // 10 * 10, y // 10 * 10


def sentido_cobra(direcao):
    if direcao == UP:
        return snake[0][0], snake[0][1] - 10
    if direcao == LEFT:
        return snake[0][0] - 10, snake[0][1]
    if direcao == DOWN:
        return snake[0][0], snake[0][1] + 10
    if direcao == RIGHT:
        return snake[0][0] + 10, snake[0][1]


def colidiu(c1, c2):
    """
    Essa função returna True se houve colisão.

    :param c1: Geralmente a cabeça da cobra Anaconda
    :param c2: Alguma posição do quadro: Comida ou borda
    :return: True, caso haja colisão ou False, caso contrário
    """
    return (c1[0] == c2[0]) and (c1[1] == c2[1])


def saiu_do_grid(posicao):

    if posicao[0] > SCREEN_WIDTH or posicao[0] < 0:
        return True
    if posicao[1] > SCREEN_HEIGHT or posicao[1] < 0:
        return True
    else:
        return False


food_posicao = tuple(posicao_no_grid())
clock = pygame.time.Clock()

while True:

    clock.tick(dificuldade/2)

    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_0:
                pygame.quit()

            if event.key == K_UP:
                direcao = UP
            if event.key == K_DOWN:
                direcao = DOWN
            if event.key == K_LEFT:
                direcao = LEFT
            if event.key == K_RIGHT:
                direcao = RIGHT

    snake[0] = sentido_cobra(direcao)

    i = 1
    while i < len(snake)-1:
        if colidiu(snake[0], snake[i]):
            pygame.quit()
        i += 1

    if saiu_do_grid(snake[0]):
        if snake[0][0] > SCREEN_WIDTH:
            snake[0] = (0, snake[0][1])
        if snake[0][0] < 0:
            snake[0] = (SCREEN_WIDTH, snake[0][1])
        if snake[0][1] > SCREEN_HEIGHT:
            snake[0] = (snake[0][0], 0)
        if snake[0][1] < 0:
            snake[0] = (snake[0][0], SCREEN_HEIGHT)

    if colidiu(snake[0], food_posicao):
        food_posicao = posicao_no_grid()
        snake.append((0, 0))
        dificuldade += 1

    i = 0
    for i in range(len(snake) - 1, 0, -1):
        snake[i] = (snake[i-1][0], snake[i-1][1])


    screen.fill((0, 0, 0))
    screen.blit(food, food_posicao)
    for posicao in snake:
        screen.blit(snake_skin, posicao)
    pygame.display.update()
