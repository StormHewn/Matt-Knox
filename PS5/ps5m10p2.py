def main():
    TotalPrice = 0
    print("Do you want to begin your purchase? (Y/n)")
    repeatFlag = input()
    print()
    loopEntered = False
    while repeatFlag.lower().count("n") == 0:
        loopEntered = True

        make = inputAlphaNum("Please enter the make you would like to purchase")
        model = inputAlphaNum("Please enter the model you would like to purchase")
        msrp = inputDollar("Please enter the sticker price of your car")
        isElectric = inputBool("Would you like the electric model?")

        priceMultiplier = 0.95
        if ((make == "Honda") & (model == "Accord")):
            priceMultiplier = 0.90
        if ((make == "Toyota") & (model == "Rav4")):
            priceMultiplier = 0.85
        elif isElectric:
            priceMultiplier = 0.70

        priceOfCar = msrp * priceMultiplier * 1.07

        print(f"The price of a {make} {model} is ${priceOfCar:,.2f}")
        print()
        TotalPrice += priceOfCar

        print("Do you want to add another car? (Y/n)")
        repeatFlag = input()
        print()

    if (loopEntered):
        print(f"The total cost of your purchase is ${TotalPrice:,.2f}")

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

def inputBool(message):
    returnBool = None
    while returnBool == None:
        print(message + " (y/n)")
        rawBool = input().lower()
        if (rawBool.count("y") > 0) | (rawBool == "true"):
            returnBool = True
        elif (rawBool.count("n") > 0) | (rawBool == "false"):
            returnBool = False
        else:
            print()
            print("Please enter a valid boolean value")
    print()
    return returnBool

def inputAlphaNum(message):
    returnString = None
    while not((returnString != None) and (returnString.isalnum())):
        print(message)
        stringInput = input()
        print()
        if not(stringInput.isalnum()):
            print("Please enter only letters and numbers, no symbols")
        else:
            returnString = stringInput.title()
    return returnString

main()