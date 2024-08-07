#1. Write a program in Python to swap between two numbers without using a third variable.

def swap(a,b):
    a,b = b,a
    print("a = ",a,"\t\t","b = ",b)
a = int(input("Enter the value of a : "))
b = int(input("Enter the value of b : "))
swap(a,b)
