itemCount = None
while itemCount == None:
    print("Please enter the quantity of widgets you would like to purchase")
    try:
        rawInt = int(input())
        if rawInt < 0:
            raise
        itemCount = rawInt
        print()
    except: 
        print()
        print("Please enter a positive integer, ex 4000")

itemPrice = 30
discountApplied = False
if itemCount >= 5000 and itemCount <= 10000:
    itemPrice = 20
    discountApplied = True
else:
    itemPrice = 10
    discountApplied = True
totalPrice = itemPrice * itemCount * 1.07

outputStrings = []
outputStrings.append(f"You selected {itemCount:,} widgets")
outputStrings.append(f"This widget costs ${itemPrice:.2f}; {"" if discountApplied else "no "}bulk discount applied")
outputStrings.append(f"With 7% sales tax, your total today is ${totalPrice:,.2f}")

maxLength = 0
for string in outputStrings:
    if (maxLength < len(string)):
        maxLength = len(string)

print("".ljust(maxLength, "-"))
for string in outputStrings:
    print(string)
print("".ljust(maxLength, "-"))