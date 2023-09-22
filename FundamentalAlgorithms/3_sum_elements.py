#NOTE: USE ONLY 1 METHOD AND COMMENT OUT THE REST


input_string = input("Enter the list of numbers to be added: ")
num_list = input_string.split()
num_list = list(map(int, num_list))

#method 1: using for loop
total = 0
for ele in num_list:
    total += ele

#method 2: using while loop
total = 0
ele = 0
while (ele < len(num_list)):
    total += num_list[ele]
    ele += 1

#method 3: using recursive approach
def listSum(mylist, size):
    if (size == 0):
        return 0
    else:
        return mylist[size - 1] + listSum(mylist, size - 1)

total = listSum(num_list, len(num_list))

#method 4: using sum() method
total = sum(num_list)

#method 5: using add() from operator module
from operator import *
total = 0
for ele in num_list:
    total = add(ele , total)

#method 6: using enumerate (IMO not worth it)
total = 0
for i,ele in enumerate(num_list):
    total += ele

#method 7: using list comprehension (IMO not worth it)
total = [num for num in num_list]
total = sum(total)

#method 8: using lambda funtion
total = sum(list(filter(lambda i: (i), num_list)))

print("Sum of all the elements in the given list: ", total)
