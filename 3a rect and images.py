import pygame
pygame.init()

screen = pygame.display.set_mode((800, 600))
w, h = pygame.display.get_surface().get_size()

print(w,h)

# x y width height

# Pygame rects
rect1 = pygame.Rect(100, 250, 50, 50)
rect2 = pygame.Rect(110, 250, 50, 50)

# Pygame sprite
m_falcon = pygame.image.load("falcon.png").convert_alpha()
m_falcon = pygame.transform.scale(m_falcon, (120,150))
m_falcon = pygame.transform.rotate(m_falcon,(0))

new_tie = pygame.image.load("tiefighter3.png").convert()
new_tie.set_colorkey((0,0,0))
new_tie = pygame.transform.scale(new_tie, (95,100))


tie2 = new_tie.copy()
tie2.fill((255, 0, 0, 0), special_flags=pygame.BLEND_RGBA_MULT)
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

    screen.fill((0, 0, 0))

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

    screen.blit(new_tie, (w/3, h/2))
    screen.blit(tie2, (w/3, h/3))

    pygame.display.flip()

# Done! Time to quit.
pygame.quit()