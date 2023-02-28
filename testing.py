import math
import pygame

proximal_length = 32
distal_length = 15

display_size = (1000, 800)

pixels_per_inch = display_size[0] * 0.01

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

angles = [-80.0, 80.0]
run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
    if pygame.key.get_pressed()[pygame.K_w]:
        angles[0] += 1.5
    if pygame.key.get_pressed()[pygame.K_s]:
        angles[0] -= 1.5
        
    if pygame.key.get_pressed()[pygame.K_UP]:
        angles[1] += 1.5
    if pygame.key.get_pressed()[pygame.K_DOWN]:
        angles[1] -= 1.5
    
    gameDisplay.fill(background_color)
    
    pygame.draw.rect(gameDisplay, green, (0, int(display_size[1] * 0.85), display_size[0], display_size[1]))
    drawPolygons(
        (display_size[0] * 0.1, display_size[1] * 0.85), 
        angles, 
        pointToAngles(mouse_pos_to_inches(pygame.mouse.get_pos()))
    )

    pygame.display.update()
    clock.tick(40)

pygame.quit()
