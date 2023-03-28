import math
import pygame


class Polygon(object):

    def __init__(self, points, color: tuple[int, int, int], surface, scale=1.0, pivot=(0, 0), name=""):

        self.points = points
        self.color = color
        self.pivot = pivot  # special points that are also tracked
        self.scale = scale
        self.name = name

        self.surface = surface

        self.x = 0
        self.y = 0
        self.angle = 0
        self.hitbox = []
        self.pivotPoint = (0, 0)

    def setPos(self, pos: tuple[float, float]):
        self.x = pos[0]
        self.y = pos[1]

        self.pivotPoint = (self.x + self.scale * self.pivot[0] * math.cos(self.angle) + self.scale * self.pivot[1] * math.sin(self.angle),
                           self.y + self.scale * self.pivot[0] * math.sin(self.angle) - self.scale * self.pivot[1] * math.cos(self.angle))

    def rotateTo(self, angle: float):
        self.angle = (-1) * angle * math.pi / 180.0

        self.pivotPoint = (self.x + self.scale * self.pivot[0] * math.cos(self.angle) + self.scale * self.pivot[1] * math.sin(self.angle),
                           self.y + self.scale * self.pivot[0] * math.sin(self.angle) - self.scale * self.pivot[1] * math.cos(self.angle))

    def update_hitbox(self):
        self.hitbox = []
        for i in self.points:  # for every point
            point = (self.x + self.scale * i[0] * math.cos(self.angle) + self.scale * i[1] * math.sin(self.angle),
                     self.y + self.scale * i[0] * math.sin(self.angle) - self.scale * i[1] * math.cos(self.angle))
            self.hitbox.append(point)  # in form [(x1, y1), (x2, y2), ...]

        self.pivotPoint = (self.x + self.scale * self.pivot[0] * math.cos(self.angle) + self.scale * self.pivot[1] * math.sin(self.angle),
                           self.y + self.scale * self.pivot[0] * math.sin(self.angle) - self.scale * self.pivot[1] * math.cos(self.angle))

    def draw(self):
        self.update_hitbox()
        pygame.draw.polygon(self.surface, self.color, self.hitbox)
