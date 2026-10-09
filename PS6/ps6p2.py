def main():
    namesArr  = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Rodriguez", "Martinez"]
    scoresArr = [    287,       713,        673,     967,     709,      942,      405,     474,         781,        773]


    print("Print forward...")
    PrintArraysForward(namesArr, scoresArr)
    print()
    print("...and backward")
    PrintArraysReverse(namesArr, scoresArr)

def PrintArraysForward(array1, array2):
    if len(array1) != len(array2): raise BaseException("Arrays have different sizes")
    i = 0
    while i < len(array1):
        print(f"{array1[i]} -- {array2[i]}")
        i += 1

def PrintArraysReverse(array1, array2):
    if len(array1) != len(array2): raise BaseException("Arrays have different sizes")
    i = len(array1) - 1
    while i > -1:
        print(f"{array1[i]} -- {array2[i]}")
        i -= 1

main()