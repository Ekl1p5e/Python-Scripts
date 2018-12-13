import math

# Prompt for 2 numbers, a and b
intargs = input('Enter 2 integer numbers (separated by space): ')

# Split input by space
intlist = list(map(int, intargs.split()))

# Get highest and lowest integers
low = min(intlist)
hi = max(intlist)

# Get sequence of numbers between (low, hi)
primeSeq = range(low + 1, hi)

# Filter multiples out
for i in range(2, int(math.sqrt(hi))):
	primeSeq = list(filter(lambda x: x % i != 0, primeSeq))

symbolInd = 0
symbolList = [':', '!', ',']
primeList = []

while len(primeSeq) > 0:
	primeList.append(str(primeSeq.pop(0)))
	primeList.append(symbolList[symbolInd % 3])
	symbolInd = symbolInd + 1

print(''.join(primeList))
