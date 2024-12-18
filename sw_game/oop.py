import pygame
class Player:
    def __init__(self, screen, setImage, setWidth, setHeight):
        self.screen = screen
        self.image = setImage
        self.width = setWidth
        self.height = setHeight
        self.surf = pygame.image.load(self.image).convert_alpha()
        self.surf = pygame.transform.scale(self.surf, (self.width, self.height))
        self.surf = pygame.transform.rotate(self.surf,(0))
        self.xpos = 400
        self.ypos = 500
        self.rect = self.surf.get_rect(topleft=(self.xpos, self.ypos))
        self.xspeed = 10
        self.yspeed = 3 
        self.bullets = []

    def draw(self):
        self.rect = self.surf.get_rect(topleft=(self.xpos, self.ypos))
        self.screen.blit(self.surf, self.rect)
        
    def move(self):
        global bullets
        w=800
        h=600
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
            self.bullets.append(Bullet(self.screen, self.xpos+35, self.ypos))

    def collide(self, obj):
        collide = pygame.Rect.colliderect(self.rect, obj.rect)
        return collide
        
class Bullet:
    def __init__(self, screen, setX, setY):
        self.screen = screen
        self.xpos = setX
        self.ypos = setY
        self.width = 2
        self.height = 10
        self.speed = 3
        self.rect = pygame.Rect(self.xpos, self.ypos, self.width, self.height)

    def draw(self):
        self.rect = pygame.Rect(self.xpos, self.ypos, self.width, self.height)
        pygame.draw.rect(self.screen, (255, 0, 250), self.rect)
    def move(self):
        self.ypos-=self.speed
    def collide(self, obj):
        collide = pygame.Rect.colliderect(self.rect, obj.rect)
        return collide

class Enemies(Player):
    def __init__(self, screen, setImage, setWidth, setHeight, setX, setY):
        super().__init__(screen, setImage, setWidth, setHeight)
        self.xpos = setX
        self.ypos = setY