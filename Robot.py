import math


import Obj_Tem as Object_Template
import Spec_Shap as Spec_Shap
import Colors as Colors

class New_Robot(object):

    def __init__(self, surface):
        
        self.position = [100, 0]
        self.angles = [0, 0]
        
        self.hitbox = []
        
        self.x = 200
        self.y = 500
        self.angle = 0
        
        self.first_arm_start_pos = [72, 333]
        
        self.frame = Object_Template.New_Object([[ # lol
                                                    (75, -343), 
                                                    (83, -330), 
                                                    (-95, -227), 
                                                    (-95, -53), 
                                                    (125, -53), 
                                                    (125, -16), 
                                                    (98, -16), 
                                                    (98, -0), 
                                                    (-98, -0), 
                                                    (-98, -16), 
                                                    (-125, -16), 
                                                    (-125, -53), 
                                                    (-103, -53), 
                                                    (-103, -240)
                                                ]], 
                                                [Colors.black], surface)
        
        self.first_arm = Object_Template.New_Object([Spec_Shap.polygon_for_line((0, 0), (231, 0), 15)], 
                                                [Colors.red], surface)
        
        self.second_arm = Object_Template.New_Object([Spec_Shap.polygon_for_line((0, 0), (212, 0), 15)], 
                                                [Colors.blue], surface)
        
        self.target_xy = Object_Template.New_Object([Spec_Shap.polygon_for_line((0, 0), (0, 0), 150)], 
                                                [Colors.green], surface)
        
        self.ListOfObjects = [self.frame, self.first_arm, self.second_arm, self.target_xy]
    
    def setTargetAngles(self, target_x, target_y, ccu):

        if (abs(target_x) < 0.25):
            target_x = 0.25

        radius = math.sqrt(target_x * target_x + target_y * target_y)
        
        if (radius < 1.2 * (19)):
            target_x *= 1.2 * (19) / radius
            target_y *= 1.2 * (19) / radius
            radius = 1.2 * (19)
            
        elif (radius > 0.99 * (443)):
            target_x *= 0.99 * (443) / radius
            target_y *= 0.99 * (443) / radius
            radius = 0.99 * (443)

        angle = math.atan(target_y / target_x) * 180.0 / math.pi;
        if (target_x < 0):
            if (angle > 0):
                angle -= 180
            else:
                angle += 180

        first_angle = math.acos((radius * radius + 231 * 231 - 212 * 212) / (2.0 * 231 * radius)) * 180.0 / math.pi
        second_angle = math.acos((radius * radius + 212 * 212 - 231 * 231) / (2.0 * 212 * radius)) * 180.0 / math.pi
        
        first = 0 
        second = 0
        if (ccu):
            first = angle - first_angle
            second = angle + second_angle
        else:
            first = angle + first_angle
            second = angle - second_angle
        self.angles = [first, second]
    
    def align(self, x, y):
        self.frame.x = x
        self.frame.y = y
        
        self.first_arm.x = x + 72
        self.first_arm.y = y - 333
        self.first_arm.angle = 0 - self.angles[0] * math.pi / 180.0
        
        self.second_arm.x = x + 72 + math.cos(self.angles[0] * math.pi / 180.0) * 231
        self.second_arm.y = y - 333 - math.sin(self.angles[0] * math.pi / 180.0) * 231
        self.second_arm.angle = 0 - self.angles[1] * math.pi / 180.0
        
        self.target_xy.x = x + 72 + math.cos(self.angles[0] * math.pi / 180.0) * 231 + math.cos(self.angles[1] * math.pi / 180.0) * 212
        self.target_xy.y = y - 333 - math.sin(self.angles[0] * math.pi / 180.0) * 231 - math.sin(self.angles[1] * math.pi / 180.0) * 212
    
    def update_hitbox(self):
        self.align(self.x, self.y)  
        self.hitbox = []
        for obj in self.ListOfObjects:
            obj.update_hitbox()
            for polygon in obj.hitbox:
                self.hitbox.append(polygon)
    
    def draw(self):
        self.align(self.x, self.y)
        for i in range(len(self.ListOfObjects) - 1):
            self.ListOfObjects[i].draw()