currentPrice = None
pricePaid = None
numberOfShares = None

while pricePaid == None:
    print("Please enter the price you paid for share")
    try:
        floatInput = float(input())
        if (floatInput != round(floatInput, 2)):
            raise
        else:
            pricePaid = floatInput
            print()
    except: 
        print()
        print("Please enter a dollar amount, ex 3.78")
while currentPrice == None:
    print("Please enter the current price per share")
    try:
        floatInput = float(input())
        if (floatInput != round(floatInput, 2)):
            raise
        else:
            currentPrice = floatInput
            print()
    except: 
        print()
        print("Please enter a dollar amount, ex 3.78")
while numberOfShares == None:
    print("Please enter the number of shares you own")
    try:
        numberOfShares = int(input())
        print()
    except: 
        print()
        print("Please enter an integer, ex 40")

priceDifference = (currentPrice - pricePaid) * numberOfShares

if priceDifference > 0:
    print(f"This investment has gained ${priceDifference:.2f}")
elif priceDifference < 0:
    print(f"This investment has lost ${-priceDifference:.2f}")
else:
    print("Your investment has stayed at the same value")