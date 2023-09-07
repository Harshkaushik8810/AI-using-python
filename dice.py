
import random
from assistant import speak
def roll():
    randnum=random.randint(1,6)
    print("Rolling......")
    print(f"The number shown by dice is:-{randnum}")
    speak(f"The number shown by dice is {randnum}")
def roll2():
    randnum=random.randint(1,6)
    a=random.randint(1,6)
    print("Rolling......")
    print(f"The number shown by dice 1 is:-{randnum} and number shown by dice 2 is:- {a}")
    speak(f"The number shown by dice 1 is {randnum} and number shown by dice 2 is {a}")

