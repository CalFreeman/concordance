# Caleb Freeman
# Brandon Sharp

print("Please enter input file name")
try:
    with open(input(), 'rU') as f:
        wordArray = []
        charArray = []
        lines = f.read().split()
        try:
            for line in lines:
                wordArray.append(line)
                for ch in line:
                    charArray.append(ch)
        except ValueError:
            # writing error output to output file
            with open('WordsCounts.txt', 'w') as the_file:
                the_file.write('Exception: Input file must only contain...\n')
            exit(1)
except FileNotFoundError:
    print("File does not exist\n")

lenW = len(dataArray)

for x in range(lenW):
    print(dataArray[x])
#    characters = []
#    for letter in (dataArray[x]):
#        characters.append(letter)

#lenC = len(characters)

#for x in range(lenC):
#    print(characters[x])

print("")
print("done...")
