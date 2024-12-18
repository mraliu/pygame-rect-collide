import pygame
from oop import *

pygame.init()

screen = pygame.display.set_mode((800,600))
w, h = pygame.display.get_surface().get_size()
font = pygame.font.SysFont('Arial', 20)

bullets = []
    
def displaytext(text):
    text = font.render((str(text)), True, (255, 255, 255))
    textRect = text.get_rect()
    textRect.center = (w*3/4), (50)
    screen.blit(text, textRect)


running = True
clock = pygame.time.Clock() 

falcon = Player(screen, "falcon.png", 70, 75)
tie = Enemies(screen, "tiefighter.png", 50, 50, w/2, 50)

ties = [Enemies(screen, "tiefighter.png", 50, 50, x*50+50, 50) for x in range(10)]

collide = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))

    falcon.draw()
    falcon.move()

    # draw ties in array
    if ties:
        for tie in ties:
            tie.draw()
    
    if falcon.bullets:
        for b in falcon.bullets:
            b.draw()
            b.move()

            #collide
            try:
                for tie in ties:
                    if b.collide(tie):
                        falcon.bullets.remove(b)
                        ties.remove(tie)
                    elif b.ypos <=0:
                        falcon.bullets.remove(b)
            except:
                pass

    displaytext(collide)

    pygame.display.flip()
    clock.tick(60)
pygame.quit()