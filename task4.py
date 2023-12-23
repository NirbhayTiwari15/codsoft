import random
print("Welcome to the Game")
print("Rock-Paper-Scissor")
score=0
while(True):
    print("What would you like to choose between these options??")
    print("1.Rock")
    print("2.Paper")
    print("3.Scissor")
    c=int(input("Please select the number between 1 to 3 as per your choice:"))
    r=random.randint(1,3)
    print("Your choice is",c,"\t Computer choice is",r)
    if (c==1 and r==3 ):
        print("Congrats !!!!!!! You won the match.")
        score+=1
    elif( c==2 and r==1):
        print("Congrats !!!!!!! You won the match.")
        score+=1
    elif(c==3 and r==2):
        print("Congrats !!!!!!! You won the match.")
        score+=1
    elif (c==r):
        print("Match draw.")
    else:
        print("Computer won the match.")
    print("Your Score is:",score)
    s=str(input("Would you like to play game again?(y/n)"))
    if(s=='n'):
        break
