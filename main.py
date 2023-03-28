import logging
from networktables import NetworkTables
from constants import *
from shared import *
from text_engine import *
from polygon import Polygon

import pygame

pygame.init()
gameDisplay = pygame.display.set_mode(
    (display_size_left[0] + display_size_right[0], display_size_left[1]))
pygame.display.set_caption('Toqibb Display')
clock = pygame.time.Clock()

background_color = white

auto_chooser_grid = getAutoChooserGrid(gameDisplay)

polygons = [
    Polygon(robot_polygon, black, gameDisplay,
            scale=pixels_per_inch, pivot=first_pivot),
    Polygon(proximal_polygon, red, gameDisplay,
            scale=pixels_per_inch, pivot=second_pivot),
    Polygon(distal_polygon, blue, gameDisplay, scale=pixels_per_inch),
    Polygon(claw_polygon, black, gameDisplay, scale=pixels_per_inch)
]


def draw_polygon_alpha(color, points):
    lx, ly = zip(*points)
    min_x, min_y, max_x, max_y = min(lx), min(ly), max(lx), max(ly)
    target_rect = pygame.Rect(min_x, min_y, max_x - min_x, max_y - min_y)
    shape_surf = pygame.Surface(target_rect.size, pygame.SRCALPHA)
    pygame.draw.polygon(shape_surf, color, [
                        (x - min_x, y - min_y) for x, y in points])
    gameDisplay.blit(shape_surf, target_rect)


def drawPolygons(pos, current_angles, target_angles):
    polygons[0].rotateTo(0)
    polygons[0].setPos(pos)

    polygons[1].rotateTo(current_angles[0])
    polygons[1].setPos(polygons[0].pivotPoint)

    polygons[2].rotateTo(current_angles[1])
    polygons[2].setPos(polygons[1].pivotPoint)

    polygons[3].rotateTo(current_angles[1])
    polygons[3].setPos(polygons[1].pivotPoint)

    for i in polygons:
        i.draw()

    polygons[1].rotateTo(target_angles[0])
    polygons[1].setPos(polygons[0].pivotPoint)

    polygons[2].rotateTo(target_angles[1])
    polygons[2].setPos(polygons[1].pivotPoint)

    polygons[3].rotateTo(target_angles[1])
    polygons[3].setPos(polygons[1].pivotPoint)

    polygons[1].update_hitbox()
    polygons[2].update_hitbox()
    polygons[3].update_hitbox()

    draw_polygon_alpha(clear_red, polygons[1].hitbox)
    draw_polygon_alpha(clear_blue, polygons[2].hitbox)
    draw_polygon_alpha(clear_black, polygons[3].hitbox)


def mouse_pos_to_inches(mousePos):
    return (
        (mousePos[0] - polygons[0].pivotPoint[0]) / pixels_per_inch,
        (polygons[0].pivotPoint[1] - mousePos[1]) / pixels_per_inch
    )


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


logging.basicConfig(level=logging.DEBUG)

NetworkTables.initialize(server=robot_ip)  # RoboRio
smartDashboard = NetworkTables.getTable("SmartDashboard")

for i in auto_chooser_grid:
    for j in i:
        j.setPos((display_size_left[0] / 2,
                 display_size_left[1] - total_height / 2))

arrow_up.setPos((530, 100))
arrow_down.setPos((530, 100))

mousedownlast = False
mouseclicked = False

indices = [0, 0, 0, 0, 0]

time_wait = 0.0

angles = [0, 0]
run = True

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

    # double arm
    pygame.draw.rect(gameDisplay, green, (display_size_left[0] + 0, int(
        display_size_right[1] * 0.85), display_size_left[0] + display_size_right[0], display_size_right[1]))
    current_angles = (smartDashboard.getNumber(
        "Current Angle 1", -440), smartDashboard.getNumber("Current Angle 2", 80))
    target_angles = (smartDashboard.getNumber(
        "Target 1st Angle", -60), smartDashboard.getNumber("Target 2nd Angle", 60))
    claw_state = smartDashboard.getString("claw state", "bwerbhwj")
    if (claw_state == "intake"):
        polygons[3].color = orange
    elif (claw_state == "outtake"):
        polygons[3].color = green
    else:
        polygons[3].color = black
    drawPolygons(
        (display_size_left[0] + display_size_right[0]
         * 0.1, display_size_right[1] * 0.85),
        current_angles,
        target_angles
    )

    if (int(current_angles[0]) != -440):
        point = current_angles  # anglesToPoint(current_angles)
        TE.type("current position is (" + str(round(point[0], 1)) + ", " + str(round(point[1], 1)) + ")", font, (display_size_left[0] + int(display_size_right[0] * 0.5), int(
            display_size_right[1] * 0.1)), display_size_right[1] / 1600, display_size_right[1] / 1600, black, 2, space_between_letters=display_size_right[1] / 133.33)

        point = target_angles  # anglesToPoint(target_angles)
        TE.type("target position is (" + str(round(point[0], 1)) + ", " + str(round(point[1], 1)) + ")", font, (display_size_left[0] + int(display_size_right[0] * 0.5), int(
            display_size_right[1] * 0.175)), display_size_right[1] / 1600, display_size_right[1] / 1600, black, 2, space_between_letters=display_size_right[1] / 133.33)
    else:  # no reading from smartdashboard
        TE.type("could not connect to robot", font, (display_size_left[0] + int(display_size_right[0] * 0.5), int(
            display_size_right[1] * 0.1)), display_size_right[1] / 1600, display_size_right[1] / 1600, black, 2, space_between_letters=display_size_right[1] / 133.33)

    # auto selector
    pindices2 = indices[2]

    for i in range(1, len(auto_chooser_grid)):
        for j in range(len(auto_chooser_grid[i])):
            if (mouseclicked):
                if ((auto_chooser_grid[i][j].hitbox[0][0] < pygame.mouse.get_pos()[0]) == (pygame.mouse.get_pos()[0] < auto_chooser_grid[i][j].hitbox[2][0])):
                    if ((auto_chooser_grid[i][j].hitbox[0][1] < pygame.mouse.get_pos()[1]) == (pygame.mouse.get_pos()[1] < auto_chooser_grid[i][j].hitbox[2][1])):
                        indices[i - 1] = j

    indices[2] = 0  # Override because can't do double cone
    if (indices[2] == 1 and indices[3] == 0):
        indices[2] = 1 - pindices2
        indices[3] = 1 - pindices2

    for i in range(len(auto_chooser_grid)):
        if (i != 0):
            TE.type(categories[i - 1], font, (auto_chooser_grid[i][0].pivotPoint[0], gameDisplay.get_height(
            ) - total_height + (top_border + 25) / 2), 0.25, 0.25, white, 2, space_between_letters=6)
        for j in range(len(auto_chooser_grid[i])):
            temp = auto_chooser_grid[i][j].color
            if (i != 0 and indices[i - 1] != j):
                auto_chooser_grid[i][j].color = gray
            auto_chooser_grid[i][j].draw()
            auto_chooser_grid[i][j].color = temp
            if (i != 0):
                TE.type(auto_chooser_grid[i][j].name, font, auto_chooser_grid[i]
                        [j].pivotPoint, 0.25, 0.25, black, 2, space_between_letters=6)

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

    indices[4] = round(time_wait, 1)  # type: ignore

    TE.type("toqibb", font, (180, 140), 1.2, 1.2,
            black, 6, space_between_letters=12)
    TE.type("auto selector", font, (360, 187), 0.4,
            0.4, black, 2, space_between_letters=6)
    TE.type(str(round(time_wait, 1)), font, (680, 180),
            1.6, 1.6, black, 8, space_between_letters=14)

    smartDashboard.putNumberArray("Auto Data", indices)

    pygame.display.update()
    clock.tick(10)

pygame.quit()
