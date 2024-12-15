import pygame, math
pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

running = True
clock = pygame.time.Clock()

print(math.sin(math.pi/2)*10, math.cos(math.pi/2)*10)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 0))

    # Radians
    # pygame.draw.circle(screen, (255, 255, 255), (SCREEN_WIDTH/2, SCREEN_HEIGHT/2), 3)
    # pygame.draw.circle(screen, (255, 0, 0), (SCREEN_WIDTH/2+math.sin(math.pi/2)*10, SCREEN_HEIGHT/2), 3)

    # Degrees
    # pygame.draw.circle(screen, (255, 255, 255), (SCREEN_WIDTH/2, SCREEN_HEIGHT/2), 3)
    # pygame.draw.circle(screen, (255, 0, 0), (SCREEN_WIDTH/2+math.sin(math.pi/2)*10, SCREEN_HEIGHT/2), 3)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()