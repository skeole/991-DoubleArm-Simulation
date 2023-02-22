import pygame

import sys
sys.path.insert(1, '/Users/shaankeole/Downloads/Coding/PythonProjects/Pygame/Game')

import Robot as Robot
import Colors as Colors

pygame.init()
gameDisplay = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

background_color = Colors.white

robot = Robot.New_Robot(gameDisplay)
robot.update_hitbox()

acc = 6
max_count = 5

run = True
pause = False
target_x = 200.0
target_y = 0.0
max_vel = 10.0
mouse_down = False
last_time = False
ccu = True

p_last = False
c_last = False

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_down = True
        if event.type == pygame.MOUSEBUTTONUP:
            mouse_down = False

    if (pygame.key.get_pressed()[pygame.K_p] and not p_last):
        pause = not pause
        p_last = True
    elif ((not pygame.key.get_pressed()[pygame.K_p]) and p_last):
        p_last = False
        
    if (pygame.key.get_pressed()[pygame.K_c] and not c_last):
        ccu = not ccu
        c_last = True
    elif (not pygame.key.get_pressed()[pygame.K_c] and c_last):
        c_last = False
        
    if (not pause):
        if pygame.key.get_pressed()[pygame.K_RIGHT]:
            target_x += 5
        if pygame.key.get_pressed()[pygame.K_LEFT]:
            target_x -= 5
            
        if pygame.key.get_pressed()[pygame.K_UP]:
            target_y += 5
        if pygame.key.get_pressed()[pygame.K_DOWN]:
            target_y -= 5
    
        if (mouse_down and (
            (pygame.mouse.get_pos()[0] - robot.target_xy.x) * (pygame.mouse.get_pos()[0] - robot.target_xy.x) + (pygame.mouse.get_pos()[1] - robot.target_xy.y) * (pygame.mouse.get_pos()[1] - robot.target_xy.y) < 70 * 70
            or last_time)):
            target_x = pygame.mouse.get_pos()[0] - 272
            target_y = 167 - pygame.mouse.get_pos()[1]
            last_time = True
        else:
            last_time = False
        
        robot.setTargetAngles(target_x, target_y, ccu)
        
        robot.update_hitbox() #you have to update hitbox whenever you move

        gameDisplay.fill(background_color)
        
        pygame.draw.rect(gameDisplay, Colors.green, (0, 500, 800, 100))
        robot.draw()

        pygame.display.update()
    clock.tick(30)
    
    print("\n\n\n")
    print("current x: " + str(round((robot.target_xy.x - 272) * (32.0 / 231.0), 1)))
    print("current y: " + str(round((167-robot.target_xy.y) * (32.0 / 231.0), 1)))

pygame.quit()
