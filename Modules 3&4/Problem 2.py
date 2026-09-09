tickerSymbol = None
numberOfShares = None
pricePerShare = None

while not((tickerSymbol != None) and (tickerSymbol.isalpha())):
    print("Please enter a stock ticker symbol")
    stringInput = input()
    if not(stringInput.isalpha()):
        print()
        print("Please enter only letters, no numbers or symbols")
    else:
        tickerSymbol = stringInput.upper()
        print()
while numberOfShares == None:
    print("Please enter the number of shares you own")
    try:
        numberOfShares = int(input())
        print()
    except: 
        print()
        print("Please enter an integer, ex 40")
while pricePerShare == None:
    print("Please enter the price of each share")
    try:
        floatInput = float(input())
        if (floatInput != round(floatInput, 2)):
            raise
        else:
            pricePerShare = floatInput
            print()
    except: 
        print()
        print("Please enter a dollar amount, ex 3.78")

investmentCost = numberOfShares * pricePerShare
print(f"Your investment in {tickerSymbol} is worth ${investmentCost:.2f}")