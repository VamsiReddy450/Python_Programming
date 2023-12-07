
'''
problem : Factorial of a given number

steps : 1.Collect the input number from the user
        2.Generate the numbers upto user given number
        3.Multiply the number and store it
        4.after generating all the numbers, print the output.

'''
num = int(input ("Enter the number: "))
Initial_value = 1
if num<0:
    print("Please enter the positive numbers only")
else:
    for value in range (1, num+1): #taken the range() function for iteration
        Initial_value=Initial_value *value #mutiplying 
print("Factorial of the given number is: ", Initial_value)


num=int(input("Enter the number: "))
Initial_value=1
if num < 0:
    print("Factorial of given numbers is not defined for negative numbers")
elif num == 0 or num == 1:
    print("Factorial of the given number is: ", Initial_value)
else:
    for i in range(2, num + 1): #taken the range() function for iteration
        Initial_value *= i #mutiplying
    print("Factorial of the given number is:",Initial_value)





