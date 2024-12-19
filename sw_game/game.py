import pygame, random
from oop import *

pygame.init()

screen = pygame.display.set_mode((800,600))
w, h = pygame.display.get_surface().get_size()
font = pygame.font.SysFont('Arial', 20)

bullets = []
    
def displaytext(text, xpos, ypos): # Used for displaying text on screen
    text = font.render((str(text)), True, (255, 255, 255))
    textRect = text.get_rect()
    textRect.center = (xpos), (ypos)
    screen.blit(text, textRect)


running = True
clock = pygame.time.Clock() 

# Instantiation objects
falcon = Player(screen, "falcon.png", 70, 75)
tie = Enemies(screen, "tiefighter.png", 50, 50, w/2, 50)
ties = [Enemies(screen, "tiefighter.png", 50, 50, 25+x*75, random.randint(50, 150)) for x in range(10)]

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
            tie.moveto()
    
    if falcon.bullets:
        for b in falcon.bullets:
            b.draw()
            b.move()

            #collide
            try:
                for tie in ties:
                    if b.collide(tie):
                        falcon.bullets.remove(b)
                        if tie.takedmg(b.dmg):
                            ties.remove(tie)
                    elif b.ypos <=0:
                        falcon.bullets.remove(b)
            except:
                pass

    displaytext(collide, w*3/4, 50)
    displaytext(str(len(falcon.bullets)), w*3/4, 100)

    pygame.display.flip()
    clock.tick(60)
pygame.quit()