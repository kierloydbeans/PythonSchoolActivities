# Schofield, Kierloyd Vince V.
# BSIS 3B
# 3/17/26
# Practical 3

try:
    with open("data.txt", "r") as fr:
        lines = fr.readlines()
        for line in lines:
            cleanLine = line.strip()
            if cleanLine:
                print(cleanLine.upper())
                print(f"Total number of words: {len(cleanLine.split())}")
        fr.close()

except FileNotFoundError:
    print("File does not exists.")

# EXPECTED OUTPUT
# PYTHON PROGRAMMING ESSENTIAL COURSE
# Total number of words: 4
#
# THE QUICK BROWN FOX JUMPS OVER A LAZY DOG
# Total number of words: 9
