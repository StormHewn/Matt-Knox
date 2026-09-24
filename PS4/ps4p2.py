startValue = None
stopValue  = None
increment  = None

while startValue == None:
    print("Please enter a starting value")
    try:
        startValue = int(input())
        print()
    except:
        print()
        print("Please enter an integer, ex 4")
while stopValue == None:
    print("Please enter a stopping value (inclusive)")
    try:
        rawInt = int(input())
        if (rawInt < startValue):
            raise
        else:
            stopValue = rawInt
            print()
    except:
        print()
        print(f"Please enter an integer greater than {startValue}")
while increment == None:
    print("Please enter an increment amount")
    try:
        increment = int(input())
        print()
    except:
        print()
        print("Please enter an integer, ex 4")

index = startValue
while index <= stopValue:
    print(index)
    index += increment