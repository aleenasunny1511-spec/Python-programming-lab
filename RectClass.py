#Create Rectangle class with attributes length & breadth and methods to find area & perimeter.Compare two rectangle objects by their area

class Rect:
    def __init__(self,length,breadth):
        self.l=length
        self.b=breadth

    def area(self):
        ar=self.l*self.b
        return ar
    def perimeter(self):
        p=2*(self.l+self.b)
        return p
x1=int(input("Enter length of 1st rectangle: "))
y1=int(input("Enter breadth of 1st rectangle: "))
r1=Rect(x1,y1)
print("Area of 1st rectangle is ",r1.area())
print("Perimeter of 1st rectangle is ",r1.perimeter())


x2=int(input("Enter length of 2nd rectangle: "))
y2=int(input("Enter breadth of 2nd rectangle: "))
r2=Rect(x2,y2)
print("Area of 2nd rectangle is ",r2.area())
print("Perimeter of 2nd rectangle is ",r2.perimeter())

if(r1.area()==r2.area()):
   print("\nAreas of both rectangles are equal.")
else:
    print("\nAreas of both rectangles are not equal.")
