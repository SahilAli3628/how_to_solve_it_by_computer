'''
Design an algorithm to compute the sum of the squares of n numbers.
'''

def squareSum(num):
    if num == 1:
        return 1
    sum = 1
    for i in range(2, num+1):
        sum += i*i
    return sum

n = int(input("Enter the number to calculate sum of the squares of: "))
print(f"sum of the squares of first {n} numbers is: {squareSum(n)}")