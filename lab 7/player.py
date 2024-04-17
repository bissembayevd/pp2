import pygame

pygame.mixer.pre_init(44100)
pygame.init()

screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()

first = pygame.mixer.Sound("C:\\Users\\bisse\\OneDrive\\Рабочий стол\\pp2\\labs\\lab 7\\first.mp3")
second = pygame.mixer.Sound("C:\\Users\\bisse\\OneDrive\\Рабочий стол\\pp2\\labs\\lab 7\\second.mp3")
third = pygame.mixer.Sound("C:\\Users\\bisse\\OneDrive\\Рабочий стол\\pp2\\labs\\lab 7\\third.mp3")
first_img = pygame.image.load("C:\\Users\\bisse\\OneDrive\\Рабочий стол\\pp2\\labs\\lab 7\\first.jpg")
second_img = pygame.image.load("C:\\Users\\bisse\\OneDrive\\Рабочий стол\\pp2\\labs\\lab 7\\second.jpeg")
third_img = pygame.image.load("C:\\Users\\bisse\\OneDrive\\Рабочий стол\\pp2\\labs\\lab 7\\third.jpg")
background_surface = pygame.Surface((800, 800))
background_surface.fill((0,0,0))
images = [first_img, second_img, third_img]
sounds = [first, second, third]
current_sound_index = 0
started = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
            if not started:
                sounds[current_sound_index].play()
                started = True
                print("started")
            else:
                print("already started")
        pygame.time.delay(200)
        if event.key == pygame.K_RIGHT:
            if started:
                sounds[current_sound_index].stop()
                current_sound_index = (current_sound_index + 1) % len(sounds)
                sounds[current_sound_index].play()
                print("next sound")
            else:
                print("not started")
            pygame.time.delay(200)
        if event.key == pygame.K_LEFT:
            if started:
                sounds[current_sound_index].stop()
                current_sound_index = (current_sound_index - 1) % len(sounds)
                sounds[current_sound_index].play()
                print("prev sound")
            else:
                print("not started")
            pygame.time.delay(200)
        elif event.key == pygame.K_DOWN:
            if sounds[current_sound_index]:
                sounds[current_sound_index].stop()
                pygame.time.delay(200)
                print("stopped")
                started = False
            print("not stopped")

    if started:
        if current_sound_index == 0:
            background_surface.fill((255,255,255))
        elif current_sound_index == 1:
            background_surface.fill((255,255,255))
        elif current_sound_index == 2:
            background_surface.fill((255,255,255))
        screen.blit(background_surface, (0, 0))
        screen.blit(images[current_sound_index], (150,150))
    else:
        background_surface.fill((0,0,0))
        screen.blit(background_surface, (0, 0))

    pygame.display.flip()
    clock.tick(60)
