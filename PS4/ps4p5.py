file = open("Students.txt")
totalTuition = 0
studentCount = 0


line = file.readline().strip()
lineNum = 1
while line != "":
    name = line
    line = file.readline().strip()
    lineNum += 1
    if (line.lower() == 'o'):
        rate = 500
    elif (line.lower() == 'i'):
        rate = 250
    else:
        print(f"Invalid district at line {lineNum}")
        raise 
    try:
        line = file.readline().strip()
        lineNum += 1
        credits = int(line)
        if credits < 0:
            raise
    except:
        print(f"Invalid number of credits at line {lineNum}")
        raise 

    tuition = credits * rate

    totalTuition += tuition
    studentCount += 1

    print(f"Mr/Ms. {name}, taking {credits} credits, owes ${tuition}")

    line = file.readline().strip()
    lineNum += 1

print()
print(f"The total tuition for this semester is ${totalTuition:,.2f}")
print(f"Total enrollment this semester at the Gardening Academy is {studentCount} students")

file.close()