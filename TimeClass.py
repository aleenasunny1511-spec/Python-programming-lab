#Create a class time with private attributes hour,minitue,and second.Overload the + operator to find the sum of two time objects

class Time:
    def __init__(self):
        self.__hours=int(input("Enter the hours(0-23): "))
        self.__minitues=int(input("Enter the minitues: "))
        self.__seconds=int(input("Enter the seconds: "))
    def __add__(self,other):
        total_seconds=((self.__hours+other.__hours)*3600+(self.__minitues+other.__minitues)*60+(self.__seconds+other.__seconds))

        hours=(total_seconds//3600)%24
        minitues=(total_seconds//60)%60
        seconds=total_seconds%60
        return f"{hours:02d}:{minitues:02d}:{seconds:02d}"
    
print("Enter details for time 1:")
t1=Time()
print("\nEnter details for time 2:")
t2=Time()
result=t1+t2
print("Sum of the two times: ",result)
