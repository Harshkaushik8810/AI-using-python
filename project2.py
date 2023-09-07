#number guessing
def game():
    import random
    randnumber=random.randint(1,100)
    a=None
    guesses=0
    print("you have 5 turns only")
    while(guesses<=5):
        a=int(input("enter number \n"))
        guesses=guesses+1
        if randnumber==a:   
            print("you guessed right")
            print("#The number was# ",randnumber)
            break
        else:
            if (randnumber > a):   
                print("you guessed wrong the number is **BIGGER** than ",a,"\n")
                if randnumber%2==0:
                    print("---HINT---- No is even")
                else:
                    print("---HINT---- No is odd")    
            else:
                print("you guessed wrong the number is **SMALLER** than",a,"\n")
                if randnumber%2==0:
                    print("---HINT---- No is even")
                else:
                    print("---HINT---- No is odd")
    
    if randnumber!=a:
        print("OOPS! out of turn")
        print("***The number was***",randnumber)            
print("press 1 to start the game")
a=int(input("enter number \n"))
if a==1:
    game()
else:
    print("____OK BYE ____")
print("**do you still wanna play press 1 for yes 2 for no***")
b=int(input("1 or 2"))
if b==1:
 while b==1:
    game()
    b=b-1
    print("**do you wanna play again press 1 for yes 2 for no***")
    b=int(input("1 or 2"))
    if b==2:
        print("--see you soon--")
    else:
        pass
else:
    print("--see you soon--")      
