import math

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

def polygons_for_bezier(start_point, mid_point, end_point, width, smoothness=10, line_smoothness=4):
    ListOfPolygons = []
    x_next, y_next = start_point
    i = 0.0
    for j in range(smoothness):
        x_now = x_next
        y_now = y_next
        i += 1.0/smoothness
        x_next = (1-i)*(1-i)*start_point[0] + 2*i*(1-i)*mid_point[0] + i*i*end_point[0]
        y_next = (1-i)*(1-i)*start_point[1] + 2*i*(1-i)*mid_point[1] + i*i*end_point[1]
        ListOfPolygons.append(polygon_for_line((x_now, y_now), (x_next, y_next), width, smoothness=line_smoothness))
    return ListOfPolygons