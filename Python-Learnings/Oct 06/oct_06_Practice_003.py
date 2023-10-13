# # user_input = int(input('give me number to print  table\n'))
# # for x in range(1, 11, ):
# #     print(f"{user_input} *  {x} = {x * user_input}")
#
# # write a program for calculator with print formatting f method
# num1= int(input('Enter the 1st number\n'))
# num2= int(input('enter the 2nd number\n'))
# print(f"Addition of {num1} & {num2} number = {num1+num2}")
# print(f"Subtraction of {num1} & {num2} number = {num1-num2}")
# print(f"Multiplication of {num1} & {num2} number = {num1*num2}")
# print(f"Division of {num1} & {num2} number = {num1/num2}")

#
# # Print odd numbers from 1 to 100
# # method 1
# for i in range(1,101,2):
#     print(i)
#
# # method2
# jak=[]
# for i in range(1,101,2):
#     jak.append(i)
# print(jak)


user_name= input('enter the username\n')
password= input('enter the password\n')

db_username= 'Shailbi_shukla'
db_password= 'Shailbi@123'

if user_name==db_username and password==db_password:
    print('Successfully login')
else:
    print('incorrect username/password')

s='This is a cat'
print(s[10:13])


