# Write a program that calculates and displays the letter grade for a given numerical score (e.g., A, B, C, D, or F) based on the following grading scale:
# input- score - 89
# output- B
# A: 90-100
# B: 80-89
# C: 70-79
# D: 60-69
# F: 0-59

marks= int(input('enter the marks\n'))
if marks>=90 and marks<=100:
    print('A')
elif marks>=80 and marks<=89:
    print('B')
elif marks>=70 and marks<=79:
    print('C')
elif marks>=60 and marks<=69:
    print('D')
else:
    print('F')