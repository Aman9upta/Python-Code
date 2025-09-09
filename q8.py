a=int(input("enter side length"))
b=int(input("enter side length"))
c=int(input("enter side length"))
if (a+b)>c or (b+c)>a or (a+c)>b:
    print("valid triangle")
else:
    print("invalid triangle")