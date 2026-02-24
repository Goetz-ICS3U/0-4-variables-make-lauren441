"""
HEADER COMMENTS
"""
# Lauren W
# February 18, 2026

# Input
# Processing
# Output

import math

# Input   
radius = int(input("Enter the radius of the circle: "))
length = int(input("Enter the length of the rectangle: "))
width = int(input("Enter the width of the rectangle: "))
side = int(input("Enter a side length of the octagon: "))

# Processing
circle_area = math.pi * radius  **2
circle_perimeter = 2 * math.pi * radius

rectangle_area = length * width
rectangle_perimeter = 2 * (length + width)

octagon_area = 2 * (1 + math.sqrt(2)) * side ** 2
octagon_perimeter = 8 * side

# Output
print(f"The has an area of {circle_area} and a perimeter of {circle_perimeter}")
print(f"The has an area of {rectangle_area} and a perimeter of {rectangle_perimeter}")
print(f"The has an area of {octagon_area} and a perimeter of {octagon_perimeter}")
