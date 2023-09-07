
from assistant import speak

def sum():
    sum=0
    print("Type 'q' to END")
    while (True):
        a=input("Enter the number")
        if (a!='q'):
            sum=sum+int(a)
        else:
            print(f"Your totall is {sum}") 
            speak(f"Your totall is {sum}") 
            break

def div():
    a=int(input("enter a number"))
    b=int(input("enter 2nd number"))
    c=a/b
    print(f"Your ans is",c)
    speak(f"Your ans is",c)

def sub():
     sum=0
     print("Type 'q' to END")
     while (True):
        a=input("Enter the number")
        if sum==0:
            sum=sum+int(a)
        elif (a!='q'):
                sum=sum-int(a)
                if sum==0:
                    print(f"Your totall is {sum}")
        else:
            print(f"Your totall is {sum}") 
            speak(f"Your totall is {sum}") 
            break

def mul():
     sum=0
     print("Type 'q' to END")
     while (True):
        a=input("Enter the number")
        if sum==0:
            sum=sum+int(a)
        elif (a!='q'):
                sum=sum*int(a)
                if sum==0:
                    print(f"Your totall is {sum}")
                    speak(f"Your totall is {sum}")
        else:
            print(f"Your totall is {sum}") 
            speak(f"Your totall is {sum}") 
            break

def fact():
    n=int(input("enter number"))
    a=n
    sum=1
    while n>0:
        sum=sum*n
        n=n-1
    print(f" Factorial of the number{a} is {sum}")
    speak(f" Factorial of the number{a} is {sum}")