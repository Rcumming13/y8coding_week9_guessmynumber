#
from random import randint 

correct = randint(16, 64)
number = None 
while number != correct:

    print("guess my number")
    number = int(input())
    if number > correct:  
        print("lower!")
    if number < correct:
        print("higher!")
    if number == correct :
        print("YOU WON!!!!!!!!")

#five_less = correct - 5
#five_more = correct + 5

#if number >+ five_less and number <= five_more:
 #36
 #    print("ALMOST WITHIN 5 AWAY")