# List to store values
numbers = list(map(int, input().split()))

# Get values and store in list
sum = 0         # Variable for sum of values in list
for i in range(len(numbers)):
    numbers[i] = int(numbers[i])
    sum += numbers[i]

# Calculate avg from sum
avg = sum / len(numbers)

# New list to store difference from avg values
difference = []

# Get difference from avg values and store in new list
i = 0
for i in range(len(numbers)):
    diff = avg - numbers[i]
    if diff < 0:
        diff = diff * -1
    print(f'{diff:.2f}', end = ' ')

# Use this statement to print out the list element. # Replace the variable 'dist' with your variable
# print (f'{dist:.2f}', end=' ')

