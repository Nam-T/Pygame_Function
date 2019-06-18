import pygame, math, sys, os

size = width, height = 640, 480
screen = pygame.display.set_mode(size)
screenRefresh = True
textboxGroup = pygame.sprite.OrderedUpdates()
spriteGroup = pygame.sprite.OrderedUpdates()
class Background():
    def __init__(self):
        self.colour = pygame.Color("black")

    def setTiles(self,tiles):
        if type(tiles) is str:
            self.tiles = [[loadImage(tiles)]]
        elif type(tiles[0]) is str:
            self.tiles = [[loadImage(i) for i in tiles]]
        else:
            self.tiles = [ [loadImage(i) for i in row] for row in tiles]
        self.stagePosX = 0
        self.stagePosY = 0
        self.tileWidth = self.tiles[0][0].get_width()
        self.tileHeight = self.tiles[0][0].get_height()
        screen.blit(self.tiles[0][0],[0,0])
        self.surface = screen.copy()

    def scroll(self,x,y):
        self.stagePosX -= x
        self.stagePosY -= y
        col = (self.stagePosX % (self.tileWidth * len(self.tiles[0]))) // self.tileWidth
        xOff = (0 - self.stagePosX%self.tileWidth)
        row = (self.stagePosY % (self.tileHeight * len(self.tiles))) // self.tileHeight
        yOff = (0 - self.stagePosY % self.tileHeight)

        col2 = ((self.stagePosX + self.tileWidth) % (self.tileWidth * len(self.tiles[0]))) // self.tileWidth
        row2 = ((self.stagePosY + self.tileHeight) % (self.tileHeight * len(self.tiles))) // self.tileHeight
        screen.blit(self.tiles[row][col], [xOff, yOff])
        screen.blit(self.tiles[row][col2], [xOff + self.tileWidth, yOff])
        screen.blit(self.tiles[row2][col], [xOff, yOff+self.tileHeight])
        screen.blit(self.tiles[row2][col2], [xOff + self.tileWidth, yOff + self.tileHeight])

        self.surface = screen.copy()

    def setColour(self,colour):
        self.colour = parseColour(colour)
        screen.fill(self.colour)
        pygame.display.update()
        self.surface = screen.copy()


background = Background()

def loadImage(fileName, useColorKey=False):
    if os.path.isfile(fileName):
        image = pygame.image.load(fileName)
        image = image.convert_alpha()
        # Return the image
        return image
    else:
        raise Exception("Error loading image: " + fileName + " - Check filename and path?")


def scrollBackground(x,y):
    global background
    background.scroll(x,y)

def updateDisplay():
    global background
    spriteRects = spriteGroup.draw(screen)
    textboxRects = textboxGroup.draw(screen)
    pygame.display.update()
    spriteGroup.clear(screen, background.surface)
    textboxGroup.clear(screen, background.surface)

def setBackgroundImage(img):
    global background
    background.setTiles(img)
    if screenRefresh:
        updateDisplay()