def main():
    file = open("StudentScores(p3-4).txt")

    studentInfo = {}

    name = file.readline().strip()
    score = file.readline().strip()
    while name != "" and score != "":
        studentInfo[name] = int(score)
        name = file.readline().strip()
        score = file.readline().strip()

    highestEntry = ("", 0)
    lowestEntry  = ("", 1000)

    for key, val in studentInfo.items():
        if val > highestEntry[1]: highestEntry = (key, val)
        if val < lowestEntry[1]:  lowestEntry  = (key, val)

    print(f"The highest score was {highestEntry[1]}, acheived by {highestEntry[0]}")
    print( f"The lowest score was {lowestEntry[1] }, acheived by {lowestEntry[0] }")

main()