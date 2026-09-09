wages = None

while wages == None:
    print("Please enter your collective wages")
    try:
        floatInput = float(input())
        if (floatInput != round(floatInput, 2)):
            raise
        else:
            wages = floatInput
            print()
    except: 
        print()
        print("Please enter a dollar amount, ex 3.78")

wagesRemaining = wages % 0.03
wagesPerPartner = (wages - wagesRemaining) / 3
print(f"Each partner whould get ${wagesPerPartner:.2f}, with {round(wagesRemaining * 100)}¢ left over.")