itemCount = 0
while itemCount == None:
    print("Please enter the quantity of items you would like to purchase")
    try:
        rawInt = int(input())
        if itemCount < 0:
            raise
        itemCount = rawInt
        print()
    except: 
        print()
        print("Please enter a positive integer, ex 40")

itemPrice = 5
discountApplied = False
if itemCount >= 1000:
    itemPrice = 3
    discountApplied = True
totalprice = itemPrice * itemCount * 1.07

outputStrings = []
outputStrings.append(f"You selected {itemCount} items")
outputStrings.append(f"This item costs ${itemPrice:.2f}; {"" if discountApplied else "no "}bulk discount applied")
outputStrings.append(f"With 7% sales tax, your total today is ${totalprice:.2f}")

maxLength = 0
for string in outputStrings:
    if (maxLength < len(string)):
        maxLength = len(string)

print("".ljust(maxLength, "-"))
for string in outputStrings:
    print(string)
print("".ljust(maxLength, "-"))