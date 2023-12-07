'''
Generate the first n terms of the sequence
1 2 4 8 16 32 ...
without using multiplication
'''

def sequence(n):
    seq = []
    for i in range(1, n+1):
        ele = 2**(i-1)
        seq.append(ele)
    return seq

n = int(input("Enter the number of elements to be printer in the series 1, 2, 4, 8, 16, ...: "))
print(str(sequence(n))[1:-1])