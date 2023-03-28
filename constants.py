proximal_length = 32
distal_length = 15

display_size_left = (800, 593)
display_size_right = (740, 593)

pixels_per_inch = display_size_right[0] * 0.01

space_between = 15
total_height = 400
total_width = 800
side_border = 20
top_border = 50
bottom_border = 20

robot_ip = "10.9.91.2"

categories = ["station", "place",  "elements", "autobalance"]


robot_polygon: list[tuple[float, float]] = [  # in inches
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
    (21.25, 41.244303),
    (21.25, 7),
    (19, 7),
    (19, 40.085943),
    (4.25, 31.398242),
    (4.25, 7)
]

first_pivot: tuple[float, float] = (27.278627, 45.825413)

proximal_polygon: list[tuple[float, float]] = [
    (-1, -1),
    (proximal_length - 3, -1),
    (proximal_length - 3, 1),
    (-1, 1)

]

second_pivot: tuple[float, float] = (proximal_length - 4, 0)

distal_polygon: list[tuple[float, float]] = [
    (0.792893, 1.414214),
    (2, -1),
    (distal_length - 2, -1),
    (distal_length - 2, -2.5),
    (-2, -2.5),
    (-2, -1),
    (-0.792893, 1.414214)
]

claw_polygon: list[tuple[float, float]] = [
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

purple = (125, 50, 168)
cone_yellow = (224, 206, 45)
