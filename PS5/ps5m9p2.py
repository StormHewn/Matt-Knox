def main():
    totalPlayerCount = 0
    print("Do you want to begin entering player data? (Y/n)")
    repeatFlag = input()
    print()
    loopEntered = False
    while repeatFlag.lower().count("n") == 0:
        loopEntered = True

        playerName = inputName("Please enter a player last name")
        atBats = inputInt("How many times has this player batted?", lowerBound=0)
        hits = inputInt("How many times has this player hit the ball?", lowerBound=0, upperBound=atBats+1)
        battingAverage = calculateBattingAverage(atBats, hits)
        formattedBattingAverage = f"{battingAverage:.3f}"
        if battingAverage != 1:
            formattedBattingAverage = f"{formattedBattingAverage[1:]}"

        print(f"{playerName}'s batting average is {formattedBattingAverage}")
        print()
        totalPlayerCount += 1

        print("Do you want to continue adding player data? (Y/n)")
        repeatFlag = input()
        print()

    if (loopEntered):
        print(f"You entered {totalPlayerCount:,} players")

def calculateBattingAverage(atBats, hits):
    return hits / atBats

def inputInt(message, lowerBound = -1e6, upperBound = 1e6):
    returnInt = None
    while returnInt == None:
        print(message)
        try:
            rawInt = int(input())
            if ((rawInt < lowerBound) | (rawInt > upperBound)):
                raise
            returnInt = rawInt
            print()
        except: 
            print()
            if ((lowerBound == -1e6) & (upperBound == 1e6)):
                print("Please enter an integer")
            elif ((lowerBound == -1e6) & (upperBound != 1e6)):
                print(f"Please enter an integer less than {upperBound}")
            elif ((lowerBound != -1e6) & (upperBound == 1e6)):
                print(f"Please enter an integer greater than {lowerBound}")
            elif ((lowerBound != -1e6) & (upperBound != 1e6)):
                print(f"Please enter an integer between {lowerBound} and {upperBound}")
    return returnInt

def inputName(message):
    returnString = None
    while not((returnString != None) and (returnString.isalpha())):
        print(message)
        stringInput = input()
        print()
        if not(stringInput.isalpha()):
            print("Please enter only letters, no numbers or symbols")
        else:
            returnString = stringInput.title()
    return returnString

main()