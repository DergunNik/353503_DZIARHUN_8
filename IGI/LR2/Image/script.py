import os
import square
import circle


shape = os.getenv("SHAPE", "circle")  
size = float(os.getenv("SIZE", 5))    

if shape == "circle":
    area = circle.area(size)
    perimeter = circle.perimeter(size)
elif shape == "square":
    area = square.area(size)
    perimeter = square.perimeter(size)
else:
    raise ValueError("Unknown shape")

print(f"Shape: {shape}")
print(f"Area: {area}")
print(f"Perimeter: {perimeter}")
