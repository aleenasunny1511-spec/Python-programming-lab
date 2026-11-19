#Create a class rectangle with private attributes length and width.Overload '<' operator to compare the area of two rectangles.
class Rectangle:
    def __init__(self,l,b):
        self.__length=l
        self.__breadth=b;
    def getDimensions(self):
        return self.__length.self.__breadth
    def getArea(self):
        return self.__length*self.__breadth
    def __lt__(self,other):
        return self.getArea()<other.getArea()

length1=int(input("enter length 1: "))
breadth1=int(input("enter breadth 1: "))
ar1=Rectangle(length1,breadth1)

length2=int(input("enter length 2: "))
breadth2=int(input("enter breadth 2: "))           
ar2=Rectangle(length2,breadth2)

print(f"Area of 1st rectangle ={ar1.getArea()}")
print(f"Area of 2nd rectangle ={ar2.getArea()}")

if ar1<ar2:
    print("First rectangle is smaller")
elif ar2<ar1:
    print("Second rectangle is smaller")
else:
    print("Both rectangles are equal")
    
