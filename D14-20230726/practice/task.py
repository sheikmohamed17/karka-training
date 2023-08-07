# def a():
#     first_name="sheik"
#     last_name="mohamed"
#     name=first_name+" "+last_name
#     print(name)
#  a()
##
# first_name=input("Enter the first name:")
# def b(a,b):
#     print(a+" "+b)
# last_name=input("Enter the last name:")
# b(first_name,last_name)
##
# gender=input("Enter the Gender:")
# def gen(a):
#     if a=="Male":
#         print("The Color is Blue")
#     elif a=="Female":
#         print("The Color is Pink")
#     else:
#         print("Enter the Correct Gender")
# gen(gender)
##
# number_1=int(input("Enter the Number1:"))
# number_2=int(input("Enter the Number2:"))
# def greater_no(n1,n2):
#     if n1>n2:
#         print("Number 1:",number_1,"is Greater")
#         if n1%2==0:
#             print("this is even")
#         else:
#                 print("this is odd")
#     elif n1==n2:
#         print("Both are equal")
#     elif n2>n1:
#         print("Number 2:",number_2,"is Greater")
#         if n2%2==0:
#             print("This is even")
#         else:
#             print("This is odd")
# greater_no(number_1,number_2)
# ##
# number_1=int(input("Enter the n1:"))
# number_2=int(input("enter the n2:"))
# def odd_even(n):
#     if n%2==0:
#         print("This is even")
#     else:
#         print("this is odd")
# def max(n1,n2):
#     if n1<n2:
#         print("N2 is big")
#         odd_even(n2)
#     else:
#         print("n1 is big")
#         odd_even(n1)
# max(number_1,number_2)
f_input = int(input("Enter your first number"))
s_input = int(input("Enter your second number"))

def find_even_odd(number):
    if number%2==0:
            print("even")
    else:
            print("odd")

def find_max_number(f,s):
    
    if f<s:
        find_even_odd(s) 
        print("second input is max")
    elif s<f:
        find_even_odd(f) 
        print("first input is max")
    elif s==f:
        print("both are same")
    else:
        print("check the input")

find_max_number(f_input,s_input)  




            
            
#find_even_odd(4)
