#comments missing

import random


def game(comp,palyer): 
    if comp==palyer:
        print("tie")
    elif comp=='r':
         if player=='s':
             print("you lose") 
         elif palyer=='p':
             print("you win")      
    elif comp=='p':
        if player=='r':
            print("you lose")
        elif palyer=='s':
             print("you win")        
    elif comp=='s':
        if palyer=='p':
            print("you lose")
        elif palyer=='r':
             print("you win")   
                 

print("comps turn rock(r),paper(p) sciccor(s).")
randno = random.randint(1,3)
if randno==1:
    comp='r'
elif randno==2:
    comp='p'    
else:
    comp='s'    

player=input("player turn rock(r),paper(p) sciccor(s)")    
print("computer chooses",comp,"\n" "player chooses",player)
game(comp,player)    