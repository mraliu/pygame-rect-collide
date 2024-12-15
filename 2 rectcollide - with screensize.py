import pygame
pygame.init()



# Set up the drawing window
screen = pygame.display.set_mode()

w, h = pygame.display.get_surface().get_size()

print(w,h)

# x y width height
rect1 = pygame.Rect(100, 250, 50, 50)
rect2 = pygame.Rect(110, 250, 50, 50)


running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with white
    screen.fill((255, 255, 255))

    # pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)

    pygame.draw.rect(screen, (0, 0, 255), rect1)
    pygame.draw.rect(screen, (255, 0, 0), rect2)

    collide = pygame.Rect.colliderect(rect1, rect2)

    # print(collide)

    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()