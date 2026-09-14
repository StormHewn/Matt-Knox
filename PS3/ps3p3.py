partNumber = None
while partNumber == None:
    print("Please enter a part number (Valid range: 1-100)")
    try:
        rawInt = int(input())
        if rawInt < 0 or rawInt > 100:
            raise
        partNumber = rawInt
        print()
    except: 
        print()
        print("Please enter an integer between 0 and 100, ex 45")
partCount = None
while partCount == None:
    print(f"Please enter the quantity of Part {partNumber} you would like to purchase")
    try:
        rawInt = int(input())
        if rawInt < 0:
            raise
        partCount = rawInt
        print()
    except: 
        print()
        print("Please enter a positive integer, ex 80")

itemPrice = 5
match partNumber:
    case 10 | 55:
        itemPrice = 1
    case 99:
        itemPrice = 2
    case 70 | 80:
        itemPrice = 3
totalPrice = itemPrice * partCount

outputStrings = []
outputStrings.append(f"You selected Part {partNumber}")
outputStrings.append(f"This part costs ${itemPrice:.2f}")
outputStrings.append(f"Your total today is ${totalPrice:,.2f}")

maxLength = 0
for string in outputStrings:
    if (maxLength < len(string)):
        maxLength = len(string)

print("".ljust(maxLength, "-"))
for string in outputStrings:
    print(string)
print("".ljust(maxLength, "-"))