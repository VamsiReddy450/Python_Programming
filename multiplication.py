#multiplication

input_list = [1, 2, 3, 4, 5]
multiplied_list=[]
for num in input_list:
    multiply = num ** 2 #if we give one * instead of **, the value will multipy with 2 only. if we give two **,the value will multiply itself with twice.
    multiplied_list+=[multiply]
print(multiplied_list)
