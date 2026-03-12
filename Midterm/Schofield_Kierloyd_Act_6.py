# Schofield, Kierloyd Vince
# BSIS 3B
# Activity 6

noOfNum = int(input("Enter a number: ")) # get the limit

totalSum = 0 # start at 0 sum
currentNum = 1 # kung ilan yung nadadagdag

while currentNum <= noOfNum: # looping
    totalSum = totalSum + currentNum # computation
    currentNum = currentNum + 1 # increment

print(f"Summation: {totalSum}")