# Schofield, Kierloyd Vince
# BSIS 3B
# Activity 7

noOfNum = int(input("Enter a number: ")) # get the limit

totalProduct = 1 # start at 1, not 0
currentNum = 1 # kung ilan yung nadadagdag

while currentNum <= noOfNum: # looping
    totalProduct = totalProduct * currentNum # computation
    currentNum = currentNum + 1 # increment

print(f"Factorial: {totalProduct}")

