#print postive numbers only

list_nums=[1,2,3,4,-1,-2,-3,-4,8,9,7]
empty_list=[]

for value in list_nums:
    if value>=0:
        empty_list=empty_list+[value]
print(empty_list)
