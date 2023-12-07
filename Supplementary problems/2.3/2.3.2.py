'''
Redesign the 2.3.1 approach so that it only needs to perform n-1 additions to sum n numbers.
'''
def average(num):
    if num == 1:
        return 1
    sum = 1
    for i in range(2, num+1):
        sum += i
    average = sum/num
    return average

n = int(input("Enter the number to calculate average of: "))
print(f"Average of first {n} numbers is: {average(n)}")