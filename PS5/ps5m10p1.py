import math

def main():
    print("Do you want to begin entering sales data? (Y/n)")
    repeatFlag = input()
    print()
    while repeatFlag.lower().count("n") == 0:

        lastName = inputName("Please input the salesman's last name")
        month = inputMonth()
        sales = inputInt(f"How many sales did {lastName} make?")

        forecastPercent = 1.00
        match month:
            case "Jan" | "Feb" | "Mar":
                forecastPercent = 1.10
            case "Apr" | "May" | "Jun":
                forecastPercent = 1.15
            case "Jul" | "Aug" | "Sep":
                forecastPercent = 1.20
            case "Oct" | "Nov" | "Dec":
                forecastPercent = 1.25
            case _:
                raise Exception(f"An invalid month slipped through: {month}")

        forecastedSales = math.ceil(sales * forecastPercent)

        print(f"{lastName} should make {forecastedSales} sales next month")
        print()

        print("Do you want to continue entering data? (Y/n)")
        repeatFlag = input()
        print()

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

def inputName(message):
    returnString = None
    while not((returnString != None) and (returnString.isalpha())):
        print(message)
        stringInput = input()
        print()
        if not(stringInput.isalpha()):
            print("Please enter only letters, no numbers or symbols")
        else:
            returnString = stringInput.title()
    return returnString

def inputMonth():
    validMonths = ["Jan", "Feb", "Mar"
                   "Apr", "May", "Jun"
                   "Jul", "Aug", "Sep"
                   "Oct", "Nov", "Dec"]
    returnMonth = None
    while returnMonth == None:
        print("Please enter the first three letters of a month (Jan, Feb, Mar, etc)")
        stringInput = input().title()
        print()
        if validMonths.count(stringInput) == 0:
            print("Please enter a valid month")
        else:
            returnMonth = stringInput
    return returnMonth

main()