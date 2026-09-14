principalAmount = None
while principalAmount == None:
    print("Please enter your amount pf principal")
    try:
        rawFloat = float(input())
        if rawFloat < 0:
            raise
        principalAmount = rawFloat
        print()
    except: 
        print()
        print("Please enter a dollar amount, ex 38000.57")
numberOfYears = None
while numberOfYears == None:
    print(f"Please enter the number of years for your CD")
    try:
        rawInt = int(input())
        if rawInt < 0:
            raise
        numberOfYears = rawInt
        print()
    except: 
        print()
        print("Please enter a positive integer, ex 10")

rate = 0.02
if (principalAmount > 100000):
    if (numberOfYears == 5):
        rate = 0.06
elif (principalAmount >= 50000):
    match numberOfYears:
        case 10:
            rate = 0.05
        case 5:
            rate = 0.04
firstYearInterest = (principalAmount * rate)

outputStrings = []
outputStrings.append(f"Principal: ${principalAmount:,.2f}")
outputStrings.append(f"CD rate: {rate:.2%}")
outputStrings.append(f"First Year Interest: ${firstYearInterest:,.2f}")

maxLength = 0
for string in outputStrings:
    if (maxLength < len(string)):
        maxLength = len(string)

print("".ljust(maxLength, "-"))
for string in outputStrings:
    print(string)
print("".ljust(maxLength, "-"))