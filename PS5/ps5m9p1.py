def main():
    totalExtendedPrice = 0
    print("Do you want to begin your purchase? (Y/n)")
    repeatFlag = input()
    print()
    loopEntered = False
    while repeatFlag.lower().count("n") == 0:
        loopEntered = True
        
        numberOfUnits = inputInt("Please enter the number of units you would like to purchase")
        pricePerUnit = inputDollar("Please enter the price per unit")
        extendedPrice = calculateExtendedPrice(numberOfUnits, pricePerUnit)
        print(f"{numberOfUnits:,} units, at ${pricePerUnit:,.2f} per unit, costs ${extendedPrice:,.2f}")
        print()

        totalExtendedPrice += extendedPrice

        print("Do you want to add another item? (Y/n)")
        repeatFlag = input()
        print()

    if (loopEntered):
        print(f"The total price of your purchase is ${totalExtendedPrice:,.2f}")
        print("Thank you for your purchase!")
    else:
        print("Come again soon!")

def calculateExtendedPrice(quantity, price):
    extendedPrice = quantity * price
    if(extendedPrice > 10000):
        extendedPrice = extendedPrice * 0.9
    return extendedPrice

def inputInt(message):
    returnInt = None
    while returnInt == None:
        print(message)
        try:
            rawInt = int(input())
            if rawInt <= 0:
                raise
            returnInt = rawInt
            print()
        except: 
            print()
            print("Please enter a positive integer, ex 10")
    return returnInt

def inputDollar(message):
    returnFloat = None
    while returnFloat == None:
        print(message)
        try:
            rawFloat = float(input())
            if rawFloat <= 0:
                raise
            returnFloat = rawFloat
            print()
        except: 
            print()
            print("Please enter a dollar amount, ex 38.57")
    return returnFloat

main()