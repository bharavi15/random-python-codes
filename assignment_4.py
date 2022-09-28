
# def add_two(a,b):
#     return a + b

# def add_three(a,b,c):
#     print(a+b+c)
# # TASK 1 - Write a function to return a given number as prime or not 
from math import sqrt


def isPrime(x):
    for i in range(2, int(sqrt(x))+1):
        if x % i == 0:
            return False
    return True

# add_three(1,2,3)

# print(add_two(2,3))

#LAMBDA FUNCTIONS
# def add(a,b):
#     return a + b

# addLambda = lambda x,y: x + y
# print(addLambda(1,4))

# OBJECT ORIENTED PROGRAMMING

# class Person:
#     age = 10
#     def greet(self):
#         print(f'hello {self.age}')
# print(Person.greet)

# me = Person()
# me.greet()

# TASK 2 - Create employees class and create id as private member

class Employee:
    def __init__(self):
        self.name = 'Bharavi'
        self.__EmpId = 1
        self.lastName = 'Lakhote'
    def printfirstname(self):
        return self.name
    def printlastname(self):
        return self.lastname
    def printemployeeid(self):
        return self.__EmpId
emp1 = Employee()
print(emp1.printfirstname())
print(emp1.printemployeeid())
print(emp1.__EmpId) # not accesible
# print([1,2,3,4,5]+[5,5,6])

# class Point:
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y
    
#     def __str__(self):
#         return f'({self.x}, {self.y})'
#     def __add__(self,other):
#         return Point(self.x + other.x, self.y + other.y)
    
# p1 = Point(1,2)
# p2 = Point(2,3)
# print(p1)
# print(p1+p2)

# TASK 3 - List all methods that could be used with Operator Overloading
# p1.__add__(p2)
# p1.__sub__(p2)
# p1.__mul__(p2)
# p1.__pow__(p2)
# p1.__truediv__(p2)
# p1.__floordiv__(p2)
# p1.__mod__(p2)
# p1.__lshift__(p2) #left shift
# p1.__rshift__(p2) #right shift
# p1.__and__(p2)
# p1.__or__(p2)
# p1.__xor__(p2)
# p1.__invert__()

# TASK 4 - Try to design basic calculator methods using OOPs
class Value:
    def __init__(self, value):
        self.value = value
    def __add__(self, other):
        return Value(self.value + other.value)
    def __sub__(self, other):
        return Value(self.value - other.value)
    def __mul__(self, other):
        return Value(self.value * other.value)
    def __truediv__(self, other):
        return Value(self.value / other.value)
    def __str__(self):
        return str(self.value)
print(Value(3)+Value(2))
print(Value(2)-Value(2))
print(Value(3)*Value(2))
print(Value(2)/Value(2))
# POLYMORPHISM
# def add(a,b,c=0):
#     return a + b + c
# print(add(5,4))
# print(add(5,4,8))

# TASK 5 - Create a class DIAT with subclasses like Finances and administration
class DIATstaff:
    def __init__(self):
        self.title = 'Title : Staff'
    def position(self):
        print(self.title)
class Professor(DIATstaff):
    def __init__(self):
        self.title = 'Title : Professor'
    def position(self):
        print(self.title)
class Admin(DIATstaff):
    def __init__(self):
        self.title = 'Title : Admin'
    def position(self):
        print(self.title)
class Finance(DIATstaff):
    def __init__(self):
        self.title = 'Title : Finance'
    def position(self):
        print(self.title)
diatstaff = DIATstaff()
diatProfessor = Professor()
diatadmin = Admin()
diatFinance = Finance()
diatstaff.position()
diatProfessor.position()
diatadmin.position()
diatFinance.position()