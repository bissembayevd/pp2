import pygame

pygame.init()

# Set up the screen
screen = pygame.display.set_mode((1080, 800))

# Create a clock to control the frame rate
clock = pygame.time.Clock()

# Define color constants
RED = (230, 0, 0)
GREEN = (0, 230, 0)
BLUE = (0, 0, 230)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW=(255,234,0)
FPS=400

# Store colors in a list
colors = [RED, GREEN, YELLOW]

# Set the initial color to white
color = WHITE

# Load the eraser image and resize it
eraser = pygame.image.load("C:\\Users\\bisse\\OneDrive\\Рабочий стол\\pp2\\labs\\lab 8\\eraser.png")
eraser = pygame.transform.scale(eraser, (70, 70))

# Function to draw color rectangles
def draw_rect(index):
    pygame.draw.rect(screen, colors[index], (index*40, 0, 40, 40))

# Function to pick a color based on mouse position
def pick_color():
    click = pygame.mouse.get_pressed()
    x, y = pygame.mouse.get_pos()
    if click[0]:
        if 0 <= x <= 40 and 0 <= y <= 40:
            return RED
        elif 40 < x <= 80 and 0 <= y <= 40:
            return GREEN
        elif 80 < x <= 120 and 0 <= y <= 40:
            return YELLOW
        elif 1010 <= x <= 1080 and 0 <= y <= 40:
            return BLACK
        elif 130 <= x <= 170 and 0 <= y <= 40:
            return "rect"
    return color

# Function to draw on the screen
def painting(color):
    click = pygame.mouse.get_pressed()
    x, y = pygame.mouse.get_pos()
    if click[0] and y>65:
        if color != 'rect':
            pygame.draw.circle(screen, color, (x, y), 27)
        else:
            pygame.draw.rect(screen, WHITE, (x, y, 40, 40), 4)

# Main game loop
while True:
    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    # Draw color rectangles
    for i in range(len(colors)):
        draw_rect(i)

    # Draw the eraser
    screen.blit(eraser, (1010, 0))

    # Draw a white rectangle for the eraser
    pygame.draw.rect(screen, WHITE, (130, 0, 40, 40), 4)

    # Pick the color and draw on the screen
    color = pick_color()
    painting(color)


    clock.tick(FPS)

    pygame.display.update()
