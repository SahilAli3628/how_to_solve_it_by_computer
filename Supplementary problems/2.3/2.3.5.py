'''
Develop an algorithm to compute the sums for first n terms (n >=0) of the following series:
a) s = 1+2+3+....
b) s = 1+3+5+...
c) s = 2+4+6+...
d) s = 1+1/2+1/3+...
'''

def sum_a(num):
    if num == 1:
        return 1
    else:
        sum = 0
        for i in range(1, num+1):
            sum += i
        return sum

def sum_b(num):
    if num == 1:
        return 1
    else:
        sum = 0
        count = 1
        i = 1
        while count <= num:
            if i % 2 != 0:
                sum += i
                i += 1
                count += 1
            i += 1
        return sum

def sum_c(num):
    if num == 1:
        return 2
    else:
        sum = 0
        count = 1
        i = 1
        while count <= num:
            if i % 2 == 0:
                sum += i
                i += 1
                count += 1
            i += 1
        return sum

def sum_d(num):
    if num == 1:
        return 1
    else:
        sum = 0
        for i in range(1, num+1):
            sum += i**-1
        return sum

print("Compute the sums for first n terms (n >=0) of the following series: \na) s = 1+2+3+....\nb) s = 1+3+5+...\nc) s = 2+4+6+...\nd) s = 1+1/2+1/3+...")
series = input("Enter the series number (a, b, c, d): ")
n = int(input("Enter the upper limit whole number: "))

if series == "a":
    print("The sum for series a =",sum_a(n))
elif series == "b":
    print("The sum for series b =",sum_b(n))
elif series == "c":
    print("The sum for series c =",sum_c(n))
else:
    print("The sum for series d =",sum_d(n))