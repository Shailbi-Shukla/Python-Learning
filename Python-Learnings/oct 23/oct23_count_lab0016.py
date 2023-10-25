# Task 1
# ✅ Count vowels and consonants in a String
# aeiou
# input = pramod
# vol = 2

name=input('enter the string\n')
count=0
vowels= 'aeiou'
for char in name:
    if char in vowels:
        count=count+1
print(count)



