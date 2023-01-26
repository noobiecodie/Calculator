from tkinter import *

print("#### Addition Calculator ####")
a = input("Enter your name:")
print("Welcome!", a)
x = input("Enter first number:")
m = input("Enter second number:")
z = input("Are you sure? [y/n]:")
l = "+"
k = "-"
j = "/"
h = "*"
t = "%"
u = input("Choose your operation : + - / * % : ")
if(z=="y"):
    print("Your operation is: ",u)
else:
    print("Thank you for visiting!")

if(u==l): 
    print("The answer is:",int(x) + int(m))
# else:
#     print("Try again!")

if(u==k):
    print("The answer is:",int(x) - int(m))
# else:
#     print("Try again!")

if(u==j):
    print("The answer is:",int(x) / int(m))
# else:
#     print("Try again!")

if(u==h):
    print("The answer is:",int(x) * int(m))
# else:
#     print("Try again!")

if(u==t):
    print("The answer is:",int(x) % int(m))
