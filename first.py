# Factorial function with recursion
def factorial(val):
	# No negative values
	if val < 0:
		return -1
	# The factorial of 0 is 1
	elif val == 0:
		return 1
	# Recursively get the factorial
	else:
		return val * factorial(val - 1)

inputVal = -1

# Prompt for input until it is valid
while inputVal < 0:
	inputVal = int(input('Enter an integer: '))

# Print the result
print(factorial(inputVal))
