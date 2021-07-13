import pygame
pygame.init()

class GameOverError(Exception):
    pass

class Snek:

    def __init__(self, xBound, yBound, delta:int, initX=0, intiY=0, size=15, color=(255,255,255)):
        self.x = initX
        self.y = intiY
        self.listPos = [[initX, intiY]]
        self.dir = ""
        self.delta = delta
        self.color = color
        self.xBound = xBound
        self.yBound = yBound

    def isEating(self, foodPos:list):
        if self.x == foodPos[0] and self.y == foodPos[1]:
            return True
        else:
            return False

    def move(self, foodPos:list):
        directionFlag = 1
        if self.dir == "left":
            self.x -= self.delta
        elif self.dir == "right":
            self.x += self.delta
        elif self.dir == "up":
            self.y -= self.delta
        elif self.dir == "down":
            self.y += self.delta
        else:
            directionFlag = 0
        if directionFlag:
            self.listPos += [[self.x, self.y]]
            if not self.isEating(foodPos):
                self.listPos = self.listPos[1:]

    def draw(self, win: pygame.display): #call in draw helper function 
        for i in self.listPos:
            pygame.draw.rect(win, self.color, [i[0],i[1], self.delta, self.delta])
            if i == self.listPos[-1]:
                pygame.draw.rect(win, (0,0,0), [i[0]+3,i[1]+3,self.delta-6, self.delta-6])

    def headCollidesWithSelf(self):
        if [self.x, self.y] in self.listPos[:-1]:
            return True
        else:
            return False

    def headCollidesWith(self, collideList: list):
        if [self.x,self.y] in collideList:
            return True
        else:
            return False

    def keyboardInput(self, foodPos: list): #call in loop
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.dir = "left"
        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.dir = "right"
        elif keys[pygame.K_UP] or keys[pygame.K_w]:
            self.dir = "up"
        elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.dir = "down"
        if self.x < 0 or self.y < 0 or self.x > self.xBound or self.y > self.yBound:
            raise GameOverError("Snake went out of bounds.")
        elif self.headCollidesWithSelf():
            raise GameOverError("Snake's head collided with itself.")
        else:
            self.move(foodPos)
