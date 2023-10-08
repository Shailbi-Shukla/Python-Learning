# Take a input from a user and print the table

# Task 1
user_input= int(input('give me number to print  table\n'))
max_value= user_input * 11
min_value= user_input * 1
x=list(range(min_value,max_value,user_input))
print(x)


# # Take a input from a user and print the table-Type-2
user_input= int(input('give me number to print  table\n'))
for x in range(1,11,):
    print(user_input ,'*' , x , '=', x * user_input)


# # How to use the print with formatting f-Type3
user_input = int(input('give me number to print  table\n'))
for x in range(1, 11, ):
    print(f"{user_input} *  {x} = {x * user_input}\n")



# Prints today's date with help of datetime library

import datetime

today = datetime.datetime.today()
print(f"{today:%d %B, %Y}")

