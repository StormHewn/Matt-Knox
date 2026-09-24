file = open("Employees.txt")
totalBonuses = 0.0

line = file.readline().strip()
lineNum = 1
while line != "":
    name = line
    line = file.readline().strip()
    lineNum += 1
    try:
        salary = float(line)
    except:
        print(f"Invalid salary at line {lineNum}")
        raise 

    if (salary >= 100000.0):
        rate = 0.20
    elif (salary >= 50000.0):
        rate = 0.15
    else:
        rate = 0.10
    bonusAmount = salary * rate

    totalBonuses += bonusAmount

    line = file.readline().strip()
    lineNum += 1

print(f"The total amount of bonuses paid out is ${totalBonuses:,.2f}")

file.close()