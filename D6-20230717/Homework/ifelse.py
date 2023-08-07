print("If you is eligible for Token")
billamount=int(input("Enter the your Bill Amount"))
if billamount>500 and billamount<=1000:
    print("You won a Silver Coin")
elif billamount>1000 and billamount<5000:
    print("You have won a Gold Coin")
elif billamount>=5000:
    print("You Won a Platinum Coin")
else:
     print("You not won a Coin" '\n' "Please Purshace High")    
# n=int(input("Enter the age : "))
# if 15<=n and 17>=n:
#     print("You is not eligble for drive")
# elif 17<n<25:
#     print("You is eligble for drive")
# gender=input("Enter the gender:")
# if gender== "Male":
#     print("Blue")
# elif gender=="female":
#     print("Pink")
# elif gender == "Third gender":
#     print("yellow")
