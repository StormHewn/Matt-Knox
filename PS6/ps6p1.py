def main():
    arr = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Rodriguez", "Martinez"]

    print("Print forward...")
    PrintArrayForward(arr)
    print()
    print("...and backward")
    PrintArrayReverse(arr)

def PrintArrayForward(array):
    i = 0
    while i < len(array):
        print(array[i])
        i += 1

def PrintArrayReverse(array):
    i = len(array) - 1
    while i > -1:
        print(array[i])
        i -= 1

main()