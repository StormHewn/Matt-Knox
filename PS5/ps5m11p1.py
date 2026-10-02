def main():
    quantity = inputInt("How many items would you like to buy?", lowerBound= 0)
    price = inputDollar("What is the unit price?")
    discountRate = (inputFloat("The item is ____% off unit price", lowerBound= 0, upperBound= 100) / 100)

    discountAmount, discountPrice = computeDiscountAmountAndPrice(quantity, price, discountRate)

    print(f"{quantity:,} items, at ${price:,.2f} per item, on a {(discountRate * 100):.1f}% discount, costs ${discountPrice:,.2f} and saves ${discountAmount:.2f}")

def computeDiscountAmountAndPrice(quantity, price, discountRate):
    simplePrice = quantity * price
    discountAmount = simplePrice * discountRate
    discountPrice = simplePrice - discountAmount
    return discountAmount, discountPrice

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

def inputInt(message, lowerBound = -1e6, upperBound = 1e6):
    returnInt = None
    while returnInt == None:
        print(message)
        try:
            rawInt = int(input())
            if ((rawInt < lowerBound) | (rawInt > upperBound)):
                raise
            returnInt = rawInt
            print()
        except: 
            print()
            if ((lowerBound == -1e6) & (upperBound == 1e6)):
                print("Please enter an integer")
            elif ((lowerBound == -1e6) & (upperBound != 1e6)):
                print(f"Please enter an integer less than {upperBound}")
            elif ((lowerBound != -1e6) & (upperBound == 1e6)):
                print(f"Please enter an integer greater than {lowerBound}")
            elif ((lowerBound != -1e6) & (upperBound != 1e6)):
                print(f"Please enter an integer between {lowerBound} and {upperBound}")
    return returnInt

def inputFloat(message, lowerBound = -1e6, upperBound = 1e6):
    returnFloat = None
    while returnFloat == None:
        print(message)
        try:
            rawFloat = float(input())
            if ((rawFloat < lowerBound) | (rawFloat > upperBound)):
                raise
            returnFloat = rawFloat
            print()
        except: 
            print()
            if ((lowerBound == -1e6) & (upperBound == 1e6)):
                print("Please enter an number")
            elif ((lowerBound == -1e6) & (upperBound != 1e6)):
                print(f"Please enter an number less than {upperBound}")
            elif ((lowerBound != -1e6) & (upperBound == 1e6)):
                print(f"Please enter an number greater than {lowerBound}")
            elif ((lowerBound != -1e6) & (upperBound != 1e6)):
                print(f"Please enter an number between {lowerBound} and {upperBound}")
    return returnFloat

main()