print("Welcome to Calculator")
while(True):
    print("What do you want to do?\n 1.Addition\n 2.Subtraction\n 3.Multiplication\n 4.Division")
    c=int(input("Please choose the number between 1 to 4 as per your requirement."))

    a=float(input("Enter First Number:"))
    b=float(input("Enter Second Number:"))
    if (c==1):
        print("Addition result i.e. a+b=",a+b)
    elif (c==2):
        print("Subtraction result i.e. a-b=",a-b)
    elif (c==3):
        print("Multiplication result i.e. a*b=",a*b)
    elif (c==4):
        if(b==0):
            print("Denominator cannot be 0")
        else:
            print("Division result i.e. a/b=",a/b)
    s=str(input("Would you like to use caculator again?(y/n)"))
    if(s=="n"):
        print("Thankyou for using Calculator!!!!!!!!!!!!")
        break