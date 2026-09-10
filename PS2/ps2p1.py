firstScore  = None
secondScore = None

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

firstWeightedScore  = firstScore  * 0.6
secondWeightedScore = secondScore * 0.4
totalScore = firstWeightedScore + secondWeightedScore

print(f"Your total score is {totalScore}.")