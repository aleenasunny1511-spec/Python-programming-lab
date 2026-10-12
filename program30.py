# write lambda functions to find area of a square,rectangle and triangle.
square_area=lambda a:a**2
rectangle_area=lambda l,b:l*b
triangle_area=lambda ba,h:0.5*ba*h

a=int(input("Enter the length: "))
print("Area of Square: ",square_area(a))

l=int(input("Enter the length: "))
b=int(input("Enter the breadth: "))
print("Area of rectangle: ",rectangle_area(l,b))


ba=int(input("Enter the base: "))
h=int(input("Enter the height: "))
print("Area of triangle: ",triangle_area(ba,h))
