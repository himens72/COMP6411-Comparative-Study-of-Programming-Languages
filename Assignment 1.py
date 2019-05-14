import random
words = []
currentGuess = ""
def readFile():
    print("Inside Read File Function")
    input_files = open("four_letters.txt", "r+")
    print("Name of the file : ", input_files.name)
    for line in input_files:
        line = line.strip()
        line = line.split(" ")
        for x in line:
            words.append(x)

def selectOption():
    option = input();
    if "g" == option:
        print("Guess Option selected")
    elif "t" == option:
        print("Tell me Option selected")
    elif "l" == option:
        print("Letter Option selected")
    elif "q" == option:
        print("Quit Option selected")
    else:
        print("Please Select Proper Option")
        print("g = guess, t = tell me, l for a letter, and q to quit")
        selectOption()

print("Call Read File Function")
readFile()
print("Words in Repo : ",len(words))
currentGuess = words[random.randint(0,len(words))]
print("Initial Guess : ",currentGuess)
print("** The great guessing game **")
print("g = guess, t = tell me, l for a letter, and q to quit")
print("Current Guess: _ _ _ _")
print("Call Select Input Function")
selectOption()
print("End Select Option")