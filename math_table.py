
'''

problem : math_table

steps : 1.Collect the input table number from the user
        2.Collect the input occurance number from the user
        3.Generate the numbers upto user given number
        4.Multiply the number and store it
        5.after generating all the numbers, print the output.
        
'''

table_num=int(input("Enter number which table you want : "))
occurance_num=int(input("Enter the occurances : "))
for value in range(1, occurance_num+1): #used the range() function for iteration
    multiple = table_num * value #multiply the table number with variable name called value
    print(multiple)