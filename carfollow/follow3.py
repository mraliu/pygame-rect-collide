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
        self.xdiff = 0
        self.ydiff = 0
    
    def changeDirection(self, angle):
        self.surface = pygame.transform.rotate(self.surface,(angle))

    def setDestination(self, coords):
        self.destination = coords

        self.xdiff = abs(self.x-self.destination[0]) #abs converts to positive value to find difference between x's
        self.ydiff = abs(self.y-self.destination[1])

        self.scalefx = 1 # use to adjust the changes in x or y
        self.scalefy = 1

        if self.xdiff > self.ydiff:
            print("x greater", self.scalefx, self.scalefy)
            self.scalefy = self.ydiff / self.xdiff 

        elif self.ydiff > self.xdiff:
            print("y greater", self.scalefy, self.scalefy)
            self.scalefx = self.xdiff / self.ydiff 

    def moveTo(self):

        if self.x < self.destination[0]:
            self.x+=self.scalefx
        if self.x > self.destination[0]:
            self.x-=self.scalefx
        if self.y < self.destination[1]:
            self.y+=self.scalefy
        if self.y > self.destination[1]:
            self.y-=self.scalefy
        
        

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


    red.moveTo()

    pygame.draw.circle(screen, (255, 0, 0), (red.x, red.y), 2) #red
    # pygame.draw.circle(screen, (0, 255, 0), (green.x, green.y), 2) #green

    pygame.display.flip()
    clock.tick(60)
pygame.quit()