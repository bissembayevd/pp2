import pygame
from random import randrange

RES = 800
SIZE = 40
score = 0
level = 1
x, y = randrange(0, RES, SIZE), randrange(0, RES, SIZE)
apple = randrange(0, RES, SIZE), randrange(80, RES , SIZE)
control={'K_UP':True,'K_DOWN':True,'K_LEFT':True,'K_RIGHT':True,}
length = 1
snake = [(x, y)]
dx, dy = 0, 0
fps = 8

pygame.init()
screen = pygame.display.set_mode([RES, RES])
pygame.display.set_caption("Snake")
clock = pygame.time.Clock()
font_level=pygame.font.SysFont('Arial',26,bold=True)
font_score = pygame.font.SysFont('Arial', 26, bold=True)
font_end = pygame.font.SysFont('Arial', 70, bold=True)


while True:
    screen.fill(pygame.Color('black'))
    [(pygame.draw.rect(screen, pygame.Color('green'), (i, j, SIZE, SIZE))) for i, j in snake]
    pygame.draw.rect(screen, pygame.Color('red'), (*apple, SIZE, SIZE))

    # show score
    render_level = font_score.render(f'LEVEL:{level}', 1, pygame.Color('orange'))
    render_score = font_score.render(f'SCORE:{score}', 1, pygame.Color('orange'))
    screen.blit(render_level, (350, 10))
    screen.blit(render_score, (350, 40))
    # snake movement
    x += dx * SIZE
    y += dy * SIZE
    snake.append((x, y))
    snake = snake[-length:]

    # eating apple
    if snake[-1] == apple:
        while True:
            new_apple = randrange(0, RES, SIZE), randrange(80,RES , SIZE)
            if new_apple not in snake:
                apple = new_apple
                break
        length += 1
        score += 1
        if score%3==0:
            level+=1
            fps+=2

    # game over
    if x < 0 or x > RES-SIZE or y < 0 or y > RES-SIZE or len(snake) != len(set(snake)):
        while True:
            render_end = font_end.render('GAME OVER', 1, pygame.Color('orange'))
            screen.blit(render_end, (240, 350))
            pygame.display.flip()
            pygame.time.delay(2000)
            pygame.quit()
            exit()

    pygame.display.flip()
    clock.tick(fps)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # control
    key = pygame.key.get_pressed()
    if key[pygame.K_UP] and control['K_UP']:
        dx, dy = 0, -1
        control={'K_UP':True,'K_DOWN':False,'K_LEFT':True,'K_RIGHT':True,}
    if key[pygame.K_DOWN] and control['K_DOWN']:
        dx, dy = 0, 1
        control={'K_UP':False,'K_DOWN':True,'K_LEFT':True,'K_RIGHT':True,}
    if key[pygame.K_LEFT] and control['K_LEFT']:
        dx, dy = -1, 0
        control={'K_UP':True,'K_DOWN':True,'K_LEFT':True,'K_RIGHT':False,}
    if key[pygame.K_RIGHT] and control['K_RIGHT']:
        dx, dy = 1, 0
        control={'K_UP':True,'K_DOWN':True,'K_LEFT':False,'K_RIGHT':True,}
