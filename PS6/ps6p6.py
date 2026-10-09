def main():
    file = open("BattingAverages.txt")

    playerData: dict[str, float] = {}
    nameHeaderMessage = "Name"

    data = file.readline().strip()
    while data != "":
        record = tuple(data.split(": "))
        playerData[record[0]] = float(record[1])
        data = file.readline().strip()

    # data processing loop
    longestKey = len(nameHeaderMessage)
    scoreSum = 0
    for key, val in playerData.items():
        if len(key) > longestKey: longestKey = len(key)
        scoreSum += val
    scoreAvg = scoreSum / (len(playerData))

    # print loop
    headers = f"{"Name".rjust(longestKey)} | Batting Average"
    print(headers)
    print("".ljust(len(headers) + 2, "-"))
    for key, val in playerData.items():
        average = f"{val:.3f}"
        print(f"{key.rjust(longestKey)} | {average[1:]}")

main()