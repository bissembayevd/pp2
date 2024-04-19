import pygame
import random

# Initialize pygame
pygame.init()

# Screen settings
screen_width, screen_height = 400, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Racer")

# Clock and FPS
clock = pygame.time.Clock()
FPS = 60

# Load images
car_image = pygame.image.load("C:\\Users\\bisse\\OneDrive\\Рабочий стол\\pp2\\labs\\lab 8\\player.png")
car_image = pygame.transform.scale(car_image, (60, 110))
enemy_image = pygame.image.load("C:\\Users\\bisse\\OneDrive\\Рабочий стол\\pp2\\labs\\lab 8\\Enemy.png")
coin_image = pygame.image.load("C:\\Users\\bisse\\OneDrive\\Рабочий стол\\pp2\\labs\\lab 8\\coin.png")
background = pygame.image.load("C:\\Users\\bisse\\OneDrive\\Рабочий стол\\pp2\\labs\\lab 8\\AnimatedStreet.png")

# Load and play music
pygame.mixer.music.load("C:\\Users\\bisse\\OneDrive\\Рабочий стол\\pp2\\labs\\lab 8\\racer.mp3")
pygame.mixer.music.play(-1)

# Font setup
font_score = pygame.font.SysFont('Verdana', 20, bold=True)
font_game_over = pygame.font.SysFont('Verdana', 40, bold=True)

# Initialize score
score = 0
render_score = font_score.render(f'COINS: {score}', 1, pygame.Color('black'))

# Car settings
car_x, car_y = 180, 480
car_width, car_height = 60, 110
car_rect = car_image.get_rect(topleft=(car_x, car_y))

# Enemy class
class Enemy(pygame.sprite.Sprite):
    speed = 7

    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(enemy_image, (60, 110))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, screen_width-40), 0)

    def update(self):
        self.rect.y += self.speed
        if self.rect.y > screen_height:
            self.rect.y = 0
            self.rect.center = (random.randint(40, screen_width-40), 0)

# Coins class
class Coin(pygame.sprite.Sprite):
    speed=5

    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(coin_image, (80, 60))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, screen_width-40), 0)

    def update(self):
        self.rect.y += self.speed
        if self.rect.y > screen_height:
            self.rect.y = 0
            self.rect.center = (random.randint(40, screen_width-40), 0)

# Sprite group for enemies
enemies = pygame.sprite.Group()
coins = pygame.sprite.Group()

# Function to spawn enemies
def spawn_enemy():
    if len(enemies) == 0:
        enemy = Enemy()
        enemies.add(enemy)

# Function to spawn coins
def spawn_coin():
    if len(coins) == 0:
        coin = Coin()
        coins.add(coin)

# Main game loop
game_over = False
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            pygame.mixer.music.stop()

    # Handle car movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        car_x -= 10
    if keys[pygame.K_RIGHT]:
        car_x += 10

    # Limit car movement within screen boundaries
    if car_x < 0:
        car_x = 0
    if car_x > 340:
        car_x = 340

    # Update car rectangle
    car_rect.topleft = (car_x, car_y)

    # Spawn enemies and coins
    spawn_enemy()
    spawn_coin()

    # Update enemy positions
    for enemy in enemies:
        enemy.update()
        if enemy.rect.colliderect(car_rect):
            game_over = True
            pygame.mixer.music.load("C:\\Users\\bisse\\OneDrive\\Рабочий стол\\pp2\\labs\\lab 8\\crash.wav")
            pygame.mixer.music.play(0)

    for coin in coins:
        coin.update()
        if coin.rect.colliderect(car_rect):
            coins.remove(coin)
            score += 1
            render_score = font_score.render(f'COINS: {score}', 1, pygame.Color('black'))
            # Increase enemy and coin speed when a coin is collected
            Enemy.speed += 0.2
            Coin.speed += 0.2

    # Draw everything
    screen.blit(background, (0, 0))
    screen.blit(car_image, (car_x, car_y))
    enemies.draw(screen)
    coins.draw(screen)
    screen.blit(render_score, (280, 10))

    pygame.display.flip()
    clock.tick(FPS)

# Game over screen
game_over_text = font_game_over.render('GAME OVER', 1, pygame.Color('black'))
screen.blit(game_over_text, (screen_width // 2 - 135, screen_height // 2 - 50))
pygame.display.flip()

# Wait for a few seconds before quitting
pygame.time.wait(2000)
pygame.quit()
