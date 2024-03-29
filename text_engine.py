
import math

import pygame


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


class Text_Engine(object):
    def __init__(self, surface):
        self.surface = surface
    
    def type(self, text: str, font, point, width, height, color, weight, angle=0, space_between_letters: float=0, italics=0.0):
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
