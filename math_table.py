#math_table

occurance_num=int(input("Enter the occurances : "))
table_num=int(input("Enter number which table you want : "))
for value in range(1, occurance_num+1): #used the range() function for iteration
    multiple = table_num * value #multiply the table number with variable name called value
    print(multiple)