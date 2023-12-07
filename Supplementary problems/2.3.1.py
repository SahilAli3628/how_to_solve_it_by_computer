"""
Design an algorithm to compute the average of n numbers
"""

def average(num):
    sum = 0
    for i in range(num+1):
        sum += i
    average = sum/num
    return average

n = int(input("Enter the number to calculate average of: "))
print(f"Average of first {n} numbers is: {average(n)}")

"""
another faster way to calculate sum first n numbers:
n = int(input())
print(n * (n+1) // 2)

A note about the division (//) (in Python 3): As you might know, there are two types of division 
operators in Python. In short, / will give a float result and // will give an int. In this case, we 
could use both operators, the only difference will be the returned type, but not the value. Since 
multiplying an odd with an even always gives an even number, dividing that by 2 will always be a 
whole number. In other words - n*(n+1) // 2 == n*(n+1) / 2 (but one would be x and the 
other x.0, respectively).
"""