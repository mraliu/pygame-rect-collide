import pygame
pygame.init()

class Car:
    def __init__(self, x, y, image):
        if not image == None:
            self.image = image
            self.surface = pygame.image.load(self.image).convert_alpha() # Convert to transparent
            self.surface = pygame.transform.scale(self.surface, (50, 60)) # Scale the image
        
        self.direction = 0
        self.x = x
        self.y = y
        self.destination = [x, y]
    
    def changeDirection(self, angle):
        self.surface = pygame.transform.rotate(self.surface,(angle))

    def setDestination(self, coords):
        self.destination = coords

    def moveTo(self):
        
        if self.x < self.destination[0]:
            self.x+=1
        if self.x > self.destination[0]:
            self.x-=1
        if self.y < self.destination[1]:
            self.y+=1
        if self.y > self.destination[1]:
            self.y-=1
        
        

# Game Values
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Object Values
newpath = []
path = [(210, 256), (146, 162), (415, 101), (584, 65), (675, 190), (646, 335), (626, 484)]
falcon = Car(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, "falcon.png")

red = Car(210, 256, None)
green = Car(415, 101, None)


running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            newpath.append(pygame.mouse.get_pos())

            red.setDestination(pygame.mouse.get_pos())
            # print(newpath)

    screen.fill((0, 0, 0))

    # for point in newpath:
    #     pygame.draw.circle(screen, (255, 0, 0), point, 2)

    # for point in path:
    #     screen.blit(falcon.surface, point)    

    # red.setDestination([green.x, green.y])
    red.moveTo()

    pygame.draw.circle(screen, (255, 0, 0), (red.x, red.y), 2) #red
    pygame.draw.circle(screen, (0, 255, 0), (green.x, green.y), 2) #green

    

    pygame.display.flip()
    clock.tick(60)
pygame.quit()