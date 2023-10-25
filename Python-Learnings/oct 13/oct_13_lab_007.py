# # ######################### OPERATORS ############################
#
# # print(3+4, 4-2, 4*2, 5//2, 4%2, 4**2, 4^3)
#
# thisIsMyVariableName=8
# print(thisIsMyVariableName)
# thisIsMyVariableName=thisIsMyVariableName+10
# thisIsMyVariableName+=10
# print(thisIsMyVariableName)
#
#
# t = [1,3,4,5,6,9]
# x=55
# y=15
# age =8
# print("You are allowed to watch movies" if age>18 else "You are a kid, watch POGO")
# # if not y>x:
# #     print( x+12 )
# # else:
# #     print(x-12)


number= int(input('enter the table\n'))
start= int(input('enter the start value'))
end= int(input('enter the end value'))
while start<=end:
    print(start, '*', number, '=' , start * number)
    start=start+1

