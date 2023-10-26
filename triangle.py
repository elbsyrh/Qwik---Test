def triangleType(side1, side2, side3):
    if side1 == side2 == side3:
        return "Equilateral Triangle"
    elif side1 == side2 or side2 == side3 or side1 == side3:
        return "Isosceles Triangle"
    else:
        return "Scalene Triangle"

# Example sides of a triangle
triangle_side1 = 3
triangle_side2 = 5
triangle_side3 = 8

triangle_type = triangleType(triangle_side1, triangle_side2, triangle_side3)
print(f"The triangle is a {triangle_type}.")
