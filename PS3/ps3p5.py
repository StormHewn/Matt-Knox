ticketCount = None
while ticketCount == None:
    print("Please enter the quantity of tickets you would like to purchase")
    try:
        rawInt = int(input())
        if rawInt < 0:
            raise
        ticketCount = rawInt
        print()
    except: 
        print()
        print("Please enter a positive integer, ex 40")

if (ticketCount < 5):
    ticketPrice = 75
    discountLevel = "no"
elif (ticketCount < 10):
    ticketPrice = 70
    discountLevel = "light"
elif (ticketCount < 25):
    ticketPrice = 60
    discountLevel = "heavy"
else:
    ticketPrice = 50
    discountLevel = "max"
totalPrice = ticketPrice * ticketCount

outputStrings = []
outputStrings.append(f"You selected {ticketCount:,} tickets")
outputStrings.append(f"Each ticket costs ${ticketPrice:.2f}; {discountLevel} bulk discount")
outputStrings.append(f"Your total today is ${totalPrice:,.2f}")

maxLength = 0
for string in outputStrings:
    if (maxLength < len(string)):
        maxLength = len(string)

print("".ljust(maxLength, "-"))
for string in outputStrings:
    print(string)
print("".ljust(maxLength, "-"))