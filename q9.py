a=int(input("enter Cost="))
b=int(input("enter selling="))
if (b-a)>0:
    print("profit=",b-a)
elif (b-a)<0:
    print("Loss=",b-a)
else:
    print("no profit no loss")