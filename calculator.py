import math
while True: 
     print(""" 
    press -  
    1 - Addition(x, y) 
    2 - subtraction(x,y) 
    3-multiplication(x,y) 
    4 - division(x, y) 
    5- tan(x) 
    6 - sin(x) 
    7 - cos(x) 
    8 - log(x) 
    9 - cot(x)  
    """) 
     o = input("") 
     if o == "1": 
        x = int(input("1st number -")) 
        y = int(input("2nd number -")) 
        result=x+y
        print(result) 
     elif o == "2": 
        x = int(input()) 
        y = int(input()) 
        result=x-y 
        print(result) 
     elif o == "3": 
        x = int(input()) 
        y = int(input())
        result=x*y 
        print(result) 
     elif o == "4": 
        x = int(input()) 
        y = int(input())
        result=x/y 
        print(result)  
     elif o == "5": 
        x = int(input()) 
        d=x/360*2*math.pi
        result= math.tan(d)
        print(result) 
     elif o == "6": 
        x = int(input()) 
        d=x/360*2*math.pi
        result= math.sin(d)
        print(result) 
     elif o == "7": 
        x = int(input()) 
        d=x/360*2*math.pi
        result= math.cos(d)
        print(result)
     elif o == "8": 
        x = int(input())
        result=math.log(x)
        print(result) 
     elif  o=="9" :
        x = int(input())
        d=x/3600*2*math.pi
        result=1/math.tan(d)
        print(result)
     break  
