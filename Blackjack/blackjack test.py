#poker test
import random
total=0
set=[1,2,3,4,5,6,7,8,9,10,10,10,10,11,1]

while True:
    card=random.choice(set)
    total+=card
    print("You drew a card with value:", card)
    print("Your total is:", total)
    if total > 21:
        print("You lost! Total exceeded 21.")
        break
    elif total == 21:
        print("You won! Total is exactly 21.")
        break
    else:
        cont=input("Do you want to draw another card (yes/no)?")
        if cont.lower() != 'yes':
            print("Game ended, your final total is:", total)
            break
    print()
