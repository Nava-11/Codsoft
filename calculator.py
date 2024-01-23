import math
x=int(input("enter the x value "))
y=int(input("enter the y value "))
op=(input("enter the operation to be performed "))
if(op=='+'):
  result=x+y
  print("addition of two numbers ",result)
elif(op=='-'):
  result=x-y
  print("subtraction of two numbers ",result)
elif(op=='*'):
  result=x*y
  print("multiplication of two numbers ",result)
elif(op=='/'):
  result=x/y
  print("division of two numbers ",result)
elif(op=='x**y'):
  result=math.pow(x,y)
  print("square is ",result)
elif(op=='%'):
  result=(x/y)*100
  print("percent of two numbers is ",result)
elif(op=='log'):
  result=math.log(x,y)
  print("log of x for base y is  ",result)