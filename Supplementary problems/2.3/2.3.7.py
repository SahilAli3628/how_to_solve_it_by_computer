'''
Develop an algorithm that prints out n values of the sequence
1, -1, 1, -1, 1, -1, ....
'''

def sequence(n):
    seq_list = []
    for i in range(1, n+1):
        if i % 2 != 0:
            seq_list.append(1)
        else:
            seq_list.append(-1)
    return seq_list

num = int(input("Enter the max number of elements to be printed in the series 1, -1, 1, -1, 1, -1, ... : "))
print(str(sequence(num))[1:-1])