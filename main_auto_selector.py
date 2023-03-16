display_size = (800, 600)

space_between = 15
total_height = 400
total_width = 800
side_border = 20
top_border = 50
bottom_border = 20

roboRio_server = "10.9.91.2"

categories = ["station", "place",  "elements", "autobalance"]

import math
import pygame

class Polygon(object):
    
    def __init__(self, Points, Color, surface, scale=1.0, Pivot=(0, 0), name=""):
        
        self.Points = Points
        self.Color = Color
        self.Pivot = Pivot # special points that are also tracked
        self.scale = scale
        self.name = name
        
        self.surface = surface
        
        self.x = 0
        self.y = 0
        self.angle = 0
        self.hitbox = []
        self.pivotPoint = (0, 0)
    
    def setPos(self, pos : tuple[float, float]):
        self.x = pos[0]
        self.y = pos[1]
        
        self.pivotPoint = (self.x + self.scale * self.Pivot[0] * math.cos(self.angle) + self.scale * self.Pivot[1] * math.sin(self.angle), 
                           self.y + self.scale * self.Pivot[0] * math.sin(self.angle) - self.scale * self.Pivot[1] * math.cos(self.angle))
        
    def rotateTo(self, angle : float):
        self.angle = (-1) * angle * math.pi / 180.0
        
        self.pivotPoint = (self.x + self.scale * self.Pivot[0] * math.cos(self.angle) + self.scale * self.Pivot[1] * math.sin(self.angle), 
                           self.y + self.scale * self.Pivot[0] * math.sin(self.angle) - self.scale * self.Pivot[1] * math.cos(self.angle))
    
    def update_hitbox(self):
        self.hitbox = []
        for i in self.Points: #for every point
            point = (self.x + self.scale * i[0] * math.cos(self.angle) + self.scale * i[1] * math.sin(self.angle), 
                     self.y + self.scale * i[0] * math.sin(self.angle) - self.scale * i[1] * math.cos(self.angle))
            self.hitbox.append(point) #in form [(x1, y1), (x2, y2), ...]
            
        self.pivotPoint = (self.x + self.scale * self.Pivot[0] * math.cos(self.angle) + self.scale * self.Pivot[1] * math.sin(self.angle), 
                           self.y + self.scale * self.Pivot[0] * math.sin(self.angle) - self.scale * self.Pivot[1] * math.cos(self.angle))
    
    def draw(self):
        self.update_hitbox()
        pygame.draw.polygon(self.surface, self.Color, self.hitbox)

black = (0, 0, 0)
white = (234, 234, 234)
gray = (128, 128, 128)

red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

clear_black = (0, 0, 0, 128)

clear_red = (255, 0, 0, 128)
clear_green = (0, 255, 0, 128)
clear_blue = (0, 0, 255, 128)

orange = (255, 128, 0)
yellow = (255, 255, 0)
lime = (128, 255, 0)

# total_height - 1 or 2 * space_between / 2 or 3
# total_width - 2 * space_between / 3

temp = [
    (total_height - top_border - bottom_border - space_between) / 2, 
    (total_height - top_border - bottom_border - 2 * space_between) / 3, 
    (total_width - 2 * side_border - 3 * space_between) / 4
]

pygame.init()
gameDisplay = pygame.display.set_mode(display_size)
pygame.display.set_caption('AutoSelector Display')
clock = pygame.time.Clock()

background_color = white

grid = [[
    Polygon(
        [[-total_width / 2, total_height / 2],
        [total_width / 2, total_height / 2],
        [total_width / 2, -total_height / 2],
        [-total_width / 2, -total_height / 2]], 
        black, 
        gameDisplay
    )
], [
    Polygon(
        [[-total_width / 2 + side_border, total_height / 2 - top_border],
        [-total_width / 2 + side_border + temp[2], total_height / 2 - top_border],
        [-total_width / 2 + side_border + temp[2], total_height / 2 - top_border - temp[0]],
        [-total_width / 2 + side_border, total_height / 2 - top_border - temp[0]]], 
        blue, 
        gameDisplay, 
        Pivot=(-total_width / 2 + side_border + temp[2] / 2, total_height / 2 - top_border - temp[0] / 2), 
        name="blue"
    ), 
    Polygon(
        [[-total_width / 2 + side_border, -total_height / 2 + bottom_border],
        [-total_width / 2 + side_border + temp[2], -total_height / 2 + bottom_border],
        [-total_width / 2 + side_border + temp[2], -total_height / 2 + bottom_border + temp[0]],
        [-total_width / 2 + side_border, -total_height / 2 + bottom_border + temp[0]]], 
        red, 
        gameDisplay, 
        Pivot=(-total_width / 2 + side_border + temp[2] / 2, -total_height / 2 + bottom_border + temp[0] / 2), 
        name="red"
    )
], [
    Polygon(
        [[-temp[2] - space_between / 2, total_height / 2 - top_border], 
        [-space_between / 2, total_height / 2 - top_border], 
        [-space_between / 2, total_height / 2 - top_border - temp[1]], 
        [-temp[2] - space_between / 2, total_height / 2 - top_border - temp[1]]], 
        yellow, 
        gameDisplay, 
        Pivot=(-temp[2] / 2 - space_between / 2, total_height / 2 - top_border - temp[1] / 2), 
        name="short"
    ), 
    Polygon(
        [[-temp[2] - space_between / 2, total_height / 2 - top_border - temp[1] - space_between], 
        [-space_between / 2, total_height / 2 - top_border - temp[1] - space_between], 
        [-space_between / 2, -total_height / 2 + bottom_border + temp[1] + space_between], 
        [-temp[2] - space_between / 2, -total_height / 2 + bottom_border + temp[1] + space_between]], 
        green, 
        gameDisplay, 
        Pivot=(-temp[2] / 2 - space_between / 2, (bottom_border - top_border) / 2), 
        name="medium"
    ), 
    Polygon(
        [[-temp[2] - space_between / 2, -total_height / 2 + bottom_border], 
        [-space_between / 2, -total_height / 2 + bottom_border], 
        [-space_between / 2, -total_height / 2 + bottom_border + temp[1]], 
        [-temp[2] - space_between / 2, -total_height / 2 + bottom_border + temp[1]]], 
        orange, 
        gameDisplay, 
        Pivot=(-temp[2] / 2 - space_between / 2, -total_height / 2 + bottom_border + temp[1] / 2), 
        name="long"
    )
], [
    Polygon(
        [[temp[2] + space_between / 2, total_height / 2 - top_border],
        [space_between / 2, total_height / 2 - top_border],
        [space_between / 2, total_height / 2 - top_border - temp[0]],
        [temp[2] + space_between / 2, total_height / 2 - top_border - temp[0]]], 
        lime, 
        gameDisplay, 
        Pivot=(temp[2] / 2 + space_between / 2, total_height / 2 - top_border - temp[0] / 2), 
        name="one"
    ), 
    Polygon(
        [[temp[2] + space_between / 2, -total_height / 2 + bottom_border],
        [space_between / 2, -total_height / 2 + bottom_border],
        [space_between / 2, -total_height / 2 + bottom_border + temp[0]],
        [temp[2] + space_between / 2, -total_height / 2 + bottom_border + temp[0]]], 
        lime, 
        gameDisplay, 
        Pivot=(temp[2] / 2 + space_between / 2, -total_height / 2 + bottom_border + temp[0] / 2), 
        name="two"
    )
], [
    Polygon(
        [[total_width / 2 - side_border, total_height / 2 - top_border],
        [total_width / 2 - side_border - temp[2], total_height / 2 - top_border],
        [total_width / 2 - side_border - temp[2], total_height / 2 - top_border - temp[0]],
        [total_width / 2 - side_border, total_height / 2 - top_border - temp[0]]], 
        lime, 
        gameDisplay, 
        Pivot=(total_width / 2 - side_border - temp[2] / 2, total_height / 2 - top_border - temp[0] / 2), 
        name="yes"
    ), 
    Polygon(
        [[total_width / 2 - side_border, -total_height / 2 + bottom_border],
        [total_width / 2 - side_border - temp[2], -total_height / 2 + bottom_border],
        [total_width / 2 - side_border - temp[2], -total_height / 2 + bottom_border + temp[0]],
        [total_width / 2 - side_border, -total_height / 2 + bottom_border + temp[0]]], 
        lime, 
        gameDisplay, 
        Pivot=(total_width / 2 - side_border - temp[2] / 2, -total_height / 2 + bottom_border + temp[0] / 2), 
        name="no"
    )
]]

CharacterList = "abcdefghijklmnopqrstuvwxyz 0123456789(),.-"
font = [[50, ['l', (50, 0), (50, 40)], ['l', (50, 40), (40, 50)], ['l', (40, 50), (10, 50)], ['l', (10, 50), (0, 40)], 
            ['l', (0, 40), (0, 10)], ['l', (0, 10), (10, 0)], ['l', (10, 0), (40, 0)], ['l', (40, 0), (50, 10)]], #a
         [50, ['l', (0, 100), (0, 0)], ['l', (0, 0), (0, 10)], ['l', (0, 10), (10, 0)], ['l', (10, 0), (40, 0)], ['l', (40, 0), (50, 10)], 
            ['l', (50, 10), (50, 40)], ['l', (50, 40), (40, 50)], ['l', (40, 50), (10, 50)], ['l', (10, 50), (0, 40)]], #b
         [50, ['l', (50, 40), (40, 50)], ['l', (40, 50), (10, 50)], ['l', (10, 50), (0, 40)], ['l', (0, 40), (0, 10)], 
            ['l', (0, 10), (10, 0)], ['l', (10, 0), (40, 0)], ['l', (40, 0), (50, 10)]], #c
         [50, ['l', (50, 100), (50, 0)], ['l', (50, 10), (40, 0)], ['l', (40, 0), (10, 0)], ['l', (10, 0), (0, 10)], ['l', (0, 10), (0, 40)], ['l', (0, 40), (10, 50)], ['l', (10, 50), (40, 50)], ['l', (40, 50), (50, 40)]], #d
         [50, ['l', (0, 30), (50, 30)], ['l', (50, 30), (50, 40)], ['l', (50, 40), (40, 50)], ['l', (40, 50), (10, 50)], ['l', (10, 50), (0, 40)], ['l', (0, 40), (0, 10)], ['l', (0, 10), (10, 0)], ['l', (10, 0), (40, 0)], ['l', (40, 0), (50, 10)]], #e
         [40, ['l', (40, 90), (30, 100)], ['l', (30, 100), (20, 100)], ['l', (20, 100), (10, 90)], ['l', (10, 90), (10, 0)], ['l', (0, 50), (30, 50)]], #f
         [50, ['l', (50, 40), (40, 50)], ['l', (40, 50), (10, 50)], ['l', (10, 50), (0, 40)], ['l', (0, 40), (0, 10)], ['l', (0, 10), (10, 0)], ['l', (10, 0), (40, 0)], ['l', (40, 0), (50, 10)], ['l', (50, 40), (50, -40)], ['l', (50, -40), (40, -50)], ['l', (40, -50), (10, -50)], ['l', (10, -50), (0, -40)], ['l', (0, -40), (0, -30)]], #g
         [50, ['l', (0, 100), (0, 0)], ['l', (0, 40), (10, 50)], ['l', (10, 50), (40, 50)], ['l', (40, 50), (50, 40)], ['l', (50, 40), (50, 0)]], #h
         [0, ['l', (0, 0), (0, 50)], ['l', (0, 70), (0, 70)]], #i
         [10, ['l', (10, 50), (10, -40)], ['l', (10, -40), (0, -50)], ['l', (10, 70), (10, 70)]], #j
         [30, ['l', (0, 100), (0, 0)], ['l', (0, 30), (30, 50)], ['l', (0, 30), (30, 0)]], #k
         [0, ['l', (0, 100), (0, 0)]], #l
         [60, ['l', (0, 0), (0, 50)], ['l', (0, 40), (10, 50)], ['l', (10, 50), (20, 50)], ['l', (20, 50), (30, 40)], ['l', (30, 0), (30, 40)], 
            ['l', (30, 40), (40, 50)], ['l', (40, 50), (50, 50)], ['l', (50, 50), (60, 40)], ['l', (60, 0), (60, 40)]], #m
         [40, ['l', (0, 50), (0, 0)], ['l', (0, 40), (10, 50)], ['l', (10, 50), (30, 50)], ['l', (30, 50), (40, 40)], ['l', (40, 40), (40, 0)]], #n
         [50, ['l', (40, 50), (10, 50)], ['l', (10, 50), (0, 40)], ['l', (0, 40), (0, 10)], ['l', (0, 10), (10, 0)], ['l', (10, 0), (40, 0)], ['l', (40, 0), (50, 10)], ['l', (50, 10), (50, 40)], ['l', (50, 40), (40, 50)]], #o
         [50, ['l', (50, 40), (50, 10)], ['l', (50, 10), (40, 0)], ['l', (40, 0), (10, 0)], ['l', (10, 0), (0, 10)], ['l', (50, 40), (40, 50)], ['l', (40, 50), (10, 50)], ['l', (10, 50), (0, 40)], ['l', (0, 40), (0, -50)]], #p
         [50, ['l', (50, 40), (40, 50)], ['l', (40, 50), (10, 50)], ['l', (10, 50), (0, 40)], ['l', (0, 40), (0, 10)], ['l', (0, 10), (10, 0)], ['l', (10, 0), (40, 0)], ['l', (40, 0), (50, 10)], ['l', (50, 40), (50, -40)], ['l', (50, -40), (60, -50)]], #q
         [50, ['l', (0, 50), (0, 0)], ['l', (0, 40), (10, 50)], ['l', (10, 50), (40, 50)], ['l', (40, 50), (50, 40)]], #r
         [50, ['l', (50, 40), (40, 50)], ['l', (40, 50), (10, 50)], ['l', (10, 50), (0, 40)], ['l', (0, 40), (10, 30)], ['l', (10, 30), (40, 20)], ['l', (40, 20), (50, 10)], ['l', (50, 10), (40, 0)], ['l', (40, 0), (10, 0)], ['l', (10, 0), (0, 10)]], #s
         [40, ['l', (10, 100), (10, 10)], ['l', (10, 10), (20, 0)], ['l', (20, 0), (30, 0)], ['l', (30, 0), (40, 10)], ['l', (0, 50), (30, 50)]], #t
         [50, ['l', (0, 50), (0, 10)], ['l', (0, 10), (10, 0)], ['l', (10, 0), (40, 0)], ['l', (40, 0), (50, 10)], ['l', (50, 50), (50, 0)]], #u
         [50, ['l', (0, 50), (25, 0)], ['l', (25, 0), (50, 50)]], #v
         [60, ['l', (0, 50), (20, 0)], ['l', (20, 0), (30, 30)], ['l', (30, 30), (40, 0)], ['l', (40, 0), (60, 50)]], #w
         [50, ['l', (0, 50), (50, 0)], ['l', (50, 50), (0, 0)]], #x
         [50, ['l', (0, 50), (0, 10)], ['l', (0, 10), (10, 0)], ['l', (10, 0), (40, 0)], ['l', (40, 0), (50, 10)], ['l', (50, 50), (50, -40)], ['l', (50, -40), (40, -50)], ['l', (40, -50), (10, -50)], ['l', (10, -50), (0, -40)]], #y
         [50, ['l', (0, 50), (50, 50)], ['l', (50, 50), (0, 0)], ['l', (0, 0), (50, 0)]], #z
         [30], #space
         [50, ['l', (50, 90), (40, 100)], ['l', (40, 100), (10, 100)], ['l', (10, 100), (0, 90)], ['l', (0, 90), (0, 10)], ['l', (0, 10), (10, 0)], ['l', (40, 0), (10, 0)], ['l', (40, 0), (50, 10)], ['l', (50, 10), (50, 90)], ['l', (50, 80), (0, 20)]], #0
         [40, ['l', (0, 80), (20, 100)], ['l', (20, 100), (20, 0)], ['l', (0, 0), (40, 0)]], #1
         [50, ['l', (0, 80), (0, 90)], ['l', (0, 90), (10, 100)], ['l', (10, 100), (40, 100)], ['l', (40, 100), (50, 90)], ['l', (50, 90), (50, 60)], ['l', (50, 60), (0, 10)], ['l', (0, 10), (0, 0)], ['l', (0, 0), (50, 0)], ['l', (50, 0), (50, 10)]], #2
         [50, ['l', (0, 80), (0, 90)], ['l', (0, 90), (10, 100)], ['l', (10, 100), (40, 100)], ['l', (40, 100), (50, 90)], ['l', (50, 90), (50, 60)], ['l', (50, 60), (40, 50)], ['l', (40, 50), (20, 50)], ['l', (40, 50), (50, 40)], ['l', (50, 40), (50, 10)], ['l', (50, 10), (40, 0)], ['l', (40, 0), (10, 0)], ['l', (10, 0), (0, 10)], ['l', (0, 10), (0, 20)], ['l', (10, 50), (20, 50)]], #3
         [50, ['l', (0, 100), (0, 50)], ['l', (0, 50), (50, 50)], ['l', (50, 100), (50, 0)]], #4
         [50, ['l', (50, 100), (0, 100)], ['l', (0, 100), (0, 50)], ['l', (0, 50), (40, 50)], ['l', (40, 50), (50, 40)], ['l', (50, 40), (50, 10)], ['l', (50, 10), (40, 0)], ['l', (40, 0), (10, 0)], ['l', (10, 0), (0, 10)]], #5
         [50, ['l', (50, 90), (40, 100)], ['l', (40, 100), (10, 100)], ['l', (10, 100), (0, 90)], ['l', (0, 90), (0, 10)], ['l', (0, 10), (10, 0)], ['l', (10, 0), (40, 0)], ['l', (40, 0), (50, 10)], ['l', (50, 10), (50, 40)], ['l', (50, 40), (40, 50)], ['l', (40, 50), (10, 50)], ['l', (10, 50), (0, 40)]], #6
         [50, ['l', (0, 100), (50, 100)], ['l', (50, 100), (10, 0)], ['l', (40, 50), (20, 50)]], #7
         [50, ['l', (50, 90), (40, 100)], ['l', (40, 100), (10, 100)], ['l', (10, 100), (0, 90)], ['l', (0, 90), (0, 60)], ['l', (0, 60), (10, 50)], ['l', (10, 50), (0, 40)], ['l', (0, 40), (0, 10)], ['l', (0, 10), (10, 0)], ['l', (10, 0), (40, 0)], ['l', (40, 0), (50, 10)], ['l', (50, 10), (50, 40)], ['l', (50, 40), (40, 50)], ['l', (40, 50), (50, 60)], ['l', (50, 60), (50, 90)], ['l', (40, 50), (10, 50)]], #8
         [50, ['l', (50, 90), (40, 100)], ['l', (40, 100), (10, 100)], ['l', (10, 100), (0, 90)], ['l', (0, 90), (0, 60)], ['l', (0, 60), (10, 50)], ['l', (10, 50), (40, 50)], ['l', (40, 50), (50, 60)], ['l', (50, 90), (50, 0)]], #9  
         [20, ['l', (20, 100), (10, 100)], ['l', (10, 100), (0, 90)], ['l', (0, 90), (0, 10)], ['l', (0, 10), (10, 0)], ['l', (10, 0), (20, 0)]], #(
         [20, ['l', (0, 100), (10, 100)], ['l', (10, 100), (20, 90)], ['l', (20, 90), (20, 10)], ['l', (20, 10), (10, 0)], ['l', (10, 0), (0, 0)]], #)
         [3, ['l', (3, 0), (3, -10)], ['l', (3, -10), (0, -20)]], #,
         [2, ['l', (0, 0), (0, 2)], ['l', (0, 2), (2, 2)], ['l', (2, 2), (2, 0)], ['l', (2, 0), (0, 0)]], #.
         [30, ['l', (0, 50), (30, 50)]], #-
         ]

def polygon_for_line(point_1, point_2, width, smoothness=4):
    radius = float(width)/2
    if point_1[0] == point_2[0]:
        x_min = point_1[0]
        y_min = min(point_1[1], point_2[1])
        x_max = point_1[0]
        y_max = max(point_1[1], point_2[1])
        angle = math.pi/2
    else:
        if point_1[0] < point_2[0]:
            x_min = point_1[0]
            y_min = point_1[1]
            x_max = point_2[0]
            y_max = point_2[1]
        else:
            x_max = point_1[0]
            y_max = point_1[1]
            x_min = point_2[0]
            y_min = point_2[1]
        angle = math.atan((y_max-y_min)/(x_max-x_min))
    
    polygon = []
    
    angle_modifier = -math.pi/2
    for i in range(smoothness+1):
        polygon.append((x_max + radius * math.cos(angle + angle_modifier), y_max + radius * math.sin(angle + angle_modifier)))
        angle_modifier += math.pi/smoothness
    angle_modifier -= math.pi/smoothness
    for i in range(smoothness+1):
        polygon.append((x_min + radius * math.cos(angle + angle_modifier), y_min + radius * math.sin(angle + angle_modifier)))
        angle_modifier += math.pi/smoothness
    
    return polygon

def translate(point, reference, width, height, italics, angle):
    return (reference[0] + (point[0] + italics * point[1]) * math.cos(angle) * width + point[1] * math.sin(angle) * height, 
            reference[1] - (point[0] + italics * point[1]) * math.sin(angle) * width + point[1] * math.cos(angle) * height)

def letter_hitbox(data, point, weight, width, height, italics=0.0, angle=0, smoothness=3):
    convertedAngle = - angle * math.pi / 180.0
    hitbox = []
    for i in data:
        if i != data[0]: #data[0] = width
            if i[0] == "l":
                hitbox.append(polygon_for_line(translate(i[1], point, width, -height, italics, convertedAngle), 
                                               translate(i[2], point, width, -height, italics, convertedAngle), 
                                               weight))
    return hitbox

class Text_Engine(object):
    def __init__(self, surface):
        self.surface = surface
    
    def type(self, text, font, point, width, height, color, weight, angle=0, space_between_letters=0, italics=0.0):
        cangle = angle * math.pi/180.0
        temp = -float(space_between_letters)
        word_hitbox = []
        for i in text:
            temp += font[CharacterList.index(i)][0] * width
            temp += space_between_letters
        current_distance = -temp/2
        for i in text:
            for j in letter_hitbox(font[CharacterList.index(i)], (point[0] + current_distance*math.cos(cangle), point[1] - current_distance*math.sin(cangle)), weight, width, height, italics=italics, angle=-angle):
                word_hitbox.append(j)
            current_distance += font[CharacterList.index(i)][0] * width + space_between_letters
        for polygon in word_hitbox:
            pygame.draw.polygon(self.surface, color, polygon)

TE = Text_Engine(gameDisplay)

arrow_up = Polygon(
    [
        (-30, 10), 
        (30, 10), 
        (0, 80)
    ], 
    gray, 
    gameDisplay, 
)

arrow_down = Polygon(
    [
        (-30, -10), 
        (30, -10), 
        (0, -80)
    ], 
    gray, 
    gameDisplay, 
)

def point_above_line(point, line): #definition of "above": y above line, or if vertical, then x value greater
    #point format: (x, y)
    #line format: [(x1, y1), (x2, y2)]
    if line[0][0] == line[1][0]:
        return point[0] > line[0][0]
    elif point[0] == line[0][0]:
        return point[1] > line[0][1]
    elif point[0] > line[0][0]:
        return (point[1]-line[0][1])/(point[0]-line[0][0]) > (line[1][1]-line[0][1])/(line[1][0]-line[0][0])
    else:
        return (point[1]-line[0][1])/(point[0]-line[0][0]) < (line[1][1]-line[0][1])/(line[1][0]-line[0][0])

def point_on_line(point, line):
    if abs(line[1][0]-line[0][0]) == 0:
        return abs(line[0][0] - point[0]) < 0.01
    elif abs(point[0]-line[0][0]) == 0:
        return False
    else:
        return (point[1]-line[0][1])/(point[0]-line[0][0]) == (line[1][1]-line[0][1])/(line[1][0]-line[0][0])

def intersect(line_1, line_2):
    if (max(line_1[0][0], line_1[1][0]) < min(line_2[0][0], line_2[1][0])) or (min(line_1[0][0], line_1[1][0]) > max(line_2[0][0], line_2[1][0])) or (max(line_1[0][1], line_1[1][1]) < min(line_2[0][1], line_2[1][1])) or (min(line_1[0][1], line_1[1][1]) > max(line_2[0][1], line_2[1][1])):
        return False #legit zero chance they intersect
    
    temp_1 = line_1[1][0]
    temp_2 = line_2[1][0]
    if line_1[0][0] == line_1[1][0]:
        temp_1 += 0.01
    if line_2[0][0] == line_2[1][0]:
        temp_2 += 0.01
    lein_1 = [line_1[0], (temp_1, line_1[1][1])]
    lein_2 = [line_2[0], (temp_2, line_2[1][1])]
    
    if point_on_line(lein_1[0], lein_2) or point_on_line(lein_1[1], lein_2) or point_on_line(lein_2[0], lein_1) or point_on_line(lein_2[1], lein_1):
        return False #if any of the points are on the line
    else:
        return (point_above_line(lein_1[0], lein_2) != point_above_line(lein_1[1], lein_2)) and (point_above_line(lein_2[0], lein_1) != point_above_line(lein_2[1], lein_1))

def point_inside_polygon(point, polygon, accuracy=6): #we want the inside-ness to be the same for every line
    #solution - very scuffed - kinda LOLLY - but should work
    min_x = 10000000
    min_y = 10000000
    max_x = -10000000
    max_y = -10000000
    for i in polygon:
        min_x = min(min_x, i[0])
        max_x = max(max_x, i[0])
        min_y = min(min_y, i[1])
        max_y = max(max_y, i[1])
    length = math.sqrt((max_x-min_x)*(max_x-min_x)+(max_y-min_y)*(max_y-min_y))
    
    for i in range(accuracy): #go over "accuracy" radial lines
        temp = 0
        
        for j in range(len(polygon)): #add 1 if intersects line, 0.5 for each endpoint it touches
            radial_line = [point, (point[0] + length*math.cos(2*math.pi/accuracy * i), point[1] + length*math.sin(2*math.pi/accuracy * i))]
            if point_on_line(polygon[j], radial_line):
                temp += 1
            if point_on_line(polygon[(j+1) % len(polygon)], radial_line):
                temp += 1
            if intersect(radial_line, 
                         [polygon[j], polygon[(j+1) % len(polygon)]]):
                temp += 2
            #see if the radial line intersects any of the hitbox lines
        
        if temp % 4 != 2:
            return False
    return True

run = True

from networktables import NetworkTables
import logging
logging.basicConfig(level=logging.DEBUG)

NetworkTables.initialize(server=roboRio_server) # RoboRio
smartDashboard = NetworkTables.getTable("SmartDashboard")

for i in grid:
    for j in i:
        j.setPos((gameDisplay.get_width() / 2, gameDisplay.get_height() - total_height / 2))

arrow_up.setPos((530, 100))
arrow_down.setPos((530, 100))

mousedownlast = False
mouseclicked = False

indices = [0, 0, 0, 0, 0]

time_wait = 0.0

while run:
    mouseclicked = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouseclicked = not mousedownlast
            mousedownlast = True
        if event.type == pygame.MOUSEBUTTONUP:
            mouseclicked = False
            mousedownlast = False
    
    gameDisplay.fill(background_color)
    
    for i in range(1, len(grid)):
        for j in range(len(grid[i])):
            if (mouseclicked):
                if ((grid[i][j].hitbox[0][0] < pygame.mouse.get_pos()[0]) == (pygame.mouse.get_pos()[0] < grid[i][j].hitbox[2][0])):
                    if ((grid[i][j].hitbox[0][1] < pygame.mouse.get_pos()[1]) == (pygame.mouse.get_pos()[1] < grid[i][j].hitbox[2][1])):
                        indices[i - 1] = j
    
    indices[2] = 0 # Override because can't do double cone
    
    for i in range(len(grid)):
        if (i != 0):
            TE.type(categories[i - 1], font, (grid[i][0].pivotPoint[0], gameDisplay.get_height() - total_height + (top_border + 25) / 2), 0.25, 0.25, white, 2, space_between_letters=6)
        for j in range(len(grid[i])):
            temp = grid[i][j].Color
            if (i != 0 and indices[i - 1] != j):
                grid[i][j].Color = gray
            grid[i][j].draw()
            grid[i][j].Color = temp
            if (i != 0):
                TE.type(grid[i][j].name, font, grid[i][j].pivotPoint, 0.25, 0.25, black, 2, space_between_letters=6)
    
    arrow_up.draw()
    arrow_down.draw()
    
    if (mouseclicked and point_inside_polygon(pygame.mouse.get_pos(), arrow_up.hitbox)):
        time_wait += 0.5
        if (time_wait > 5):
            time_wait = 5.0
    
    if (mouseclicked and point_inside_polygon(pygame.mouse.get_pos(), arrow_down.hitbox)):
        time_wait -= 0.5
        if (time_wait < 0):
            time_wait = 0.0
    
    indices[4] = round(time_wait, 1)
    
    TE.type("toqibb", font, (180, 140), 1.2, 1.2, black, 6, space_between_letters=12)
    TE.type("auto selector", font, (360, 190), 0.4, 0.4, black, 2, space_between_letters=6)
    TE.type(str(round(time_wait, 1)), font, (680, 180), 1.6, 1.6, black, 8, space_between_letters=14)
    
    smartDashboard.putNumberArray("Auto Data", indices)
    
    pygame.display.update()
    clock.tick(10)

pygame.quit()