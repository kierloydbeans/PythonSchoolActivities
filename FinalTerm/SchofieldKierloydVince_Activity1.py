# Schofield, Kierloyd Vince V.
# BSIS 3B
# Activity 1 - Word Bank
# Time started: 1:15PM
# Time finished: 1:34PM

# ask the user to input a word (input)
# store the word in a list (append)
# ask if the user wanna try again (while True)
# if yes, back to step 1
# if no, display the total number of words and all the words in the list (print)

words = []  # start with empty list

while True:  # looping through the whole code

    wordInput = input('Enter word: ')
    words.append(wordInput)  # storing

    if (input("Do you want to continue? (Y/y or N/n): ")).lower() != 'y':  # again or no
        print("\nRegistered Words \n")
        print(f"The number of words in the bank: {len(words)}")  # number of registered words
        print(f"The words in the bank:")
        for x in range(len(words)):  # looping through the list
            print(words[x])
        break