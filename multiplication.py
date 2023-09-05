
'''
problem : multiplication with it self number

steps : 1.Take the list with some values
        2.Take the empty list to store the values after generating
        3.Do the loop for the list
        4.Multiply the number with sqaure
        5.Add the multiplied value in to the empty list
        5.after adding all the numbers, print the empty list.
        

'''
input_list = [1, 2, 3, 4, 5]
multiplied_list=[]
for num in input_list:
    multiply = num ** 2 #if we give one * instead of **, the value will multipy with 2 only. if we give two **,the value will multiply itself with twice.
    multiplied_list+=[multiply]
print(multiplied_list)
