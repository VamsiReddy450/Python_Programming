
#factorial of a given number

num = int(input ("Enter the number: "))
Initial_value = 1
if num > 1:
    for value in range (1, num+1): #taken the range() function for iteration
        Initial_value=Initial_value *value #mutiplying 
print("Factorial of the given number is: ", Initial_value)








'''

Assignments in loops on 17-08-2023

*1.Factorial of a given number...done
2.if we give factorial number like 5, the output should be 5 4 3 2 1
*3.display first 5 multiples of 5...done
*4.input=[1,2,3,4,5], output should be [1,4,9,16,25] 
5.input=[1,2,3,4,-1,5,-5,6,-4], case1 : only print positive numbers..done
								case2 : when the negative number comes skip those
*6.patterns problem...done



Task1.Factorial of a given number :

what is factorial: 5!=5*4*3*2*1=120

step1 : take in the input from the user
step2 : 

'''

num = int (input ("Enter a number: "))
Initial_value = 1
if num<0:
    print("Please enter positive number")

if num > 1:
    for value in range (1, num+1):
        Initial_value=Initial_value *value
print("Factorial of the given number is: ", Initial_value)


num=