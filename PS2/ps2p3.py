lastName = None
midtermScore   = None
finalExamScore = None

while not((lastName != None) and (lastName.isalpha())):
    print("Please enter your last name")
    stringInput = input()
    if not(stringInput.isalpha()):
        print()
        print("Please enter only letters, no numbers or symbols")
    else:
        lastName = stringInput.title()
        print()
while midtermScore == None:
    print("Please enter your midterm exam score")
    rawIntScore = int(input())
    try:
        if not (0 <= rawIntScore and rawIntScore <= 100):
            raise
        else:
            midtermScore = rawIntScore
            print()
    except:
        print()
        print("Please enter an integer between 0 and 100, ex 40")
while finalExamScore == None:
    print("Please enter your final exam score")
    rawIntScore = int(input())
    try:
        if not (0 <= rawIntScore and rawIntScore <= 100):
            raise
        else:
            finalExamScore = rawIntScore
            print()
    except: 
        print()
        print("Please enter an integer between 0 and 100, ex 40")

midtermWeightedScore   = midtermScore   * 0.4
finalExamWeightedScore = finalExamScore * 0.6
totalScore = midtermWeightedScore + finalExamWeightedScore

print(f"Mr/Ms. {lastName}'s total score is {totalScore:.1f}%")