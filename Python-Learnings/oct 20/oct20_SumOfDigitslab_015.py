# #2 Task
# Sum of Digits: Create a function that calculates the sum of the digits of a positive integer.
# n = 12345
# sum = 15
# n = 123
# sum = 6

number = int(input('enter the number\n'))
sumOfDigits = 0
for i in range(0, len(str(number))):
    rem = number % 10
    number = number // 10
    sumOfDigits = sumOfDigits + rem
print(sumOfDigits)
