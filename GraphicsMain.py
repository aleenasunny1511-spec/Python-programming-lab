from graphics.rectFunctions import*
from graphics.cirFunctions import*
from graphics.DGraphics.sphereFns import*
from graphics.DGraphics.cuboidFns import*
#Rectangle
l=int(input("Enter the length: "))
b=int(input("Enter the breadth: "))
print("Rectangle Area is ",rectArea(l,b))
print("Rectangle perimeter is ",rectPerimeter(l,b))

#Circle
r=int(input("Enter the radius of circle: "))
print("Circle Area is ",circleArea(r))
print("Circle perimeter is ",circlePerimeter(r))

#Sphere
r=int(input("Enter the radius of sphere: "))
print("Sphere Area is ",sphArea(r))
print("Sphere perimeter is ",sphPerimeter(r))

#Cuboid
l=int(input("Enter the length: "))
b=int(input("Enter the breadth: "))
h=int(input("Enter the height: "))
print("Cuboid Area is ",cubArea(l,b,h))
print("Rectangle perimeter is ",cubPerimeter(l,b,h))
