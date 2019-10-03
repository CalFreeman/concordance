# Caleb Freeman
# Brandon Sharp

print("Please enter input file name")

with open(input(), 'rU') as f:
    dataArray = []
    lines = f.read().split()
    try:
        for line in lines:
            for ch in line:
                dataArray.append(ch)
    except ValueError:
        # writing error output to output file
        with open('WordsCounts.txt', 'w') as the_file:
            the_file.write('Exception: Input file must only contain...\n')
        exit(1)

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
