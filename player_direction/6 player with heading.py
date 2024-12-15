import pygame, math
pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
font = pygame.font.SysFont('Consola', 22)


player_x = SCREEN_WIDTH/2
player_y = SCREEN_HEIGHT/2
player_speed = 10
player_radius = 50
player_angle = 0
x_smooth = 0.05

running = True
clock = pygame.time.Clock()

def checkkeys():
    global player_x, player_y, player_angle

    key = pygame.key.get_pressed()
    # if key[pygame.K_a] or key[pygame.K_LEFT] == True:
    #     if player_x >= 12.5:
    #         player_x=player_x-player_speed
    # elif key[pygame.K_d] or key[pygame.K_RIGHT]== True:
    #     if player_x <= SCREEN_WIDTH - 50:
    #         player_x=player_x+player_speed


    if key[pygame.K_w] or key[pygame.K_UP] == True:
        player_x += math.sin(player_angle*x_smooth)*1
        player_y += math.cos(player_angle*x_smooth)*1
        if key[pygame.K_q] == True:
            player_angle+=1
        elif key[pygame.K_e] == True:
            player_angle-=1
    elif key[pygame.K_s] or key[pygame.K_DOWN]== True:
        player_x -= math.sin(player_angle*x_smooth)*1
        player_y -= math.cos(player_angle*x_smooth)*1
    elif key[pygame.K_q] == True:
        player_angle+=1
        # pygame.draw.line(screen, (255, 255, 255), (player_x+12.5, player_y+12.5), (player_x+12.5+math.sin(player_angle*x_smooth)*player_radius, player_y+12.5+math.cos(player_angle*x_smooth)*player_radius), 1)
    elif key[pygame.K_e] == True:
        player_angle-=1
    pygame.draw.line(screen, (255, 255, 255), (player_x+12.5, player_y+12.5), (player_x+12.5+math.sin(player_angle*x_smooth)*player_radius, player_y+12.5+math.cos(player_angle*x_smooth)*player_radius), 1)


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
    # checkkeys()
    displaytext(str(player_angle))

    pygame.draw.rect(screen, (0, 255, 0), (player_x, player_y, 25, 25))
    checkkeys()
    pygame.display.flip()
    clock.tick(60)

pygame.quit()