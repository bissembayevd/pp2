import pygame

pygame.init()
screen = pygame.display.set_mode((600,600))
clock = pygame.time.Clock()
fps = 60

GREEN = (0,255,0)
radius = 20
x, y = 300, 300
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= 20
    if keys[pygame.K_RIGHT]:
        x += 20
    if keys[pygame.K_UP]:
        y -= 20
    if keys[pygame.K_DOWN]:
        y += 20

    if x < 20:
        x = 20
    if x > 580:
        x = 580
    if y < 20:
        y = 20
    if y > 580:
        y = 580

    screen.fill((255,255,255))
    pygame.draw.circle(screen, GREEN, (x, y), radius)

    pygame.display.flip()
    clock.tick(fps)
