studentCount = 0

print("Do you want to enter the loop? (Yes/No)")
answer = input()
print()

while answer.lower().count("y") > 0:
    lastName = None
    firstScore = None
    secondScore = None
    while not((lastName != None) and (lastName.isalpha())):
        print("Please enter your last name")
        stringInput = input()
        if not(stringInput.isalpha()):
            print()
            print("Please enter only letters, no numbers or symbols")
        else:
            lastName = stringInput.title()
            print()
    while firstScore == None:
        print("Please enter your first exam score")
        try: 
            firstScore = int(input())
            print()
        except: 
            print()
            print("Please enter an integer, ex 40")
    while secondScore == None:
        print("Please enter your second exam score")
        try:
            secondScore = int(input())
            print()
        except: 
            print()
            print("Please enter an integer, ex 40")

    averageScore = (firstScore + secondScore) / 2

    print(f"Mr/Ms. {lastName} has an average score of {averageScore}")

    studentCount += 1

    print("Do you want to enter another student record? (Yes/No)")
    answer = input()
    print()

print(f"{studentCount} student records were entered")