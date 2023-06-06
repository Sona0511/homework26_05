#Write a program that asks the user to enter two numbers ,x, and y, and computes |x-y|/(x+y)
x = float(input("Enter x:"))
y = float(input("Enter y:"))
if x !=0 or y!=0:
    a = (abs(x-y))/(x+y)
    print(a)
else:
    print("x AND y can not be zero")
