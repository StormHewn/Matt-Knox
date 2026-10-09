def main():
    file = open("StudentScores(p3-4).txt")

    studentData = {}
    nameHeaderMessage = "Name"
    averageScoreMessage = "Average"

    name = file.readline().strip()
    score = file.readline().strip()
    while name != "" and score != "":
        studentData[name] = int(score)
        name = file.readline().strip()
        score = file.readline().strip()

    # data processing loop
    longestKey = max(len(nameHeaderMessage), len(averageScoreMessage))
    scoreSum = 0
    for key, val in studentData.items():
        if len(key) > longestKey: longestKey = len(key)
        scoreSum += val
    scoreAvg = scoreSum / (len(studentData))

    # print loop
    headers = f"{"Name".rjust(longestKey)} | Average"
    print(headers)
    print("".ljust(len(headers) + 2, "-"))
    for key, val in studentData.items():
        print(f"{key.rjust(longestKey)} | {val}")
    print("".ljust(len(headers) + 2, "-"))
    print(f"{averageScoreMessage.rjust(longestKey)} | {scoreAvg:.2f}")

main()