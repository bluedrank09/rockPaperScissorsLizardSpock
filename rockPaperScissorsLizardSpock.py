import sys
from enum import Enum
import random 

class options(Enum):
    Rock = 1
    Paper = 2
    Scissors = 3
    Lizard = 4
    Spock = 5


    

def findWinner(userNumber, computerNumber):

    throw = {
        1:'Rock',
        2:'Paper',
        3:'Scissors',
        4:'Lizard',
        5:'Spock'
    }
    comWin = f"I won! You threw {throw[userNumber]} and I threw {throw[computerNumber]}"
    userWin = f"You won! You threw {throw[userNumber]} and I threw {throw[computerNumber]}"

    if computerNumber == userNumber:
        returnValue = f"It's a tie. We both threw {throw[userNumber]}"
    
    if computerNumber == options.Rock.value:
        if userNumber == options.Scissors.value or userNumber == options.Lizard.value:
            returnValue = comWin
        elif userNumber == options.Paper.value or userNumber == options.Spock.value:
            returnValue = userWin

    elif computerNumber == options.Paper.value:
        if userNumber == options.Rock.value or userNumber == options.Spock.value:
            returnValue = comWin
        elif userNumber == options.Scissors.value or userNumber == options.Lizard.value:
            returnValue = userWin

    elif computerNumber == options.Scissors.value:
            if userNumber == options.Lizard.value or userNumber == options.Paper.value:
                returnValue = comWin
            elif userNumber == options.Spock.value or userNumber == options.Rock.value:
                returnValue = userWin

    elif computerNumber == options.Lizard.value:
        if userNumber == options.Spock.value or userNumber == options.Paper.value:
            returnValue = comWin
        elif userNumber == options.Rock.value or userNumber == options.Scissors.value:
            returnValue = userWin

    elif computerNumber == options.Spock.value:
        if userNumber == options.Rock.value or userNumber == options.Scissors.value:
            returnValue = comWin
        elif userNumber == options.Paper.value or userNumber == options.Lizard.value:
            returnValue = userWin

    return(returnValue)
        
if __name__ == "__main__":
    try:
        userNumber = int(input('Give me a number : '))
        computerNumber = random.randint(1,6)

        print(findWinner(userNumber, computerNumber))

    except Exception as error:
        e_type, e_object, e_traceback = sys.exc_info()
        print(f"{e_type}, {e_object}")

    finally:
        print(f":)")