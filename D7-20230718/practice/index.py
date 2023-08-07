year=int(input("  Enter the year:"))
if(year%400==0 and year%100==0)or(year%4==0 and not year%100==0):
    print(" This is Leap Year")
else:
    print(" This is Not a Leap Year")
# number1=int(input("Enter the Number 1:"))
# number2=int(input("Enter the Number 2:"))
# if((number1%number2)==0):
#     print("It's Dividable")
# else:
#     print("It's Not dividable")
