# Read in file
intfile = input()

# Split file by space
intlist = list(map(int, intfile.split()))

# Divide sum of integers by number of integers
print(sum(intlist) / len(intlist))
