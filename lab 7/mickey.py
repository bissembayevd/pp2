import pygame
import sys
import datetime


pygame.init()
screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()

mikey = pygame.image.load("C:\\Users\\bisse\\OneDrive\\Рабочий стол\\pp2\\labs\\lab 7\\mikey.png")
hour_hand = pygame.image.load("C:\\Users\\bisse\\OneDrive\\Рабочий стол\\pp2\\labs\\lab 7\\hour.png")
minute_hand = pygame.image.load("C:\\Users\\bisse\\OneDrive\\Рабочий стол\\pp2\\labs\\lab 7\\min.png")

mikey_rect = mikey.get_rect(center=(400, 400))
hour_hand_rect = hour_hand.get_rect(center=mikey_rect.center)
minute_hand_rect = minute_hand.get_rect(center=mikey_rect.center)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    current_time = datetime.datetime.now()
    hour_angle = (current_time.minute * 6) - 90
    minute_angle = (current_time.second * 6) - 90

    rotated_hour_hand = pygame.transform.rotate(hour_hand, -hour_angle)
    rotated_minute_hand = pygame.transform.rotate(minute_hand, -minute_angle)
    hour_hand_rect = rotated_hour_hand.get_rect(center=mikey_rect.center)
    minute_hand_rect = rotated_minute_hand.get_rect(center=mikey_rect.center)

    screen.fill((255,255,255))
    screen.blit(mikey, mikey_rect)
    screen.blit(rotated_hour_hand, hour_hand_rect)
    screen.blit(rotated_minute_hand, minute_hand_rect)

    pygame.display.update()
    clock.tick(60)
