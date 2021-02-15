import math
side_a = int(input())
side_b = int(input())
side_c = int(input())

perimeter = (side_a + side_b + side_c) / 2
area_triangle = math.sqrt(perimeter * (perimeter - side_a) * (perimeter - side_b) * (perimeter - side_c))
print(area_triangle)