list =[]
number_1 = int(input("Number: "))
list.append(number_1)
number_2 = int(input("Number: "))
list.append(number_2)
number_3 = int(input("Number: "))
list.append(number_3)
number_4 = int(input("Number: "))
list.append(number_4)
number_5 = int(input("Number: "))
list.append(number_5)

print("The first number is: "+ str(list[0]))
print("The last number is: "+ str(list[4]))
print("The smallest number is: "+ str(min(list)))
print("The largest number is: "+ str(max(list)))
print("The average of the numbers is: "+ str(sum(list)/len(list)))

usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
name= str(input("Enter your username: "))
if name in usernames:
    print("Access Granted")
else:
    print("Access denied")