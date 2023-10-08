# Take a input from a user and print the table

# user_input= int(input('give me number to print  table\n'))
# max_value= user_input * 11
# min_value= user_input * 1
# x=list(range(min_value,max_value,user_input))
# print(x)

user_input= int(input('give me number to print  table\n'))
for x in range(1,11,):
    print(user_input ,'*' , x , '=', x * user_input)

