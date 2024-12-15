import pygame
pygame.init()



# Set up the drawing window
screen = pygame.display.set_mode()

w, h = pygame.display.get_surface().get_size()

print(w,h)

# x y width height

# Pygame rects
rect1 = pygame.Rect(100, 250, 50, 50)
rect2 = pygame.Rect(110, 250, 50, 50)

# Pygame sprite
m_falcon = pygame.image.load("falcon.png").convert_alpha()
# m_falcon_rect = m_falcon.get_rect(topleft=(135,150))

# print(m_falcon_rect.x, m_falcon_rect.y)

m_falcon = pygame.transform.scale(m_falcon, (135,150))
m_falcon = pygame.transform.rotate(m_falcon,(0))

player_x = w/2
player_y = h/2

font = pygame.font.SysFont('Arial', 20)


collide=False

running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

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

    screen.fill((255, 255, 255))

    # pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)

    pygame.draw.rect(screen, (0, 0, 255), rect1)
    # pygame.draw.rect(screen, (255, 0, 0), rect2)


    m_falcon_rect = m_falcon.get_rect()



    collide = pygame.Rect.colliderect(rect1, m_falcon_rect)

    # testtext = str(m_falcon_rect.width) + str(m_falcon_rect.y)

    text = font.render((str(collide)), True, (0,0,0))
    textRect = text.get_rect()
    textRect.center = (w*3/4), (50)
    screen.blit(text, textRect)
    
    screen.blit(m_falcon, (player_x, player_y))


    pygame.display.flip()

# Done! Time to quit.
pygame.quit()