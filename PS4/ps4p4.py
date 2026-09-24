file = open("Inventory.txt")
totalExtendedPrices = 0.0
orderCount = 0

line = file.readline().strip()
lineNum = 1
while line != "":
    item = line
    try:
        line = file.readline().strip()
        lineNum += 1
        count = int(line)
    except:
        print(f"Invalid count at line {lineNum}")
        raise 
    try:
        line = file.readline().strip()
        lineNum += 1
        cost = float(line)
    except:
        print(f"Invalid cost at line {lineNum}")
        raise 

    extendedPrice = cost * count

    totalExtendedPrices += extendedPrice
    orderCount += 1

    line = file.readline().strip()
    lineNum += 1

print(f"The total cost of your purchase is ${totalExtendedPrices:,.2f}")
print(f"The number of orders is {orderCount}")
print(f"The average price of an order is {totalExtendedPrices / orderCount}")

file.close()