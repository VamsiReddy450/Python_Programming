#sequence of factorial number
	
num = int(input("Enter a factorial number: "))

for value in range(1, num + 1): #used the range() function for iteration
    factorial_sequence = num - value + 1 #decreating 1 value for every iteration 
    print("factorial sequence of given number is : ",factorial_sequence)
