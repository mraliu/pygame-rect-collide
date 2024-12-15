# left – sets the left side of the rectangle. right – sets the right side of the rectangle. top – sets the top side of the rectangle. bottom – sets the bottom side of the rectangle. center – sets the center of the rectangle. topleft – sets the top-left corner of the rectangle. bottomleft – sets the bottom-left corner of the rectangle. topright – sets the top-right corner of the rectangle. bottomright – sets the bottom-right corner of the rectangle. centerx – sets the x-coordinate of the center of the rectangle. centery – sets the y-coordinate of the center of the rectangle. size – sets the size (width and height) of the rectangle. width – sets the width of the rectangle. height – sets the height of the rectangle.

import pygame
pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

font = pygame.font.SysFont('Arial', 20) # Set font
running = True
clock = pygame.time.Clock()

def displaytext(text):
    text = font.render((str(text)), True, (255, 255, 255)) # Set text to render as screen
    textRect = text.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)) # look at first line for position of getrect
    screen.blit(text, textRect)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 0))

    displaytext("My Text")
    pygame.display.flip()
    clock.tick(60)

pygame.quit()