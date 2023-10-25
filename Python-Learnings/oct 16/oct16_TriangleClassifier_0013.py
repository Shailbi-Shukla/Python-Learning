# Write a program that classifies a triangle based on its side lengths.
# Given three input values representing the lengths of the sides, determine if the triangle is equilateral (all sides are equal), isosceles (exactly two sides are equal), or scalene (no sides are equal).
#
# Use an if-else statement to classify the triangle.
# 3 Input
# side 1, side 2 and side 3
# output - Eq, Iso, Scalene -
# Eq. = side 1 == side 2 = side 3

a=int(input('enter the sideA\n'))
b=int(input('enter the sideB\n'))
c=int(input('enter the sideC\n'))
if a==b and b==c and c==a :
    print('Equilater Triangle')
elif a==b or b==c or c==a:
    print('Iso triangle')
else:
    print('Scalene Triangle')
