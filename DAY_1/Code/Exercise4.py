# Write a program that switches the values stored in the variables a and b.

# Example input
# a: 5
# b: 3 

# Example output
# a: 3
# b: 5

a = input("a: ")
b = input("b: ")

####################################
# Logic
temp = a 
a=b
b=temp

####################################
print("\n After Swapping")
print("a: " + a)
print("b: " + b)