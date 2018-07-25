#!/usr/bin/env python
#This function adds two numbers.
def add(x,y):
	return x+y

#This fuction subtract two numbers.
def subtract(x,y):
    return x-y

#This function multiply two numbers.
def multiply(x,y):
    return x*y

#This function divide two numbers.
def divide(x,y):
    return x/y

print("Select Operation")
print("1 Add")
print("2 subtract") 
print("3 multiply")
print("4 divide")

#Take input from the user

choice=int(input("Enter choice(1/2/3/4):")) 
x=int(input("Enter frist number :"))
y=int(input("Enter second number :"))

if choice==1:
    print(x,'+',y,'=',add(x,y))


elif choice == 2:
    print(x,'-',y,'=',subtract(x,y))

elif choice == 3:
    print(x,'*',y,'=',multiply(x,y))

elif choice == 4:
     print(x,'/',y,'=',divide(x,y))
else:
    print("Invalid Operation")
