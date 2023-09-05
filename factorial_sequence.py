
'''
problem : Sequence of factorial number

steps : 1.Collect the input number from the user
        2.Generate the numbers upto user given number
        3.decreating 1 value for every iteration and store it
        4.after generating all the numbers, print the output.
'''	
num = int(input("Enter a factorial number: "))

for value in range(1, num + 1): #used the range() function for iteration
    factorial_sequence = num - value + 1 #decreating 1 value for every iteration 
    print("factorial sequence of given number is : ",factorial_sequence)
