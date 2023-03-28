import math
from constants import *
from polygon import Polygon
from pygame import Surface


temp = [
    (total_height - top_border - bottom_border - space_between) / 2,
    (total_height - top_border - bottom_border - 2 * space_between) / 3,
    (total_width - 2 * side_border - 3 * space_between) / 4
]


def getAutoChooserGrid(gameDisplay: Surface):
    return [[
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
             [-total_width / 2 + side_border + temp[2],
                 total_height / 2 - top_border],
                [-total_width / 2 + side_border + temp[2],
             total_height / 2 - top_border - temp[0]],
                [-total_width / 2 + side_border, total_height / 2 - top_border - temp[0]]],
            blue,
            gameDisplay,
            pivot=(-total_width / 2 + side_border +
                   temp[2] / 2, total_height / 2 - top_border - temp[0] / 2),
            name="blue"
        ),
        Polygon(
            [[-total_width / 2 + side_border, -total_height / 2 + bottom_border],
             [-total_width / 2 + side_border + temp[2], -
             total_height / 2 + bottom_border],
                [-total_width / 2 + side_border + temp[2], -
             total_height / 2 + bottom_border + temp[0]],
                [-total_width / 2 + side_border, -total_height / 2 + bottom_border + temp[0]]],
            red,
            gameDisplay,
            pivot=(-total_width / 2 + side_border +
                   temp[2] / 2, -total_height / 2 + bottom_border + temp[0] / 2),
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
            pivot=(-temp[2] / 2 - space_between / 2,
                   total_height / 2 - top_border - temp[1] / 2),
            name="short"
        ),
        Polygon(
            [[-temp[2] - space_between / 2, total_height / 2 - top_border - temp[1] - space_between],
             [-space_between / 2, total_height / 2 -
             top_border - temp[1] - space_between],
                [-space_between / 2, -total_height / 2 +
             bottom_border + temp[1] + space_between],
                [-temp[2] - space_between / 2, -total_height / 2 + bottom_border + temp[1] + space_between]],
            green,
            gameDisplay,
            pivot=(-temp[2] / 2 - space_between / 2,
                   (bottom_border - top_border) / 2),
            name="medium"
        ),
        Polygon(
            [[-temp[2] - space_between / 2, -total_height / 2 + bottom_border],
             [-space_between / 2, -total_height / 2 + bottom_border],
                [-space_between / 2, -total_height / 2 + bottom_border + temp[1]],
                [-temp[2] - space_between / 2, -total_height / 2 + bottom_border + temp[1]]],
            orange,
            gameDisplay,
            pivot=(-temp[2] / 2 - space_between / 2, -
                   total_height / 2 + bottom_border + temp[1] / 2),
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
            pivot=(temp[2] / 2 + space_between / 2,
                   total_height / 2 - top_border - temp[0] / 2),
            name="one"
        ),
        Polygon(
            [[temp[2] + space_between / 2, -total_height / 2 + bottom_border],
             [space_between / 2, -total_height / 2 + bottom_border],
                [space_between / 2, -total_height / 2 + bottom_border + temp[0]],
                [temp[2] + space_between / 2, -total_height / 2 + bottom_border + temp[0]]],
            lime,
            gameDisplay,
            pivot=(temp[2] / 2 + space_between / 2, -
                   total_height / 2 + bottom_border + temp[0] / 2),
            name="two"
        )
    ], [
        Polygon(
            [[total_width / 2 - side_border, total_height / 2 - top_border],
             [total_width / 2 - side_border - temp[2],
                 total_height / 2 - top_border],
                [total_width / 2 - side_border - temp[2],
             total_height / 2 - top_border - temp[0]],
                [total_width / 2 - side_border, total_height / 2 - top_border - temp[0]]],
            lime,
            gameDisplay,
            pivot=(total_width / 2 - side_border -
                   temp[2] / 2, total_height / 2 - top_border - temp[0] / 2),
            name="yes"
        ),
        Polygon(
            [[total_width / 2 - side_border, -total_height / 2 + bottom_border],
             [total_width / 2 - side_border - temp[2], -
             total_height / 2 + bottom_border],
                [total_width / 2 - side_border - temp[2], -
             total_height / 2 + bottom_border + temp[0]],
                [total_width / 2 - side_border, -total_height / 2 + bottom_border + temp[0]]],
            lime,
            gameDisplay,
            pivot=(total_width / 2 - side_border -
                   temp[2] / 2, -total_height / 2 + bottom_border + temp[0] / 2),
            name="no"
        )
    ]]


def anglesToPoint(angles):
    return [
        (proximal_length - 4) * math.cos(math.pi / 180.0 *
                                         angles[0]) + (distal_length + 7.751984) * math.cos(math.pi / 180.0 * angles[1]),
        (proximal_length - 4) * math.sin(math.pi / 180.0 *
                                         angles[0]) + (distal_length + 7.751984) * math.sin(math.pi / 180.0 * angles[1])
    ]


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

    angle = math.atan(y / x) * 180.0 / math.pi
    if (x < 0):
        if (angle > 0):
            angle -= 180
        else:
            angle += 180

    first_angle = math.acos((radius * radius + (proximal_length - 4) * (proximal_length - 4) - (distal_length +
                            7.751984) * (distal_length + 7.751984)) / (2.0 * (proximal_length - 4) * radius)) * 180.0 / math.pi
    second_angle = math.acos((radius * radius + (distal_length + 7.751984) * (distal_length + 7.751984) - (
        proximal_length - 4) * (proximal_length - 4)) / (2.0 * (distal_length + 7.751984) * radius)) * 180.0 / math.pi

    if (ccu):
        return [angle - first_angle, angle + second_angle]
    else:
        return [angle + first_angle, angle - second_angle]


# definition of "above": y above line, or if vertical, then x value greater
def point_above_line(point, line):
    # point format: (x, y)
    # line format: [(x1, y1), (x2, y2)]
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
        return False  # legit zero chance they intersect

    temp_1 = line_1[1][0]
    temp_2 = line_2[1][0]
    if line_1[0][0] == line_1[1][0]:
        temp_1 += 0.01
    if line_2[0][0] == line_2[1][0]:
        temp_2 += 0.01
    lein_1 = [line_1[0], (temp_1, line_1[1][1])]
    lein_2 = [line_2[0], (temp_2, line_2[1][1])]

    if point_on_line(lein_1[0], lein_2) or point_on_line(lein_1[1], lein_2) or point_on_line(lein_2[0], lein_1) or point_on_line(lein_2[1], lein_1):
        return False  # if any of the points are on the line
    else:
        return (point_above_line(lein_1[0], lein_2) != point_above_line(lein_1[1], lein_2)) and (point_above_line(lein_2[0], lein_1) != point_above_line(lein_2[1], lein_1))


# we want the inside-ness to be the same for every line
def point_inside_polygon(point, polygon, accuracy=6):
    # solution - very scuffed - kinda LOLLY - but should work
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

    for i in range(accuracy):  # go over "accuracy" radial lines
        temp = 0

        # add 1 if intersects line, 0.5 for each endpoint it touches
        for j in range(len(polygon)):
            radial_line = [point, (point[0] + length*math.cos(2*math.pi/accuracy * i),
                                   point[1] + length*math.sin(2*math.pi/accuracy * i))]
            if point_on_line(polygon[j], radial_line):
                temp += 1
            if point_on_line(polygon[(j+1) % len(polygon)], radial_line):
                temp += 1
            if intersect(radial_line,
                         [polygon[j], polygon[(j+1) % len(polygon)]]):
                temp += 2
            # see if the radial line intersects any of the hitbox lines

        if temp % 4 != 2:
            return False
    return True
