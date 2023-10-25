# Use the ternary operator to find the maximum of three numbers entered by the user.

num1=int(input('enter the 1st number\n'))
num2=int(input('enter the 2nd number\n'))
num3=int(input('enter the 3rd number\n'))
max=None
if num1>num2 and num1>num3:
    max= num1
elif num2>num1 and num2>num3:
    max=num2
else:
    max=num3
print("The Maximum number out of {} {} and {} is {} ".format(num1,num2,num3,max))
