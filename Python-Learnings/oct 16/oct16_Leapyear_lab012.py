# ✅ Leap Year Checker:
# Create a program that determines whether a given year is a leap year.
# A leap year is divisible by 4, but not by 100 unless it is also divisible by 400.
# Use an if-else statement to make this determination.
# Input = 2024
# Output = Leap year

year= int(input('enter the year\n'))
if year%4==0 and year%100!=0 or year%400==0:  #doubt hai
    print('year is leap year')
else:
    print('year is not leap year')