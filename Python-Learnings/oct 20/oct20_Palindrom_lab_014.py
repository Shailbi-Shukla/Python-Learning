# #1 Task
# Palindrome Checker:
# Create a function that checks if a given string is a palindrome (reads the same forwards and backward). 121
# Example - pramod
# madam - reverse(madam) -> same
# Naman -> reverse -> same
# Malayalam
# Compare String with the Revserse of the string

string= input('enter the string\n')
reverse_string=string[::-1]
if string==reverse_string:
    print('String is palindrom')
else:
    print('string is not palindrom')