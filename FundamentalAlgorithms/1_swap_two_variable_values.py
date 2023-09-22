#################################################################
######################## Method 1 ###############################
#################################################################

#using third variable

a = input("enter the value of 1st number (a): ")
b = input("enter the value of 2nd number (b): ")
print("\nbefore swapping, a = {} and b= {}".format(a,b))
t = a
a = b
b = t
print(f"after swapping, a = {a} and b = {b}")

#################################################################
######################## Method 2 ###############################
#################################################################

#using comma operator

a = input("enter the value of 1st number (a): ")
b = input("enter the value of 2nd number (b): ")
print("\nbefore swapping, a = {} and b= {}".format(a,b))
a,b = b,a
print(f"after swapping, a = {a} and b = {b}")

#################################################################
######################## Method 3 ###############################
#################################################################

#using XOR operator

a = int(input("enter the value of 1st number (a): "))       # by default python input is in string 
b = int(input("enter the value of 2nd number (b): "))       # hence converting to int for bitwise operators
print("\nbefore swapping, a = {} and b= {}".format(a,b))
a = a ^ b
b = a ^ b
a = a ^ b
print(f"after swapping, a = {a} and b = {b}")


#################################################################
######################## Method 4 ###############################
#################################################################

#using addition and subtraction operator

a = int(input("enter the value of 1st number (a): "))
b = int(input("enter the value of 2nd number (b): "))
print("\nbefore swapping, a = {} and b= {}".format(a,b))
a = a + b
b = a - b
a = a - b
print(f"after swapping, a = {a} and b = {b}")


#################################################################
######################## Method 5 ###############################
#################################################################

#using multiplication and division operator

a = int(input("enter the value of 1st number (a): "))
b = int(input("enter the value of 2nd number (b): "))
print("\nbefore swapping, a = {} and b= {}".format(a,b))
a = a * b
b = a / b
a = a / b
print("after swapping, a = {} and b = {}".format(int(a),int(b)))    #converting back to int just because i want uniformity in both the print statements (no decimals)

#################################################################
######################## Method 6 ###############################
#################################################################

#using bitwise addition and subtraction  operator
#little tricky

a = int(input("enter the value of 1st number (a): "))
b = int(input("enter the value of 2nd number (b): "))
print("\nbefore swapping, a = {} and b= {}".format(a,b))
a = (a & b) + (a | b)
b = a + (~b) + 1
a = a + (~b) + 1
print(f"after swapping, a = {a} and b = {b}")
