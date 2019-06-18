from Character.Animation.animation import *
import pygame
import sys

class Sprite:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.mov={'UP':'false','DOWN':'false','LEFT':'false','RIGHT':'false'}
        self.width=45
        self.height=65
        self.status = 'DOWN'
    def getW(self):        
        return self.width
    def getH(self):        
        return self.height
    def getX(self):        
        return self.x
    def getY(self):        
        return self.y
    def setX(self,n):
        self.x+=n
    def setY(self,n):
        self.y+=n
    def move(self):
        if self.mov['UP']=='true':
            self.setY(-10)
        if self.mov['RIGHT']=='true':
            self.setX(10)
        if self.mov['LEFT']=='true':
            self.setX(-10)
        if self.mov['DOWN']=='true':
            self.setY(10)
    def setStatus(self,n):
        self.status=n
    def getStatus(self):
        return self.status

def handle(event,HULK):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
            HULK.mov['UP']='true'
            HULK.mov['DOWN']='false'
            HULK.setStatus('UP')  
        elif event.key == pygame.K_RIGHT:
            HULK.mov['RIGHT']='true'
            HULK.mov['LEFT']='false'
            HULK.setStatus('RIGHT') 
        elif event.key == pygame.K_LEFT:
            HULK.mov['LEFT']='true'
            HULK.mov['RIGHT']='false'
            HULK.setStatus('LEFT') 
        elif event.key == pygame.K_DOWN:
            HULK.mov['DOWN']='true'
            HULK.mov['UP']='false'
            HULK.setStatus('DOWN') 
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_UP:
            HULK.mov['UP']='false'
        elif event.key == pygame.K_RIGHT:
            HULK.mov['RIGHT']='false'
        elif event.key == pygame.K_LEFT:
            HULK.mov['LEFT']='false'
        elif event.key == pygame.K_DOWN:
             HULK.mov['DOWN']='false' 