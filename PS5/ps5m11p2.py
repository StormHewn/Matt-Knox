def main():
    lastName = inputName("Please enter the student's last name")
    scores = []
    while len(scores) < 3:
        scores.append(inputInt(f"Please enter exam score {len(scores) + 1}", lowerBound= 0, upperBound= 100))

    scoreSum, scoreAvg = calculateSumAndAverage(scores)

    print(f"{lastName}'s average is {scoreAvg:.2f} and their total score is {scoreSum}")

def calculateSumAndAverage(numbers):
    sum = 0
    for value in numbers:
        sum += value
    average = sum / len(numbers)
    return sum, average

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