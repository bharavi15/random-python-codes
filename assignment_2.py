# Python operators
# Arithmetic operators
# + - Addition, - - Subtraction, * - Multiplication, / - Division, % - Modulus, // - Floor division
# a = 3
# b = 2
# q = 3/2
# print(q, type(q))
# p = 3//2
# print(p, type(p))
# Comparison operators
# > - GT, < - LT, == - E, != - NE, >= - GTE, <= LTE
# Are both statements same: a = 1/2 and a = 1/2.0
# a = 1/2
# b = 1/2.0
# print(a, b, type(a), type(b))
# Both are same
# Logical operators
# and, or, not
# l = [1, 2, 4, 5] find the missing number using logical operators
# Bit-wise operators
# & - Bitwise AND, | - Bitwise OR, ~ - Bitwise NOT, ^ - Bitwise XOR, << - Bitwise left shift, >> - Bitwise right shift
# Identity operators
# is, is not
# Membership operators
# in, not in
# if-else syntax
# if <condition>:
# elif <condition>:
# else <condition>:
# Output of the following:
# x,y,z= 1,2,x**3  #Error
# print(x,y,z)
# x = 1
# y = 2
# z = y**3
# print(x,y,z)


# Task 1: Print the grade according to marks
marks = int(input("Enter the marks: "))
if marks>=91:
    print(10)
elif marks>=81:
    print(9)
elif marks>=71:
    print(8)
elif marks>=61:
    print(7)
elif marks>=51:
    print(6)
else:
    print("Fail")

# for loop
# for i in range(5):
#     print(i)
# while loop
# i = 0
# while(i<5):
#     print(i)
#     i += 1

# print([i for i in [5, 2, 3] if i%2 ==0])
# Task 2: Reverse the strings in a list using list comprehension
l1 = ['abc', 'def', 'ghi']
l2 = [i[::-1] for i in l1]
print(l2)
