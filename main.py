proximal_length = 32
distal_length = 15

display_size = (1000, 800)

pixels_per_inch = display_size[0] * 0.01

roboRio_server = "172.22.11.2"

robot_polygon : list[tuple[float, float]] = [ # in inches
    (33.25, 7), 
    (34.5, 5.75), 
    (34.5, 3.25), 
    (33.25, 2), 
    (30.625, 2), 
    (30.625, 1.171573), 
    (29.453427, 0), 
    (27.796573, 0), 
    (26.625, 1.171573), 
    (26.625, 2), 
    (7.875, 2), 
    (7.875, 1.171573), 
    (6.703427, 0), 
    (5.046573, 0), 
    (3.875, 1.171573), 
    (3.875, 2), 
    (1.25, 2), 
    (0, 3.25), 
    (0, 5.75), 
    (1.25, 7), 
    (3.25, 7), 
    (3.25, 33.130295), 
    (27.663629, 47.270182), 
    (28.666004, 45.539504), 
    (4.25, 31.398242), 
    (4.25, 7)
]

first_pivot : tuple[float, float] = (27.278627, 45.825413)

proximal_polygon : list[tuple[float, float]] = [
    (-1, -1), 
    (proximal_length - 3, -1), 
    (proximal_length - 3, 1), 
    (-1, 1)
    
]

second_pivot : tuple[float, float] = (proximal_length - 4, 0)

distal_polygon : list[tuple[float, float]] = [
    (0.792893, 1.414214), 
    (2, -1), 
    (distal_length - 2, -1), 
    (distal_length - 2, -2.5), 
    (-2, -2.5), 
    (-2, -1), 
    (-0.792893, 1.414214)
]

claw_polygon : list[tuple[float, float]] = [
    (distal_length - 2, -1), 
    (distal_length - 5, -1), 
    (distal_length - 5, -0.75), 
    (distal_length + 7.739619, -0.75), 
    (distal_length + 7.739619, -2.75), 
    (distal_length - 2.4174, -2.75), 
    (distal_length - 2.4174, -3), 
    (distal_length - 2.629998, -3), 
    (distal_length - 2.629998, -3.11811), 
    (distal_length - 2.728423, -3.11811), 
    (distal_length - 2.728423, -4.535433), 
    (distal_length - 3.004014, -4.870079), 
    (distal_length - 3.830785, -4.870079), 
    (distal_length - 4.106376, -4.535433), 
    (distal_length - 4.106376, -3.118110), 
    (distal_length - 4.204801, -3.118110), 
    (distal_length - 4.204801, -3), 
    (distal_length - 4.4174, -3), 
    (distal_length - 4.4174, -2.565), 
    (distal_length - 4.6365, -2.565), 
    (distal_length - 4.6365, -2.5), 
    (distal_length - 2, -2.5)
]

import math
import pygame

class Polygon(object):
    
    def __init__(self, Points, Color, surface, scale=1.0, Pivot=(0, 0)):
        
        self.Points = Points
        self.Color = Color
        self.Pivot = Pivot # special points that are also tracked
        self.scale = scale
        
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
yellow = (153, 153, 0)
lime = (76, 153, 0)


pygame.init()
gameDisplay = pygame.display.set_mode(display_size)
pygame.display.set_caption('DoubleArm Display')
clock = pygame.time.Clock()

background_color = white

Polygons = [
    Polygon(robot_polygon, black, gameDisplay, scale=pixels_per_inch, Pivot=first_pivot), 
    Polygon(proximal_polygon, red, gameDisplay, scale=pixels_per_inch, Pivot=second_pivot), 
    Polygon(distal_polygon, blue, gameDisplay, scale=pixels_per_inch), 
    Polygon(claw_polygon, black, gameDisplay, scale=pixels_per_inch)
]

def draw_polygon_alpha(color, points):
    lx, ly = zip(*points)
    min_x, min_y, max_x, max_y = min(lx), min(ly), max(lx), max(ly)
    target_rect = pygame.Rect(min_x, min_y, max_x - min_x, max_y - min_y)
    shape_surf = pygame.Surface(target_rect.size, pygame.SRCALPHA)
    pygame.draw.polygon(shape_surf, color, [(x - min_x, y - min_y) for x, y in points])
    gameDisplay.blit(shape_surf, target_rect)

def drawPolygons(pos, current_angles, target_angles):
    Polygons[0].rotateTo(0)
    Polygons[0].setPos(pos)
    
    Polygons[1].rotateTo(current_angles[0])
    Polygons[1].setPos(Polygons[0].pivotPoint)
    
    Polygons[2].rotateTo(current_angles[1])
    Polygons[2].setPos(Polygons[1].pivotPoint)
    
    Polygons[3].rotateTo(current_angles[1])
    Polygons[3].setPos(Polygons[1].pivotPoint)
    
    for i in Polygons:
        i.draw()
    
    Polygons[1].rotateTo(target_angles[0])
    Polygons[1].setPos(Polygons[0].pivotPoint)
    
    Polygons[2].rotateTo(target_angles[1])
    Polygons[2].setPos(Polygons[1].pivotPoint)
    
    Polygons[3].rotateTo(target_angles[1])
    Polygons[3].setPos(Polygons[1].pivotPoint)
    
    Polygons[1].update_hitbox()
    Polygons[2].update_hitbox()
    Polygons[3].update_hitbox()
    
    draw_polygon_alpha(clear_red, Polygons[1].hitbox)
    draw_polygon_alpha(clear_blue, Polygons[2].hitbox)
    draw_polygon_alpha(clear_black, Polygons[3].hitbox)

def mouse_pos_to_inches(mousePos):
    return (
        (mousePos[0] - Polygons[0].pivotPoint[0]) / pixels_per_inch, 
        (Polygons[0].pivotPoint[1] - mousePos[1]) / pixels_per_inch
    )

def pointToAngles(coordinates, ccu=True):
        
    x = coordinates[0]
    y = coordinates[1]

    if (abs(x) < 0.25):
        x = 0.25

    radius = math.sqrt(x * x + y * y)
    
    if (radius < 1.2 * (proximal_length - distal_length - 11.751984)):
        x *= 1.2 * (19) / radius
        y *= 1.2 * (19) / radius
        radius = 1.2 * (proximal_length - distal_length - 11.751984)
        
    elif (radius > 0.99 * (proximal_length + distal_length + 3.751984)):
        x *= 0.99 * (443) / radius
        y *= 0.99 * (443) / radius
        radius = 0.99 * (proximal_length + distal_length + 3.751984)

    angle = math.atan(y / x) * 180.0 / math.pi;
    if (x < 0):
        if (angle > 0):
            angle -= 180
        else:
            angle += 180

    first_angle = math.acos((radius * radius + (proximal_length - 4) * (proximal_length - 4) - (distal_length + 7.751984) * (distal_length + 7.751984)) / (2.0 * (proximal_length - 4) * radius)) * 180.0 / math.pi
    second_angle = math.acos((radius * radius + (distal_length + 7.751984) * (distal_length + 7.751984) - (proximal_length - 4) * (proximal_length - 4)) / (2.0 * (distal_length + 7.751984) * radius)) * 180.0 / math.pi
    
    if (ccu):
        return [angle - first_angle, angle + second_angle]
    else:
        return [angle + first_angle, angle - second_angle]

def anglesToPoint(angles):
    return [
        (proximal_length - 4) * math.cos(math.pi / 180.0 * angles[0]) + (distal_length + 7.751984) * math.cos(math.pi / 180.0 * angles[1]), 
        (proximal_length - 4) * math.sin(math.pi / 180.0 * angles[0]) + (distal_length + 7.751984) * math.sin(math.pi / 180.0 * angles[1])
    ]

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


from networktables import NetworkTables
import logging
logging.basicConfig(level=logging.DEBUG)

NetworkTables.initialize(server=roboRio_server) # RoboRio
smartDashboard = NetworkTables.getTable("SmartDashboard")

angles = [0, 0]
run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    gameDisplay.fill(background_color)
    
    pygame.draw.rect(gameDisplay, green, (0, int(display_size[1] * 0.85), display_size[0], display_size[1]))
    current_angles = (smartDashboard.getNumber("Current Angle 1", -440), smartDashboard.getNumber("Current Angle 2", 80))
    target_angles = (smartDashboard.getNumber("Target 1st Angle", -60), smartDashboard.getNumber("Target 2nd Angle", 60))
    drawPolygons(
        (display_size[0] * 0.1, display_size[1] * 0.85), 
        current_angles, 
        target_angles
    )
    
    if (int(current_angles[0]) != -440):
        point = anglesToPoint(current_angles)
        TE.type("current position is (" + str(round(point[0], 1)) + ", " + str(round(point[1], 1)) + ")", font, (int(display_size[0] * 0.5), 80), 0.5, 0.5, black, 4, space_between_letters=6)
        
        point = anglesToPoint(target_angles)
        TE.type("target position is (" + str(round(point[0], 1)) + ", " + str(round(point[1], 1)) + ")", font, (int(display_size[0] * 0.5), 140), 0.5, 0.5, black, 4, space_between_letters=6)
    else: # no reading from smartdashboard
        TE.type("could not connect to smart dashboard", font, (int(display_size[0] * 0.5), 80), 0.4, 0.4, black, 3, space_between_letters=5)

    pygame.display.update()
    clock.tick(20)

pygame.quit()
