def main():
    file = open("StudentScores(p5).txt")

    studentData: dict[str, list[int]] = {}
    studentAverages: dict[str, float] = {}
    nameHeaderMessage = "Name"

    name = file.readline().strip()
    score = file.readline().strip()
    while name != "" and score != "":
        splitScores = score.split(",")
        processedScores = []
        for x in splitScores: processedScores.append(int(x))
        studentData[name] = processedScores

        name = file.readline().strip()
        score = file.readline().strip()

    # data processing loop
    longestKey = len(nameHeaderMessage)
    scoreSum = 0
    for key, val in studentData.items():
        if len(key) > longestKey: longestKey = len(key)
        studentAverages[key] = AverageList(val)
    testAverage = AverageScorePerTest(list(studentData.values()))

    # print loop
    headers = f"{"Name".rjust(longestKey)} | Average"
    print(headers)
    print("".ljust(len(headers) + 2, "-"))
    for key, val in studentAverages.items():
        print(f"{key.rjust(longestKey)} | {val:.2f}")
    print()
    for i in range(len(testAverage)):
        print(f"The average score for test {i + 1} was {testAverage[i]}")

def AverageList(list: list[int]) -> float:
    sum = 0
    for x in list: sum += x
    return sum / len(list)

def AverageScorePerTest(table: list[list[int]]) -> list[float]:
    scoresList = TransposeIntTable(table)
    averagesList: list[float] = []
    for scores in scoresList:
        averagesList.append(AverageList(scores))
    return averagesList

def TransposeIntTable(table: list[list[int]]) -> list[list[int]]:
    transposed: list[list[int]] = []
    longestList = 0
    for x in table: 
        if len(x) > longestList: longestList = len(x)
    for j in range(longestList):
        subList:list[int] = []
        for i in range(len(table)):
            try:
                subList.append(table[i][j])
            except IndexError: pass
        transposed.append(subList)
    return transposed


main()