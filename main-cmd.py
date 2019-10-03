# Caleb Freeman
# Brandon Sharp

print("Please enter input file name")

with open(input(), 'rU') as f:
    dataArray = []
    lines = f.read().split()
    try:
        for line in lines:
            dataArray.append(line)
    except ValueError:
        # writing error output to output file
        with open('WordsCounts.txt', 'w') as the_file:
            the_file.write('Exception: Input file must only contain...\n')
        exit(1)

    len = len(dataArray)
for x in range(len):
    print(dataArray[x])
