import pygame
import math

class New_Object(object):
    
    def __init__(self, ListOfPoints, ListOfColors, surface, border_width=0): #should be a nested list
                            #ex. [[(2, 3), (4, 5)], [(6, 7), (8, 9)]] -> 2 objects with points
                            #2, 3 and 4, 5 for object 1 and 6, 7 and 8, 9 for object 2
        self.ListOfPoints = ListOfPoints
        self.ListOfColors = ListOfColors
        self.surface = surface
        self.border_width = border_width
        
        self.x = 0
        self.y = 0
        self.angle = 0
        self.hitbox = []
        
    def rotateTo(self, angle):
        self.angle = (-1) * angle * math.pi/180.0
    
    def update_hitbox(self):
        self.hitbox = []
        for i in self.ListOfPoints: #for every shape in ListOfPoints
            polygon = []
            for j in i:
                point = (self.x+j[0]*math.cos(self.angle)-j[1]*math.sin(self.angle), 
                         self.y+j[0]*math.sin(self.angle)+j[1]*math.cos(self.angle))
                polygon.append(point) #in form [(x1, y1), (x2, y2), ...]
            self.hitbox.append(polygon)
    
    def draw(self):
        self.update_hitbox()
        for i in range(len(self.hitbox)): #for every shape in the hitbox
            pygame.draw.polygon(self.surface, self.ListOfColors[i], self.hitbox[i], width=self.border_width)
