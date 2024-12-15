import pygame
pygame.init()

screen = pygame.display.set_mode((800,600))
w, h = pygame.display.get_surface().get_size()
font = pygame.font.SysFont('Arial', 20)

rect1 = pygame.Rect(100, 250, 50, 50)
rect2 = pygame.Rect(110, 250, 50, 50)

# Pygame sprite
m_falcon = pygame.image.load("falcon.png").convert_alpha()
m_falcon = pygame.transform.scale(m_falcon, (135/2,150/2))
m_falcon = pygame.transform.rotate(m_falcon,(0))

player_x = w/2
player_y = h/2

collide=False

def checkkeys():
    global player_x, player_y
    key = pygame.key.get_pressed()
    if key[pygame.K_a] or key[pygame.K_LEFT] == True:
        if player_x >= 0:
            player_x=player_x-10
    elif key[pygame.K_d] or key[pygame.K_RIGHT]== True:
        if player_x <= w - 80:
            player_x=player_x+10
    elif key[pygame.K_w] or key[pygame.K_UP] == True:
        if player_y >= 0:
            player_y=player_y-3
    elif key[pygame.K_s] or key[pygame.K_DOWN]== True:
        if player_y <= h - 110:
            player_y=player_y+3

def displaytext(text):
    text = font.render((str(collide)), True, (0,0,0))
    textRect = text.get_rect()
    textRect.center = (w*3/4), (50)
    screen.blit(text, textRect)

running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    checkkeys()
    screen.fill((255, 255, 255))


    pygame.draw.rect(screen, (0, 0, 255), rect1)
    
    # rect2 = pygame.Rect(player_x, player_y, 50, 50)
    # pygame.draw.rect(screen, (255, 0, 0), rect2)

    m_falcon_rect = m_falcon.get_rect(topleft=(player_x, player_y))

    collide = pygame.Rect.colliderect(rect1, m_falcon_rect)
    screen.blit(m_falcon, m_falcon_rect)


    displaytext(collide)
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()