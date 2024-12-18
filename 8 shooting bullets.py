import pygame
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

class Player:
    def __init__(self, setImage, setWidth, setHeight):
        self.image = setImage
        self.width = setWidth
        self.height = setHeight
        self.surf = pygame.image.load(self.image).convert_alpha()
        self.surf = pygame.transform.scale(self.surf, (self.width, self.height))
        self.surf = pygame.transform.rotate(self.surf,(0))
        self.xpos = w/2
        self.ypos = h/2
        self.rect = self.surf.get_rect(topleft=(self.xpos, self.ypos))
        self.xspeed = 10
        self.yspeed = 3 

    def draw(self):
        self.rect = self.surf.get_rect(topleft=(self.xpos, self.ypos))
        screen.blit(self.surf, self.rect)
        
    def move(self):
        global bullets
        key = pygame.key.get_pressed()
        if key[pygame.K_a] == True:
            if self.xpos >= 0+10:
                self.xpos=self.xpos-self.xspeed
        elif key[pygame.K_d] == True:
            if self.xpos <= w - 80:
                self.xpos=self.xpos+self.xspeed
        elif key[pygame.K_w] == True:
            if self.ypos >= 0+5:
                self.ypos=self.ypos-self.yspeed
        elif key[pygame.K_s] == True:
            if self.ypos <= h - 75:
                self.ypos=self.ypos+self.yspeed
        elif key[pygame.K_SPACE] == True:
            bullets.append(Bullet(self.xpos+35, self.ypos))
        
class Bullet:
    def __init__(self, setX, setY):
        self.xpos = setX
        self.ypos = setY
        self.width = 2
        self.height = 10
        self.speed = 3
        self.rect = pygame.Rect(self.xpos, self.ypos, self.width, self.height)

    def draw(self):
        self.rect = pygame.Rect(self.xpos, self.ypos, self.width, self.height)
        pygame.draw.rect(screen, (255, 0, 250), self.rect)
    def move(self):
        self.ypos-=self.speed

class Enemies(Player):
    def __init__(self, setImage, setWidth, setHeight, setX, setY):
        super().__init__(setImage, setWidth, setHeight)
        self.xpos = setX
        self.ypos = setY

running = True
clock = pygame.time.Clock() 

falcon = Player("falcon.png", 70, 75)
tie = Enemies("tiefighter.png", 50, 50, w/2, 50)

ties = [Enemies("tiefighter.png", 50, 50, x*50+50, 50) for x in range(10)]

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
    
    if bullets:
        for b in bullets:
            b.draw()
            b.move()

            #collide
            try:
                for tie in ties:
                    collide = pygame.Rect.colliderect(b.rect, tie.rect)
                    if collide:
                        bullets.remove(b)
                        ties.remove(tie)
                    elif b.ypos <=0:
                        bullets.remove(b)
            except:
                pass

    displaytext(collide)

    pygame.display.flip()
    clock.tick(60)
pygame.quit()