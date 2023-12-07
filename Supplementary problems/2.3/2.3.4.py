'''
Harmonic mean of first n numbers.
Formula H = n/summation(1/n)

Note: summation(n) = 1+2+3+...+n
'''

def harmonic(num):
    sum = 0
    for i in range(1, num + 1):
        sum += i
    h = num/(1/sum)
    return h

n = int(input("Enter the number to calculate Harmonic mean: "))
print("Harmonic mean of first {} numbers is {}".format(n,harmonic(n)))