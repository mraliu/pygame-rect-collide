import pygame
pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
font = pygame.font.SysFont('Consola', 22)


player_x = SCREEN_WIDTH/2
player_y = SCREEN_HEIGHT/2
player_speed = 20

running = True
clock = pygame.time.Clock()

def checkkeys():
    global player_x, player_y
    key = pygame.key.get_pressed()
    if key[pygame.K_a] or key[pygame.K_LEFT] == True:
        if player_x >= 12.5:
            player_x=player_x-player_speed
    elif key[pygame.K_d] or key[pygame.K_RIGHT]== True:
        if player_x <= SCREEN_WIDTH - 50:
            player_x=player_x+player_speed
    elif key[pygame.K_w] or key[pygame.K_UP] == True:
        if player_y >= 12.5:
            player_y=player_y-player_speed
    elif key[pygame.K_s] or key[pygame.K_DOWN]== True:
        if player_y <= SCREEN_HEIGHT - 50:
            player_y=player_y+player_speed

def displaytext(text):
    text = font.render((str(text)), True, (255, 255, 255)) # Set text to render as screen
    textRect = text.get_rect(center=(SCREEN_WIDTH*7/8, 20)) # look at first line for position of getrect
    screen.blit(text, textRect)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 0))
    
    # Functions
    checkkeys()
    displaytext("Allen")

    pygame.draw.rect(screen, (0, 255, 0), (player_x, player_y, 25, 25))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()