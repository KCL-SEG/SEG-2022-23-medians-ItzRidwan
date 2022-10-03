"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break
numbers.sort()
x = len(numbers)
if x%2 == 1:
    index = x//2
    median = numbers[index]
else:
    index1 = x//2 - 1
    index2 = x//2 
    median = (numbers[index1]+numbers[index2])/2
print(f'{median}')
