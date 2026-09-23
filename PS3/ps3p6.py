lastName = None
salary = None
jobLevel = None

while not((lastName != None) and (lastName.isalpha())):
    print("Please enter your last name")
    stringInput = input()
    if not(stringInput.isalpha()):
        print()
        print("Please enter only letters, no numbers or symbols")
    else:
        lastName = stringInput.title()
        print()
while salary == None:
    print("Please enter your salary")
    try:
        rawFloat = float(input())
        if rawFloat < 0:
            raise
        salary = rawFloat
        print()
    except: 
        print()
        print("Please enter a dollar amount, ex 38000.57")
while jobLevel == None:
    print("Please enter your job level")
    try:
        rawIntScore = int(input())
        if not (0 <= rawIntScore and rawIntScore <= 15):
            raise
        else:
            jobLevel = rawIntScore
            print()
    except:
        print()
        print("Please enter an integer between 0 and 15, ex 4")

if (jobLevel >= 10):
    rate = 0.25
elif (jobLevel >= 5):
    rate = 0.20
else:
    rate = 0.10
bonusAmount = salary * rate

outputString = f"Mr./Ms. {lastName} gets a bonus of ${bonusAmount:,.2f}"
print("".ljust(len(outputString), "-"))
print(outputString)
print("".ljust(len(outputString), "-"))